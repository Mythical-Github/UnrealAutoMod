import os
import sys
import json
import msvcrt
import psutil


def print_possible_commands():
    print("""
Usage: 
UnrealAutoModCLI.exe <GAME_NAME> <PRESET_NAME> <SCRIPT_ARG>
__main__.py <GAME_NAME> <PRESET_NAME> <SCRIPT_ARG>

Available SCRIPT_ARGs:
- test_mods_all
- test_mods <mod_name> [<mod_name> ...]
          
""")
    msvcrt.getch()
    
    sys.exit(1)


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


if len(sys.argv) < 4:
    print_possible_commands()
else:
    GAME_NAME = sys.argv[1]
    PRESET_NAME = sys.argv[2]
    SCRIPT_ARG = sys.argv[3]
if len(sys.argv) > 4:
    mod_names = sys.argv[4:]


SCRIPT_ARGS = {
    'test_mods_all',
    'test_mods'
}
if not SCRIPT_ARG in SCRIPT_ARGS:
    print_possible_commands()


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