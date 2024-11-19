import os
import sys
import time

import psutil
import pyjson5 as json

from unreal_auto_mod.log_py import log_message
import unreal_auto_mod.gen_py_utils as gen_utils
from unreal_auto_mod import mods

start_time = time.time()

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
    os.system(f'title {window_name}')
    auto_close_game = settings['process_kill_info']['auto_close_game']
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
            os.system(f'taskkill /f /im {process_name}')
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
            script_states,
            thread_constant
        )
    script_states.ScriptState.set_script_state(enums.ScriptStateType.INIT)
    thread_constant.constant_thread()
    script_states.ScriptState.set_script_state(enums.ScriptStateType.POST_INIT)


def close_thread_system():
    from unreal_auto_mod import thread_constant
    thread_constant.stop_constant_thread()


# all things below this should be functions that correspond to cli logic


def test_mods(settings_json: str, input_mod_names: str):
    init_thread_system()
    load_settings(settings_json)
    global mod_names
    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    mods.create_mods()
    close_thread_system()


def test_mods_all(settings_json: str):
    init_thread_system()
    load_settings(settings_json)
    global mod_names
    for entry in settings['mod_pak_info']:
        mod_names.append(entry['mod_name'])
    mods.create_mods()
    close_thread_system()


def install_stove(output_directory: str):
    init_thread_system()
    from unreal_auto_mod import utilities
    if not utilities.does_stove_exist(output_directory):
        utilities.install_stove(output_directory)
    utilities.run_app(utilities.get_stove_path(output_directory))
    close_thread_system()


def install_spaghetti(output_directory: str):
    init_thread_system()
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_spaghetti_path(output_directory)):
        utilities.install_spaghetti(output_directory)
    utilities.run_app(utilities.get_spaghetti_path(output_directory))
    close_thread_system()


def install_kismet_analyzer(output_directory: str):
    init_thread_system()
    from unreal_auto_mod import utilities
    # add shell stuff to run app later or something
    if not os.path.isfile(utilities.get_kismet_analyzer_path(output_directory)):
        utilities.install_kismet_analyzer(output_directory)
    import subprocess
    kismet_analyzer_path = utilities.get_kismet_analyzer_path(output_directory)
    kismet_directory = os.path.dirname(kismet_analyzer_path)
    command = f'cd /d "{kismet_directory}" && "{kismet_analyzer_path}" -h && set ka=kismet-analyzer.exe && cmd /k'
    subprocess.run(command, shell=True, check=False)
    close_thread_system()


def install_uasset_gui(output_directory: str):
    init_thread_system()
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_uasset_gui_path(output_directory)):
        utilities.install_uasset_gui(output_directory)
    utilities.run_app(utilities.get_uasset_gui_path(output_directory))
    close_thread_system()


def open_latest_log(settings_json: str):
    init_thread_system()
    load_settings(settings_json)
    from unreal_auto_mod import utilities
    file_to_open = f'{utilities.get_uproject_unreal_auto_mod_resources_dir()}/UnrealAutoMod/logs/latest.log'
    gen_utils.open_file_in_default(file_to_open)
    close_thread_system()


def run_game(settings_json: str):
    init_thread_system()
    load_settings(settings_json)
    from unreal_auto_mod import game_runner, thread_game_monitor
    game_runner.run_game()
    thread_game_monitor.game_monitor_thread()
    close_thread_system()


def install_umodel(output_directory: str):
    init_thread_system()
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.does_umodel_exist(output_directory)):
        utilities.install_umodel(output_directory)
    # Sets dir, so it's the dir opened by default in umodel
    # os.chdir(os.path.dirname(utilities.custom_get_game_dir()))
    utilities.run_app(utilities.get_umodel_path(output_directory))
    close_thread_system()


def install_fmodel(output_directory: str):
    init_thread_system()
    from unreal_auto_mod import utilities
    if not os.path.isfile(utilities.get_fmodel_path(output_directory)):
        utilities.install_fmodel(output_directory)
    utilities.run_app(utilities.get_fmodel_path(output_directory))
    close_thread_system()


def cleanup(settings_json: str):
    init_thread_system()
    from unreal_auto_mod.enums import ExecutionMode
    from unreal_auto_mod.utilities import run_app, get_repo_paths
    load_settings(settings_json)
    for repo_path in get_repo_paths():
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
    close_thread_system()


def build(settings_json: str):
    load_settings(settings_json)
    init_thread_system()
    log_message('place_holder function called')
    close_thread_system()


def upload_changes_to_repo(settings_json: str):
    load_settings(settings_json)
    init_thread_system()
    log_message('place_holder function called')
    close_thread_system()


def create_mods(settings_json: str, mod_names: str):
    load_settings(settings_json)
    init_thread_system()
    log_message('place_holder function called')
    close_thread_system()


def create_mods_all(settings_json: str):
    load_settings(settings_json)
    init_thread_system()
    log_message('place_holder function called')
    close_thread_system()


def create_mod_releases(settings_json: str, mod_names: str):
    load_settings(settings_json)
    init_thread_system()
    log_message('place_holder function called')
    close_thread_system()


def create_mod_releases_all(settings_json: str):
    load_settings(settings_json)
    init_thread_system()
    log_message('place_holder function called')
    close_thread_system()


def cook(settings_json: str):
    init_thread_system()
    log_message('place_holder function called')
    log_message('Content Cook Starting')
    load_settings(settings_json)
    from unreal_auto_mod.packing import cooking
    cooking()
    log_message('Content Cook Complete')
    close_thread_system()


# def open_settings_json(settings_json: str):
#     load_settings(settings_json)
#     gen_utils.open_file_in_default(settings.settings_json)
