import os
import sys
import json
import tempo_windows as windows
import tempo_utilities as utilities


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
    utilities.check_file_exists(PRESET_SETTINGS_JSON)
    with open(PRESET_SETTINGS_JSON) as preset_settings_file:
        settings = json.load(preset_settings_file)
    windows.change_window_name(settings['general_info']['window_title'])
    auto_close_game = settings['process_kill_info']['auto_close_game']
    if auto_close_game:
        game_process_name = utilities.get_process_name(settings['game_info']['game_exe_path'])
        utilities.kill_process(game_process_name)
