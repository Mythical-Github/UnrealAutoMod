import os
import sys

import psutil
import pyjson5 as json

import unreal_auto_mod.gen_py_utils as gen_utils
from unreal_auto_mod import hook_states, mods
from unreal_auto_mod.log_py import log_message

settings = ''
init_settings_done = False
settings_json_dir = ''
program_dir = ''
mod_names = []
settings_json = ''


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


def init_settings(settings_json_path: str):
    global settings
    global init_settings_done
    global settings_json
    global settings_json_dir

    with open(settings_json_path) as file:
        settings = json.load(file)
    window_name = settings['general_info']['window_title']
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(window_name)
    auto_close_game = settings['process_kill_events']['auto_close_game']
    if auto_close_game:
        def is_process_running(process_name):
            for proc in psutil.process_iter():
                try:
                    if process_name.lower() in proc.name().lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False

        process_name = settings['game_info']['game_exe_path']
        process_name = os.path.basename(process_name)
        if is_process_running(process_name):
            os.system(f'taskkill /f /im "{process_name}"')
    init_settings_done = True
    settings_json = settings_json_path
    settings_json_dir = os.path.dirname(settings_json)


def check_file_exists(file_path: str) -> bool:
    if os.path.exists(file_path):
        return True
    else:
        raise FileNotFoundError(f'File "{file_path}" not found.')


def unreal_engine_check():
    from unreal_auto_mod import log_py as log
    from unreal_auto_mod import ue_dev_py_utils as ue_dev_utils
    from unreal_auto_mod import utilities

    should_do_check = True

    if utilities.get_should_ship_uproject_steps():
        if not utilities.is_unreal_pak_packing_enum_in_use():
               should_do_check = False

    if should_do_check:
        engine_str = 'UE4Editor'
        if ue_dev_utils.is_game_ue5(utilities.get_unreal_engine_dir()):
            engine_str = 'UnrealEditor'
        check_file_exists(f'{utilities.get_unreal_engine_dir()}/Engine/Binaries/Win64/{engine_str}.exe')
        log.log_message('Check: Unreal Engine exists')


def init_checks():
    from unreal_auto_mod import log_py as log
    from unreal_auto_mod import utilities
    if not utilities.get_should_ship_uproject_steps():
        check_file_exists(utilities.get_uproject_file())
        log.log_message('Check: Uproject file exists')

    unreal_engine_check()

    if utilities.get_is_using_repak_path_override():
        check_file_exists(utilities.get_repak_path_override())
        log.log_message('Check: Repak exists')

    if not utilities.get_skip_launching_game():
        check_file_exists(utilities.get_game_exe_path())
        log.log_message('Check: Game exists')

    log.log_message('Check: Passed all init checks')


def load_settings(settings_json: str):
    if not init_settings_done:
        init_settings(settings_json)
    init_checks()
    with open(settings_json) as file:
        return json.load(file)


def save_settings(settings_json: str):
    with open(settings_json, 'w') as file:
        json.dump(settings, file, indent=2)


def pass_settings(settings_json: str):
    load_settings(settings_json)


def init_thread_system():
    from unreal_auto_mod import enums, thread_constant
    hook_states.set_hook_state(enums.HookStateType.INIT)
    thread_constant.constant_thread()
    hook_states.set_hook_state(enums.HookStateType.POST_INIT)


def close_thread_system():
    from unreal_auto_mod import thread_constant
    thread_constant.stop_constant_thread()


# all things below this should be functions that correspond to cli logic


def test_mods(settings_json: str, input_mod_names: str):
    load_settings(settings_json)
    global mod_names
    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    from unreal_auto_mod.packing import populate_queue
    populate_queue()
    mods.create_mods(settings_json)


