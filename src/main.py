import os
import sys
import json
import glob
import time
import msvcrt
import shutil
import psutil
import subprocess
import tempo_enums as enum
import tempo_windows as windows


class ScriptState():
    global SCRIPT_STATE_TYPE
    global script_state
    SCRIPT_STATE_TYPE = enum.ScriptState
    script_state = SCRIPT_STATE_TYPE.INIT
    
    
    def set_script_state(new_state):
        script_state = new_state 


def set_script_dir():
    global SCRIPT_DIR
    if getattr(sys, 'frozen', False):
        SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
    else:
        SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    os.chdir(SCRIPT_DIR)


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'Settings file "{file_path}" not found.')


def is_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def get_process_name(exe_path):
    filename = os.path.basename(exe_path)
    return filename


def get_processes_by_substring(substring):
    all_processes = psutil.process_iter(['pid', 'name'])
    matching_processes = [proc.info for proc in all_processes if substring.lower() in proc.info['name'].lower()]
    return matching_processes


def kill_process(process_name):
    if is_process_running(process_name):
        os.system(f'taskkill /f /im {process_name}')


def kill_processes():
    process_to_kill_info = settings['process_kill_info']['processes']
    for process_info in process_to_kill_info:
        if process_info['use_substring_check']:
            proc_name_substring = process_info['process_name']
            matching_processes = get_processes_by_substring(proc_name_substring)
            for proc_info in matching_processes:
                proc_name = proc_info['name']
                kill_process(proc_name)
        else:
            proc_name = process_info['process_name']
            kill_process(proc_name)


def run_app(exe_path, exec_mode, args=None, working_dir=None):
    exec_type = enum.ExecutionMode
    command = [exe_path] + args
    if exec_mode == exec_type.SYNC:
        subprocess.run(command, cwd=working_dir)
    elif exec_mode == exec_type.ASYNC:
        subprocess.run(command, cwd=working_dir)

        
def process_input_args():
    global GAME_NAME
    global PRESET_NAME
    global SCRIPT_ARG
    global mod_names

    if len(sys.argv) < 4:
        print_possible_commands()
    else:
        GAME_NAME = sys.argv[1]
        PRESET_NAME = sys.argv[2]
        SCRIPT_ARG = sys.argv[3]

    if len(sys.argv) > 4:
        mod_names = sys.argv[4:]


def print_possible_commands():
    print("""
Usage: 
TempoCLI.exe <GAME_NAME> <PRESET_NAME> <SCRIPT_ARG>
main.py <GAME_NAME> <PRESET_NAME> <SCRIPT_ARG>

Available SCRIPT_ARGs:
- test_mods_all
- test_mods
""")
    msvcrt.getch()
    
    sys.exit(1)


def process_script_args():
    SCRIPT_ARGS = {
        'test_mods_all': test_mods_all,
        'test_mods': test_mods
    }
    if not SCRIPT_ARG in SCRIPT_ARGS:
        print_possible_commands()


def test_mods_all(mod_names):
    test_mods(mod_names)


def test_mods(mod_names):
    pass


class Settings():
    global settings
    set_script_dir()
    process_input_args()
    process_script_args()
    PRESET_SETTINGS_JSON = f'{SCRIPT_DIR}/presets/{GAME_NAME}/{PRESET_NAME}/settings.json'
    check_file_exists(PRESET_SETTINGS_JSON)
    with open(PRESET_SETTINGS_JSON) as preset_settings_file:
        settings = json.load(preset_settings_file)
    windows.change_window_name(settings['general_info']['window_title'])
    auto_close_game = settings['process_kill_info']['auto_close_game']
    if auto_close_game:
        game_process_name = get_process_name(settings['game_info']['game_exe_path'])
        kill_process(game_process_name)


def get_unreal_engine_version(engine_path):
    override_automatic_version_finding = settings['engine_info']['override_automatic_version_finding']
    if override_automatic_version_finding:
        unreal_engine_major_version = settings['engine_info']['unreal_engine_major_version']
        unreal_engine_minor_version = settings['engine_info']['unreal_engine_minor_version']
        return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'
    else:
        version_file_path = os.path.join(engine_path, "Engine", "Build", "Build.version")
        check_file_exists(version_file_path)
        with open(version_file_path, "r") as f:
            version_info = json.load(f)
            unreal_engine_major_version = version_info.get("MajorVersion", 0)
            unreal_engine_minor_version = version_info.get("MinorVersion", 0)
            return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'





