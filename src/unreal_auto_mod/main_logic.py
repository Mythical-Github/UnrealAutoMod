import os
import sys

import psutil
import pyjson5 as json

import unreal_auto_mod.gen_py_utils as gen_utils
from unreal_auto_mod import hook_states, log, mods
from unreal_auto_mod.log import log_message

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
    from unreal_auto_mod import log as log
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


def game_exe_check():
    from unreal_auto_mod import utilities
    check_file_exists(utilities.get_game_exe_path())


def git_info_check():
    from unreal_auto_mod.utilities import get_git_info_repo_path

    git_repo_path = get_git_info_repo_path()
    if git_repo_path == None or git_repo_path == '':
        return

    check_file_exists(git_repo_path)



def game_launcher_exe_override_check():
    from unreal_auto_mod import utilities
    if utilities.get_override_automatic_launcher_exe_finding():
        check_file_exists(utilities.get_game_launcher_exe_path())


def init_checks():
    from unreal_auto_mod import log as log
    from unreal_auto_mod import utilities
    if not utilities.get_should_ship_uproject_steps():
        check_file_exists(utilities.get_uproject_file())
        log.log_message('Check: Uproject file exists')

    unreal_engine_check()
    game_launcher_exe_override_check()
    git_info_check()
    game_exe_check()

    if utilities.get_is_using_repak_path_override():
        check_file_exists(utilities.get_repak_path_override())
        log.log_message('Check: Repak exists')

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
    mods.generate_mods()


def test_mods_all(settings_json: str):
    load_settings(settings_json)
    global mod_names
    for entry in settings['mods_info']:
        mod_names.append(entry['mod_name'])
    mods.generate_mods()


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
    from unreal_auto_mod.gen_py_utils import kill_process
    from unreal_auto_mod.utilities import get_game_exe_path
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
    if not utilities.does_umodel_exist(output_directory):
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
        with open(settings_json, encoding="utf-8") as file:
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
            log_message("No mods were enabled because all specified mods were already enabled.")

    except json.JSONDecodeError:
        log_message(f"Error decoding JSON from file '{settings_json}'. Please check the file format.")
    except Exception as e:
        log_message(f"An error occurred: {e}")


def disable_mods(settings_json: str, mod_names: list):
    try:
        with open(settings_json, encoding="utf-8") as file:
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
            log_message("No mods were disabled because all specified mods were already disabled.")

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
        with open(settings_json) as file:
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
        with open(settings_json, encoding="utf-8") as file:
            settings = json.load(file)

        mods_removed = False

        mods_info = settings.get("mods_info", [])
        mods_info = [mod for mod in mods_info if mod["mod_name"] not in mod_names]

        if len(mods_info) < len(settings.get("mods_info", [])):
            mods_removed = True
            log_message(f"Mods {', '.join(mod_names)} have been removed.")
        else:
            log_message("No mods were removed because none of the specified mods were found.")

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
    from unreal_auto_mod import ue_dev_py_utils, utilities
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
        log.log_message('Check: Game is iostore')
    else:
        log.log_message('Check: Game is not iostore')
    return command