def test_mods_all(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.packing import populate_queue
    global mod_names
    for entry in settings['mods_info']:
        mod_names.append(entry['mod_name'])
    populate_queue()
    mods.create_mods()


def install_stove(output_directory: str, run_after_install: bool):
    from unreal_auto_mod import utilities
    if not utilities.does_stove_exist(output_directory):
        utilities.install_stove(output_directory)
    if run_after_install:
        utilities.run_app(utilities.get_stove_path(output_directory))


def install_spaghetti(output_directory: str, run_after_install: bool):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_spaghetti_path(output_directory)):
        utilities.install_spaghetti(output_directory)
    if run_after_install:
        utilities.run_app(utilities.get_spaghetti_path(output_directory))


def install_kismet_analyzer(output_directory: str, run_after_install: bool):
    from unreal_auto_mod import utilities
    # add shell stuff to run app later or something
    if not os.path.isfile(utilities.get_kismet_analyzer_path(output_directory)):
        utilities.install_kismet_analyzer(output_directory)
    if run_after_install:
        import subprocess
        kismet_analyzer_path = utilities.get_kismet_analyzer_path(output_directory)
        kismet_directory = os.path.dirname(kismet_analyzer_path)
        command = f'cd /d "{kismet_directory}" && "{kismet_analyzer_path}" -h && set ka=kismet-analyzer.exe && cmd /k'
        subprocess.run(command, shell=True, check=False)


def install_uasset_gui(output_directory: str, run_after_install: bool):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_uasset_gui_path(output_directory)):
        utilities.install_uasset_gui(output_directory)
    if run_after_install:
        utilities.run_app(utilities.get_uasset_gui_path(output_directory))


