import os
import sys
import json
import psutil
import utilities


settings = ''


def set_script_dir():
    global SCRIPT_DIR
    if getattr(sys, 'frozen', False):
        SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
    else:
        SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    os.chdir(SCRIPT_DIR)


def process_input_args():
    global GAME_NAME
    global PRESET_NAME
    global SCRIPT_ARG
    global mod_names

    if len(sys.argv) < 4:
        utilities.print_possible_commands()
    else:
        GAME_NAME = sys.argv[1]
        PRESET_NAME = sys.argv[2]
        SCRIPT_ARG = sys.argv[3]

    if len(sys.argv) > 4:
        mod_names = sys.argv[4:]


def process_script_args():
    SCRIPT_ARGS = {
        'test_mods_all',
        'test_mods'
    }
    if not SCRIPT_ARG in SCRIPT_ARGS:
        utilities.print_possible_commands()


class Settings():
    global settings
    set_script_dir()
    process_input_args()
    process_script_args()
    PRESET_SETTINGS_JSON = f'{SCRIPT_DIR}/presets/{GAME_NAME}/{PRESET_NAME}/settings.json'
    if not os.path.exists(PRESET_SETTINGS_JSON):
        raise FileNotFoundError(f'Settings file "{PRESET_SETTINGS_JSON}" not found.')
    with open(PRESET_SETTINGS_JSON) as preset_settings_file:
        settings = json.load(preset_settings_file)
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