def package(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.main_logic import mod_names
    from unreal_auto_mod.packing import generate_mods
    from unreal_auto_mod.utilities import get_mods_info_from_json

    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
    log_message('Packaging Starting')
    run_proj_build_command(get_solo_package_command())
    generate_mods()
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
    import shutil
    from unreal_auto_mod import utilities
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

    dist_dir = f'{SCRIPT_DIR}/dist'
    if os.path.isdir(dist_dir):
        shutil.rmtree(dist_dir)
    log_message(f'Cleaned up dist dir at: "{dist_dir}"')
    
    working_dir = utilities.get_working_dir()
    if os.path.isdir(working_dir):
        shutil.rmtree(working_dir)
    log_message(f'Cleaned up working dir at: "{working_dir}"')


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


def cleanup_game(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod import utilities
    game_directory = os.path.dirname(utilities.custom_get_game_dir())
    file_list_json = os.path.join(settings_json_dir, 'game_file_list.json')
    delete_unlisted_files(game_directory, file_list_json)


def generate_game_file_list_json(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod import utilities
    game_directory = os.path.dirname(utilities.custom_get_game_dir())
    file_list_json = os.path.join(settings_json_dir, 'game_file_list.json')
    generate_file_paths_json(game_directory, file_list_json)


def generate_mods(settings_json: str, input_mod_names: str):
    load_settings(settings_json)
    from unreal_auto_mod.main_logic import mod_names
    from unreal_auto_mod.packing import generate_mods
    from unreal_auto_mod.utilities import get_mods_info_from_json

    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
    generate_mods()


def generate_mods_all(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.main_logic import mod_names
    from unreal_auto_mod.packing import generate_mods
    from unreal_auto_mod.utilities import get_mods_info_from_json

    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
        print(entry['mod_name'])
    generate_mods()


def zip_directory_tree(input_dir, output_dir, zip_name="archive.zip"):
    import zipfile

    os.makedirs(output_dir, exist_ok=True)

    zip_path = os.path.join(output_dir, zip_name)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_dir)
                zipf.write(file_path, arcname)

    print(f"Directory tree zipped successfully: {zip_path}")


def make_unreal_pak_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    import shutil

    from unreal_auto_mod import utilities
    mod_name = singular_mod_info['mod_name']
    before_pak_file = f'{utilities.custom_get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.pak'
    final_pak_file = f'{base_files_directory}/{mod_name}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.pak'
    if os.path.isfile(final_pak_file):
        os.remove(final_pak_file)
    print(os.path.dirname(final_pak_file))
    os.makedirs(os.path.dirname(final_pak_file), exist_ok=True)
    shutil.copyfile(before_pak_file, final_pak_file)
    zip_directory_tree(input_dir=f'{base_files_directory}/{mod_name}', output_dir=output_directory, zip_name=f'{mod_name}.zip')


def make_repak_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    import shutil

    from unreal_auto_mod import utilities
    mod_name = singular_mod_info['mod_name']
    before_pak_file = f'{utilities.custom_get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.pak'
    final_pak_file = f'{base_files_directory}/{mod_name}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.pak'
    if os.path.isfile(final_pak_file):
        os.remove(final_pak_file)
    print(os.path.dirname(final_pak_file))
    os.makedirs(os.path.dirname(final_pak_file), exist_ok=True)
    shutil.copyfile(before_pak_file, final_pak_file)
    zip_directory_tree(input_dir=f'{base_files_directory}/{mod_name}', output_dir=output_directory, zip_name=f'{mod_name}.zip')


def make_engine_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    import shutil

    from unreal_auto_mod import ue_dev_py_utils, utilities
    mod_name = singular_mod_info['mod_name']
    uproject_file = utilities.get_uproject_file()
    mod_files = []
    pak_chunk_num = singular_mod_info['pak_chunk_num']
    uproject_file = utilities.get_uproject_file()
    uproject_dir = ue_dev_py_utils.get_uproject_dir(uproject_file)
    win_dir_str = ue_dev_py_utils.get_win_dir_str(utilities.get_unreal_engine_dir())
    uproject_name = ue_dev_py_utils.get_uproject_name(uproject_file)
    prefix = f'{uproject_dir}/Saved/StagedBuilds/{win_dir_str}/{uproject_name}/Content/Paks/pakchunk{pak_chunk_num}-{win_dir_str}.'
    mod_files.append(prefix)
    for file in mod_files:
        for suffix in ue_dev_py_utils.get_game_pak_folder_archives(uproject_file, utilities.custom_get_game_dir()):
            dir_engine_mod = f'{utilities.custom_get_game_dir()}/Content/Paks/{utilities.get_pak_dir_structure(mod_name)}'
            os.makedirs(dir_engine_mod, exist_ok=True)
            before_file = f'{file}{suffix}'
            after_file = f'{base_files_directory}/{mod_name}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.{suffix}'
            if os.path.isfile(after_file):
                os.remove(after_file)
            os.makedirs(os.path.dirname(after_file), exist_ok=True)
            shutil.copyfile(before_file, after_file)
    zip_directory_tree(input_dir=f'{base_files_directory}/{mod_name}', output_dir=output_directory, zip_name=f'{mod_name}.zip')


def get_mod_files_asset_paths_for_loose_mods(mod_name: str, base_files_directory: str) -> dict:
    from unreal_auto_mod import gen_py_utils, packing, ue_dev_py_utils, utilities
    file_dict = {}
    cooked_uproject_dir = ue_dev_py_utils.get_cooked_uproject_dir(utilities.get_uproject_file(), utilities.get_unreal_engine_dir())
    mod_info = packing.get_mod_pak_entry(mod_name)
    for asset in mod_info['manually_specified_assets']['asset_paths']:
        base_path = f'{cooked_uproject_dir}/{asset}'
        for extension in gen_py_utils.general_utils.get_file_extensions(base_path):
            before_path = f'{base_path}{extension}'
            after_path = f'{base_files_directory}/{mod_name}/mod_files/{asset}{extension}'
            file_dict[before_path] = after_path
    return file_dict


def get_mod_files_tree_paths_for_loose_mods(mod_name: str, base_files_directory: str) -> dict:
    from unreal_auto_mod import gen_py_utils, packing, ue_dev_py_utils, utilities
    file_dict = {}
    cooked_uproject_dir = ue_dev_py_utils.get_cooked_uproject_dir(utilities.get_uproject_file(), utilities.get_unreal_engine_dir())
    mod_info = packing.get_mod_pak_entry(mod_name)
    for tree in mod_info['manually_specified_assets']['tree_paths']:
        tree_path = f'{cooked_uproject_dir}/{tree}'
        for entry in gen_py_utils.get_files_in_tree(tree_path):
            if os.path.isfile(entry):
                base_entry = os.path.splitext(entry)[0]
                for extension in gen_py_utils.get_file_extensions_two(entry):
                    before_path = f'{base_entry}{extension}'
                    relative_path = os.path.relpath(base_entry, cooked_uproject_dir)
                    after_path = f'{base_files_directory}/{mod_name}/mod_files/{relative_path}{extension}'
                    file_dict[before_path] = after_path
    return file_dict


def get_mod_files_persistent_paths_for_loose_mods(mod_name: str, base_files_directory: str) -> dict:
    from unreal_auto_mod import utilities
    file_dict = {}
    persistent_mod_dir = utilities.get_persistant_mod_dir(mod_name)

    for root, _, files in os.walk(persistent_mod_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, persistent_mod_dir)
            after_path = f'{base_files_directory}/{mod_name}/mod_files/{relative_path}'
            file_dict[file_path] = after_path
    return file_dict


def get_mod_files_mod_name_dir_paths_for_loose_mods(mod_name: str, base_files_directory: str) -> dict:
    from unreal_auto_mod import gen_py_utils, ue_dev_py_utils, utilities
    file_dict = {}
    cooked_game_name_mod_dir = f'{ue_dev_py_utils.get_cooked_uproject_dir(utilities.get_uproject_file(), utilities.get_unreal_engine_dir())}/Content/{utilities.get_unreal_mod_tree_type_str(mod_name)}/{utilities.get_mod_name_dir_name(mod_name)}'

    for file in gen_py_utils.get_files_in_tree(cooked_game_name_mod_dir):
        relative_file_path = os.path.relpath(file, cooked_game_name_mod_dir)
        before_path = os.path.abspath(file)
        after_path = f'{base_files_directory}/{mod_name}/mod_files/{relative_file_path}'
        file_dict[before_path] = after_path
    return file_dict


def get_mod_paths_for_loose_mods(mod_name: str, base_files_directory: str) -> dict:
    file_dict = {}
    file_dict.update(get_mod_files_asset_paths_for_loose_mods(mod_name, base_files_directory))
    file_dict.update(get_mod_files_tree_paths_for_loose_mods(mod_name, base_files_directory))
    file_dict.update(get_mod_files_persistent_paths_for_loose_mods(mod_name, base_files_directory))
    file_dict.update(get_mod_files_mod_name_dir_paths_for_loose_mods(mod_name, base_files_directory))

    return file_dict


def make_loose_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    import shutil
    mod_name = singular_mod_info['mod_name']
    mod_files = get_mod_paths_for_loose_mods(mod_name, base_files_directory)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        before_file = key
        after_file = mod_files[key]
        os.makedirs(os.path.dirname(after_file), exist_ok=True)
        if os.path.exists(before_file):
            if os.path.islink(after_file):
                os.unlink(after_file)
            if os.path.isfile(after_file):
                os.remove(after_file)
        if os.path.isfile(before_file):
            shutil.copy(before_file, after_file)
    zip_directory_tree(input_dir=f'{base_files_directory}/{mod_name}', output_dir=output_directory, zip_name=f'{mod_name}.zip')


def generate_mod_release(settings_json: str, mod_name: str, base_files_directory: str, output_directory: str):
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


def generate_mod_releases(settings_json: str, mod_names: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    for mod_name in mod_names:
        generate_mod_release(settings_json, mod_name, base_files_directory, output_directory)


def generate_mod_releases_all(settings_json: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_mods_info_from_json
    for entry in get_mods_info_from_json():
        generate_mod_release(settings_json, entry['mod_name'], base_files_directory, output_directory)


def resync_dir_with_repo(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_cleanup_repo_path, run_app
    repo_path = get_cleanup_repo_path()
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
    run_app(exe_path=exe, args=args, working_dir=repo_path)

    args = [
        'reset',
        '--hard'
    ]
    run_app(exe_path=exe, args=args, working_dir=repo_path)

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
        if engine_minor_association not in range(28):  # Valid range is 0-27
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
            f.write(json_content)
    except OSError as e:
        raise OSError(f"Failed to write to file '{project_file}': {e}")

    return f"Successfully generated '{project_file}'."


def save_json_to_file(json_string, file_path):
    try:
        parsed_json = json.loads(json_string)

        with open(file_path, "w") as file:
            json.dump(parsed_json, file, indent=4)

        print(f"JSON data successfully saved to {file_path}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON string: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_file_paths_json(dir_path, output_json):
    all_file_paths = []

    for root, _, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_file_paths.append(full_path)

    json_string = json.dumps(all_file_paths)

    with open(output_json, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)

    print(f"JSON file with all file paths created at: {output_json}")


def delete_unlisted_files(dir_path, json_file):
    try:
        with open(json_file) as file:
            allowed_files = set(json.load(file))

        for root, _, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)
                if full_path not in allowed_files:
                    os.remove(full_path)
                    print(f"Deleted: {full_path}")

        print("Cleanup complete. All unlisted files have been removed.")
    except Exception as e:
        print(f"An error occurred: {e}")





def close_programs(exe_names: list[str]):
    import psutil

    results = {}

    for exe_name in exe_names:
        found = False
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == exe_name.lower():
                    proc.terminate()
                    proc.wait(timeout=5)
                    found = True
                    results[exe_name] = "Closed"
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass
        if not found:
            results[exe_name] = "Not Found"
    
    return results