def open_latest_log(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod import log_info
    log_prefix = log_info.LOG_INFO['log_name_prefix']
    file_to_open = f'{SCRIPT_DIR}/logs/{log_prefix}latest.log'
    gen_utils.open_file_in_default(file_to_open)


def run_game(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod import game_runner, thread_game_monitor
    game_runner.run_game()
    thread_game_monitor.game_monitor_thread()


def close_game(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_game_exe_path
    from unreal_auto_mod.gen_py_utils import kill_process
    kill_process(os.path.basename(get_game_exe_path()))


def run_engine(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.engine import open_game_engine
    open_game_engine()


def close_engine(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.engine import close_game_engine
    close_game_engine()


def install_umodel(output_directory: str, run_after_install: bool):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.does_umodel_exist(output_directory)):
        utilities.install_umodel(output_directory)
    # Sets dir, so it's the dir opened by default in umodel
    # os.chdir(os.path.dirname(utilities.custom_get_game_dir()))
    if run_after_install:
       utilities.run_app(utilities.get_umodel_path(output_directory))


def install_fmodel(output_directory: str, run_after_install: bool):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_fmodel_path(output_directory)):
        utilities.install_fmodel(output_directory)
    if run_after_install:
        utilities.run_app(utilities.get_fmodel_path(output_directory))


def get_solo_build_project_command() -> str:
    from unreal_auto_mod import utilities
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat {utilities.get_unreal_engine_building_main_command()} '
        f'-project="{utilities.get_uproject_file()}" '
    )
    for arg in utilities.get_engine_building_args():
            command = f'{command} {arg}'
    return command


def run_proj_build_command(command: str):
    command_parts = command.split(' ')
    executable = command_parts[0]
    args = command_parts[1:]
    from unreal_auto_mod import utilities
    utilities.run_app(exe_path=executable, args=args, working_dir=utilities.get_unreal_engine_dir())


def build(settings_json: str):
    load_settings(settings_json)
    log_message('Project Building Starting')
    run_proj_build_command(get_solo_build_project_command())
    log_message('Project Building Complete')


def upload_changes_to_repo(settings_json: str):
    import subprocess
    load_settings(settings_json)
    repo_path = settings['git_info']['repo_path']
    branch = settings['git_info']['repo_branch']
    desc = input("Enter commit description: ")

    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=repo_path, check=False)
    if status_result.returncode != 0 or not status_result.stdout.strip():
        log_message("No changes detected or not in a Git repository.")
        sys.exit(1)

    checkout_result = subprocess.run(["git", "checkout", branch], capture_output=True, text=True, cwd=repo_path, check=False)
    if checkout_result.returncode != 0:
        log_message(f"Failed to switch to the {branch} branch.")
        sys.exit(1)

    subprocess.run(["git", "add", "."], check=True, cwd=repo_path)

    commit_result = subprocess.run(["git", "commit", "-m", desc], capture_output=True, text=True, cwd=repo_path, check=False)
    if commit_result.returncode != 0:
        log_message("Commit failed.")
        sys.exit(1)

    push_result = subprocess.run(["git", "push", "origin", branch], capture_output=True, text=True, cwd=repo_path, check=False)
    if push_result.returncode != 0:
        log_message("Push failed.")
        sys.exit(1)

    log_message("Changes committed and pushed successfully.")


def enable_mods(settings_json: str, mod_names: list):
    try:
        with open(settings_json, "r", encoding="utf-8") as file:
            settings = json.load(file)

        mods_enabled = False

        for mod in settings.get("mods_info", []):
            if mod["mod_name"] in mod_names:
                if not mod["is_enabled"]:
                    mod["is_enabled"] = True
                    mods_enabled = True
                    log_message(f"Mod '{mod['mod_name']}' has been enabled.")
                else:
                    log_message(f"Mod '{mod['mod_name']}' is already enabled.")

        if mods_enabled:
            updated_json_str = json.dumps(settings, indent=4, ensure_ascii=False, separators=(',', ': '))

            with open(settings_json, "w", encoding="utf-8") as file:
                file.write(updated_json_str)

            log_message(f"Mods successfully enabled in '{settings_json}'.")
        else:
            log_message(f"No mods were enabled because all specified mods were already enabled.")
    
    except json.JSONDecodeError:
        log_message(f"Error decoding JSON from file '{settings_json}'. Please check the file format.")
    except Exception as e:
        log_message(f"An error occurred: {e}")
    

def disable_mods(settings_json: str, mod_names: list):
    try:
        with open(settings_json, "r", encoding="utf-8") as file:
            settings = json.load(file)

        mods_disabled = False

        for mod in settings.get("mods_info", []):
            if mod["mod_name"] in mod_names:
                if mod["is_enabled"]:
                    mod["is_enabled"] = False
                    mods_disabled = True
                    log_message(f"Mod '{mod['mod_name']}' has been disabled.")
                else:
                    log_message(f"Mod '{mod['mod_name']}' is already disabled.")

        if mods_disabled:
            updated_json_str = json.dumps(settings, indent=4, ensure_ascii=False, separators=(',', ': '))

            with open(settings_json, "w", encoding="utf-8") as file:
                file.write(updated_json_str)

            log_message(f"Mods successfully disabled in '{settings_json}'.")
        else:
            log_message(f"No mods were disabled because all specified mods were already disabled.")
    
    except json.JSONDecodeError:
        log_message(f"Error decoding JSON from file '{settings_json}'. Please check the file format.")
    except Exception as e:
        log_message(f"An error occurred: {e}")
    
    
def add_mod(
        settings_json: str, 
        mod_name: str, 
        packing_type: str, 
        pak_dir_structure: str,
        mod_name_dir_type: str,
        use_mod_name_dir_name_override: str,
        mod_name_dir_name_override: str,
        pak_chunk_num: int,
        compression_type: str,
        is_enabled: bool,
        asset_paths: list,
        tree_paths: list
    ):
    try:
        with open(settings_json, "r") as file:
            settings = json.load(file)

        new_mod = {
            "mod_name": mod_name,
            "pak_dir_structure": pak_dir_structure,
            "mod_name_dir_type": mod_name_dir_type,
            "use_mod_name_dir_name_override": use_mod_name_dir_name_override,
            "mod_name_dir_name_override": mod_name_dir_name_override,
            "pak_chunk_num": pak_chunk_num,
            "packing_type": packing_type,
            "compression_type": compression_type,
            "is_enabled": is_enabled,
            "manually_specified_assets": {
                "asset_paths": asset_paths,
                "tree_paths": tree_paths
            }
        }

        if "mods_info" not in settings:
            settings["mods_info"] = []

        existing_mod = next((mod for mod in settings["mods_info"] if mod["mod_name"] == mod_name), None)
        if existing_mod:
            log_message(f"Mod '{mod_name}' already exists. Updating its data.")
            settings["mods_info"].remove(existing_mod)

        settings["mods_info"].append(new_mod)

        settings = json.dumps(settings, indent=4)

        with open(settings_json, "w") as file:
            file.write(settings)

        log_message(f"Mod '{mod_name}' successfully added/updated in '{settings_json}'.")
    except json.JSONDecodeError:
        log_message(f"Error decoding JSON from file '{settings_json}'. Please check the file format.")
    except Exception as e:
        log_message(f"An error occurred: {e}")
    
    
def remove_mods(settings_json: str, mod_names: list):
    try:
        with open(settings_json, "r", encoding="utf-8") as file:
            settings = json.load(file)

        mods_removed = False

        mods_info = settings.get("mods_info", [])
        mods_info = [mod for mod in mods_info if mod["mod_name"] not in mod_names]

        if len(mods_info) < len(settings.get("mods_info", [])):
            mods_removed = True
            log_message(f"Mods {', '.join(mod_names)} have been removed.")
        else:
            log_message(f"No mods were removed because none of the specified mods were found.")

        settings["mods_info"] = mods_info

        if mods_removed:
            updated_json_str = json.dumps(settings, indent=4, ensure_ascii=False, separators=(',', ': '))

            with open(settings_json, "w", encoding="utf-8") as file:
                file.write(updated_json_str)

            log_message(f"Mods successfully removed from '{settings_json}'.")
    
    except json.JSONDecodeError:
        log_message(f"Error decoding JSON from file '{settings_json}'. Please check the file format.")
    except Exception as e:
        log_message(f"An error occurred: {e}")


def get_solo_cook_project_command() -> str:
    from unreal_auto_mod import ue_dev_py_utils, utilities
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat {utilities.get_unreal_engine_cooking_main_command()} '
        f'-project="{utilities.get_uproject_file()}" '
    )
    if not ue_dev_py_utils.has_build_target_been_built(utilities.get_uproject_file()):
        build_arg = '-build'
        command = f'{command} {build_arg}'
    for arg in utilities.get_engine_cooking_args():
        command = f'{command} {arg}'
    return command