def routine_checks():
    pass


def run_game():
    game_launch_type = enum.GameLaunchType
    launch_type = game_launch_type(settings['game_info']['launch_type'])
    if launch_type ==   game_launch_type.EXE:
        run_game_command = settings['game_info']['game_exe_path']
        launch_params = settings['game_info']['launch_params']
        for launch_param in launch_params:
            run_game_command = f'{run_game_command} {launch_param}'
        run_app(run_game_command, enum.ExecutionMode.ASYNC)
    elif launch_type == game_launch_type.STEAM: 
        steam_app_id = settings['game_info']['game_id']
        os.system(f'start steam://rungameid/{steam_app_id}')
    # elif launch_type == game_launch_type.EPIC:
    #     pass
    # elif launch_type == game_launch_type.ITCH_IO:
    #     pass
    # elif launch_type == game_launch_type.BATTLE_NET:
    #     pass
    # elif launch_type == game_launch_type.ORIGIN:
    #     pass
    # elif launch_type == game_launch_type.UBISOFT:
    #     pass
    else:
        raise ValueError('Unsupported launch_type specified in the settings.json under game_info[launch_type]')
    

def get_file_extensions(file_path):
    directory, file_name = os.path.split(file_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return set()
    file_name_no_ext, _ = os.path.splitext(file_name)
    try:
        matching_files = [f for f in os.listdir(directory) if f.startswith(file_name_no_ext)]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return set()
    extensions = set(os.path.splitext(f)[1].lower() for f in matching_files)
    return extensions


def get_is_game_iostore():
    is_game_iostore = False
    file_extensions = get_file_extensions(get_game_paks_dir())
    for file_extension in file_extensions:
        if file_extension == "ucas":
            is_game_iostore = True
        elif file_extension == "utoc":
            is_game_iostore = True
    return is_game_iostore


def get_win_dir_type():
    win_dir_type = enum.PackagingDirType
    if get_unreal_engine_version.startswith("5"):
        return win_dir_type.WINDOWS
    else:
        return win_dir_type.WINDOWS_NO_EDITOR


def get_game_paks_dir():
    game_exe_path = settings["game_info"]["game_exe_path"]
    game_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(game_exe_path)))))
    uproject = settings["engine_info"]["unreal_project_file"]
    uproject_name = os.path.basename(uproject)[:-9]
    alt_uproject_name_in_game_dir = settings['alt_uproject_name_in_game_dir']['use_alt_method']
    if alt_uproject_name_in_game_dir == "True":
        alt_dir_name = settings['alt_uproject_name_in_game_dir']['name']
        dir = f"{game_dir}/{alt_dir_name}/Content/Paks"
    else:
        dir = f"{game_dir}/{uproject_name}/Content/Paks"
    return dir


def cook_uproject():
    output_dir = settings['generalA_info']['output_dir']
    engine_dir = settings['engine_info']['unreal_engine_dir']
    uproject = settings['engine_info']['unreal_project_file']
    os.chdir(engine_dir)
    command = f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun -project="{uproject}" -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -cook -allmaps -stage -archive -archivedirectory="{output_dir}"'
    os.system(command)
 

def package_uproject():
    output_dir = settings['generalA_info']['packing_dir']
    engine_dir = settings['engine_info']['unreal_engine_dir']
    uproject = settings['engine_info']['unreal_project_file']
    os.chdir(engine_dir)
    command = f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun -project="{uproject}" -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -cook -allmaps -stage -archive -archivedirectory={output_dir} -pak'
    os.system(command)


def main():
    run_game()
    # kill_processes()
    # if windows.does_window_exist('Tempo', True):
    #     windows_to_manage = windows.get_windows_by_title('Tempo', True)
    #     for window in windows_to_manage:
    #         print("window")
    #         windows.move_window_to_moniter(window, 1)
    #         windows.set_window_size(window, 1550, 900)


if __name__ == '__main__':
    main()
    sys.exit()
