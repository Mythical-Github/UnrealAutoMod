import os
import sys

import psutil
import pyjson5 as json

from unreal_auto_mod.log_py import log_message
import unreal_auto_mod.gen_py_utils as gen_utils
from unreal_auto_mod import hook_states, mods


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
            for proc in psutil.process_iter(process_name):
                try:
                    if process_name.lower() == proc.info['name'].lower():
                        proc.terminate()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
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
    from unreal_auto_mod import (
            enums,
            thread_constant
        )
    hook_states.HookState.set_hook_state(enums.HookStateType.INIT)
    thread_constant.constant_thread()
    hook_states.HookState.set_hook_state(enums.HookStateType.POST_INIT)


def close_thread_system():
    from unreal_auto_mod import thread_constant
    thread_constant.stop_constant_thread()


# all things below this should be functions that correspond to cli logic


def test_mods(settings_json: str, input_mod_names: str):
    load_settings(settings_json)
    global mod_names
    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    mods.create_mods()


def test_mods_all(settings_json: str):
    load_settings(settings_json)
    global mod_names
    for entry in settings['mods_info']:
        mod_names.append(entry['mod_name'])
    mods.create_mods()


def install_stove(output_directory: str):
    from unreal_auto_mod import utilities
    if not utilities.does_stove_exist(output_directory):
        utilities.install_stove(output_directory)
    utilities.run_app(utilities.get_stove_path(output_directory))


def install_spaghetti(output_directory: str):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_spaghetti_path(output_directory)):
        utilities.install_spaghetti(output_directory)
    utilities.run_app(utilities.get_spaghetti_path(output_directory))


def install_kismet_analyzer(output_directory: str):
    from unreal_auto_mod import utilities
    # add shell stuff to run app later or something
    if not os.path.isfile(utilities.get_kismet_analyzer_path(output_directory)):
        utilities.install_kismet_analyzer(output_directory)
    import subprocess
    kismet_analyzer_path = utilities.get_kismet_analyzer_path(output_directory)
    kismet_directory = os.path.dirname(kismet_analyzer_path)
    command = f'cd /d "{kismet_directory}" && "{kismet_analyzer_path}" -h && set ka=kismet-analyzer.exe && cmd /k'
    subprocess.run(command, shell=True, check=False)


def install_uasset_gui(output_directory: str):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_uasset_gui_path(output_directory)):
        utilities.install_uasset_gui(output_directory)
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


def install_umodel(output_directory: str):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.does_umodel_exist(output_directory)):
        utilities.install_umodel(output_directory)
    # Sets dir, so it's the dir opened by default in umodel
    # os.chdir(os.path.dirname(utilities.custom_get_game_dir()))
    utilities.run_app(utilities.get_umodel_path(output_directory))


def install_fmodel(output_directory: str):
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_fmodel_path(output_directory)):
        utilities.install_fmodel(output_directory)
    utilities.run_app(utilities.get_fmodel_path(output_directory))


def get_solo_build_project_command() -> str:
    from unreal_auto_mod import utilities
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
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


def get_solo_cook_project_command() -> str:
    from unreal_auto_mod import utilities, ue_dev_py_utils
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{utilities.get_uproject_file()}" '
    )
    if not ue_dev_py_utils.has_build_target_been_built(utilities.get_uproject_file()):
        build_arg = '-build'
        command = f'{command} {build_arg}'
    for arg in utilities.get_engine_packaging_args():
        command = f'{command} {arg}'
    for arg in utilities.get_engine_cooking_args():
        command = f'{command} {arg}'
    return command


def cook(settings_json: str):
    log_message('Content Cooking Starting')
    load_settings(settings_json)
    run_proj_build_command(get_solo_cook_project_command())
    log_message('Content Cook Complete')


def resave_packages_and_fix_up_redirectors(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.engine import close_game_engine
    from unreal_auto_mod import utilities, ue_dev_py_utils
    close_game_engine()
    arg = '-run=ResavePackages -fixupredirects'
    command = f'"{ue_dev_py_utils.get_unreal_editor_exe_path(utilities.get_unreal_engine_dir())}" "{utilities.get_uproject_file()}" {arg}'
    utilities.run_app(command)


def cleanup_full(settings_json: str):
    from unreal_auto_mod.enums import ExecutionMode
    from unreal_auto_mod.utilities import run_app, get_cleanup_repo_path
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
    from unreal_auto_mod.settings import mod_names
    from unreal_auto_mod.utilities import get_mods_info_from_json
    from unreal_auto_mod.packing import make_mods_two, populate_queue

    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
    populate_queue()
    make_mods_two()


def create_mods_all(settings_json: str):
    load_settings(settings_json)
    from unreal_auto_mod.settings import mod_names
    from unreal_auto_mod.utilities import get_mods_info_from_json
    from unreal_auto_mod.packing import make_mods_two, populate_queue

    for entry in get_mods_info_from_json():
        mod_names.append(entry['mod_name'])
        print(entry['mod_name'])
    populate_queue()
    make_mods_two()


def make_archive_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    # get the installed pak files based on info from the json
    # move into the base files folder keeping the dir structure
    # zip into output dir
    print('placeholder')
    return


def make_loose_mod_release(singular_mod_info: dict, base_files_directory: str, output_directory: str):
    # get files from saved coooked
    # get files from persistent
    # get files from specified dirs in manually specified asssets
    # move them all into  the base files folder within a content folder
    # zip into the output directory
    print('placeholder')
    return


def create_mod_release(settings_json: str, mod_name: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_mods_info_from_json
    singular_mod_info = next((mod_info for mod_info in get_mods_info_from_json() if mod_info['mod_name'] == mod_name), '')
    if singular_mod_info['packing_type'] == 'loose':
        make_loose_mod_release(singular_mod_info, base_files_directory, output_directory)
    else:
        make_archive_mod_release(singular_mod_info, base_files_directory, output_directory)
    return


def create_mod_releases(settings_json: str, mod_names: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    for mod_name in mod_names:
        create_mod_release(settings_json, mod_name, base_files_directory, output_directory)


def create_mod_releases_all(settings_json: str, base_files_directory: str, output_directory: str):
    load_settings(settings_json)
    from unreal_auto_mod.utilities import get_mods_info_from_json
    for entry in get_mods_info_from_json():
        create_mod_release(settings_json, entry['mod_name'], base_files_directory, output_directory)