def cook(settings_json: str):
    log_message('Content Cooking Starting')
    load_settings(settings_json)
    run_proj_build_command(get_solo_cook_project_command())
    log_message('Content Cook Complete')


def get_solo_package_command() -> str:
    from unreal_auto_mod import utilities, ue_dev_py_utils, log_py
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat {utilities.get_unreal_engine_packaging_main_command()} '
        f'-project="{utilities.get_uproject_file()}" '
        f'-compressed'
    )
    # technically it shouldn't auto build itself, since this is not a auto run sequence but used in an explicit command
    # if not ue_dev_py_utils.has_build_target_been_built(utilities.get_uproject_file()):
    #     command = f'{command} -build'
    for arg in utilities.get_engine_packaging_args():
        command = f'{command} {arg}'
    is_game_iostore = ue_dev_py_utils.get_is_game_iostore(utilities.get_uproject_file(), utilities.custom_get_game_dir())
    if is_game_iostore:
        command = f'{command} -iostore'
        log_py.log_message('Check: Game is iostore')
    else:
        log_py.log_message('Check: Game is not iostore')
    return command


def package(settings_json: str):    
    load_settings(settings_json)
    from unreal_auto_mod.main_logic import mod_names
    from unreal_auto_mod.utilities import get_mods_info_from_json
    from unreal_auto_mod.packing import make_mods_two, populate_queue

    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
    log_message('Packaging Starting')
    run_proj_build_command(get_solo_package_command())
    populate_queue()
    make_mods_two()
    log_message('Packaging Complete')


def resave_packages_and_fix_up_redirectors(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod import ue_dev_py_utils, utilities
    from unreal_auto_mod.engine import close_game_engine
    close_game_engine()
    arg = '-run=ResavePackages -fixupredirects'
    command = f'"{ue_dev_py_utils.get_unreal_editor_exe_path(utilities.get_unreal_engine_dir())}" "{utilities.get_uproject_file()}" {arg}'
    utilities.run_app(command)


def cleanup_full(settings_json: str):
    from unreal_auto_mod.enums import ExecutionMode
    from unreal_auto_mod.utilities import get_cleanup_repo_path, run_app
    load_settings(settings_json)
    repo_path = get_cleanup_repo_path()
    log_message(f'Cleaning up repo at: "{repo_path}"')
    exe = 'git'
    args = [
        'clean',
        '-d',
        '-X',
        '--force'
    ]
    run_app(exe_path=exe, exec_mode=ExecutionMode.ASYNC, args=args, working_dir=repo_path)
    log_message(f'Cleaned up repo at: "{repo_path}"')


def cleanup_cooked(settings_json: str):
    import os
    import shutil

    from unreal_auto_mod.utilities import get_cleanup_repo_path
    load_settings(settings_json)
    repo_path = get_cleanup_repo_path()

    log_message(f'Starting cleanup of Unreal Engine build directories in: "{repo_path}"')

    build_dirs = [
        'Cooked'
    ]

    for root, dirs, files in os.walk(repo_path):
        for dir_name in dirs:
            if dir_name in build_dirs:
                full_path = os.path.normpath(os.path.join(root, dir_name))
                try:
                    shutil.rmtree(full_path)
                    log_message(f'Removed directory: {full_path}')
                except Exception as e:
                    log_message(f"Failed to remove {full_path}: {e}")


def cleanup_build(settings_json: str):
    import os
    import shutil

    from unreal_auto_mod.utilities import get_cleanup_repo_path
    load_settings(settings_json)
    repo_path = get_cleanup_repo_path()

    log_message(f'Starting cleanup of Unreal Engine build directories in: "{repo_path}"')

    build_dirs = [
        'Intermediate',
        'DerivedDataCache',
        'Build',
        'Binaries',
    ]

    for root, dirs, files in os.walk(repo_path):
        for dir_name in dirs:
            if dir_name in build_dirs:
                full_path = os.path.normpath(os.path.join(root, dir_name))
                try:
                    shutil.rmtree(full_path)
                    log_message(f'Removed directory: {full_path}')
                except Exception as e:
                    log_message(f"Failed to remove {full_path}: {e}")


def create_mods(settings_json: str, input_mod_names: str):
    load_settings(settings_json)
    from unreal_auto_mod.packing import make_mods_two, populate_queue
    from unreal_auto_mod.main_logic import mod_names
    from unreal_auto_mod.utilities import get_mods_info_from_json

    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
    populate_queue()
    make_mods_two()


def create_mods_all(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.packing import make_mods_two, populate_queue
    from unreal_auto_mod.main_logic import mod_names
    from unreal_auto_mod.utilities import get_mods_info_from_json

    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
        print(entry['mod_name'])
    populate_queue()
    make_mods_two()


def make_unreal_pak_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    # get the installed pak files based on info from the json
    # move into the base files folder keeping the dir structure
    # zip into output dir
    print('placeholder')


def make_repak_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    # get the installed pak files based on info from the json
    # move into the base files folder keeping the dir structure
    # zip into output dir
    print('placeholder')


def make_engine_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    # get the installed pak files based on info from the json
    # move into the base files folder keeping the dir structure
    # zip into output dir
    print('placeholder')


def make_loose_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    # get files from saved coooked
    # get files from persistent
    # get files from specified dirs and assets in manually specified list
    # move them all into  the base files folder within a content folder
    # zip into the output directory
    print('placeholder')


def create_mod_release(settings_json: str, mod_name: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_mods_info_from_json
    singular_mod_info = next((mod_info for mod_info in get_mods_info_from_json() if mod_info['mod_name'] == mod_name), '')
    if singular_mod_info['packing_type'] == 'unreal_pak':
        make_unreal_pak_mod_release(singular_mod_info, base_files_directory, output_directory)
    elif singular_mod_info['packing_type'] == 'repak':
        make_repak_mod_release(singular_mod_info, base_files_directory, output_directory)
    elif singular_mod_info['packing_type'] == 'engine':
        make_engine_mod_release(singular_mod_info, base_files_directory, output_directory)
    elif singular_mod_info['packing_type'] == 'loose':
        make_loose_mod_release(singular_mod_info, base_files_directory, output_directory)


def create_mod_releases(settings_json: str, mod_names: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    for mod_name in mod_names:
        create_mod_release(settings_json, mod_name, base_files_directory, output_directory)


def create_mod_releases_all(settings_json: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_mods_info_from_json
    for entry in get_mods_info_from_json():
        create_mod_release(settings_json, entry['mod_name'], base_files_directory, output_directory)


def resync_dir_with_repo(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import run_app, get_cleanup_repo_path
    repo_path = get_cleanup_repo_path()
    repo_dir = os.path.dirname(repo_path)
    """
    Resyncs a directory tree with its repository by discarding local changes and cleaning untracked files.
    
    :param repo_path: The path to the root of the git repository.
    """
    repo_path = os.path.abspath(repo_path)
    
    if not os.path.isdir(repo_path):
        raise FileNotFoundError(f"The specified path '{repo_path}' does not exist or is not a directory.")
    
    if not os.path.isdir(os.path.join(repo_path, '.git')):
        raise ValueError(f"The specified path '{repo_path}' is not a valid Git repository.")

    exe = 'git'

    args = [
        'clean',
        '-f',
        '-d',
        '-x'
    ]
    run_app(exe_path=exe, args=args, working_dir=repo_dir)

    args = [
        'reset',
        '--hard'
    ]
    run_app(exe_path=exe, args=args, working_dir=repo_dir)

    print(f"Successfully resynchronized the repository at '{repo_path}'.")


def generate_uproject(
    project_file: str,
    file_version: int = 3, 
    engine_major_association: int = 4, 
    engine_minor_association: int = 27,
    category: str = 'Modding',
    description: str = 'Uproject for modding, generated with unreal_auto_mod.',
    ignore_safety_checks: bool = False
) -> str:
    from unreal_auto_mod.ue_dev_py_utils import get_new_uproject_json_contents

    project_dir = os.path.dirname(project_file)
    os.makedirs(project_dir, exist_ok=True)

    if ignore_safety_checks == False:
    # Validate file version
        if file_version not in range(1, 4):
            raise ValueError(f'Invalid file version: {file_version}. Valid values are 1-3.')

        # Validate EngineMajorAssociation
        if engine_major_association not in range(4, 6):  # Only 4-5 is valid
            raise ValueError(f'Invalid EngineMajorAssociation: {engine_major_association}. Valid value is 4-5.')

        # Validate EngineMinorAssociation
        if engine_minor_association not in range(0, 28):  # Valid range is 0-27
            raise ValueError(f'Invalid EngineMinorAssociation: {engine_minor_association}. Valid range is 0-27.')

        # Ensure the directory is empty
        project_dir = os.path.dirname(os.path.abspath(project_file))
        if os.path.exists(project_dir) and os.listdir(project_dir):
            raise FileExistsError(f'The directory "{project_dir}" is not empty. Cannot generate project here.')

    # Generate the JSON content for the .uproject file
    json_content = get_new_uproject_json_contents(
        file_version, engine_major_association, engine_minor_association, category, description
    )

    # Write the .uproject file
    try:
        with open(project_file, 'w') as f:
            f.write(json_content)  # Write the string content directly to the file
    except IOError as e:
        raise IOError(f"Failed to write to file '{project_file}': {e}")

    return f"Successfully generated '{project_file}'."
