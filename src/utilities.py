import os
import sys
import json
import psutil
import hashlib
import utilities
import subprocess
from msvcrt import getch
from tempo_settings import settings
from script_states import ScriptState
from enums import PackagingDirType, ExecutionMode, ScriptStateType


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'Settings file "{file_path}" not found.')


def get_process_name(exe_path):
    filename = os.path.basename(exe_path)
    return filename


def get_game_process_name():
    process = settings['game_info']['game_exe_path']
    return get_process_name(process)


def kill_process(process_name):
    if is_process_running(process_name):
        os.system(f'taskkill /f /im {process_name}')


def is_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def get_processes_by_substring(substring):
    all_processes = psutil.process_iter(['pid', 'name'])
    matching_processes = [proc.info for proc in all_processes if substring.lower() in proc.info['name'].lower()]
    return matching_processes


def kill_processes(state):
    process_to_kill_info = settings['process_kill_info']['processes']
    current_state = state.value if isinstance(state, ScriptStateType) else state

    for process_info in process_to_kill_info:
        target_state = process_info.get('script_state')
        if target_state == current_state:
            if process_info['use_substring_check']:
                proc_name_substring = process_info['process_name']
                matching_processes = utilities.get_processes_by_substring(proc_name_substring)
                for proc_info in matching_processes:
                    proc_name = proc_info['name']
                    utilities.kill_process(proc_name)
            else:
                proc_name = process_info['process_name']
                utilities.kill_process(proc_name)


def get_file_extensions(file_path):
    directory, file_name = os.path.split(file_path)
    if not os.path.exists(directory):
        print(f'Error: Directory "{directory}" does not exist.')
        return set()
    file_name_no_ext, _ = os.path.splitext(file_name)
    try:
        matching_files = [f for f in os.listdir(directory) if f.startswith(file_name_no_ext)]
    except FileNotFoundError:
        print(f'Error: Directory "{directory}" not found.')
        return set()
    extensions = set(os.path.splitext(f)[1].lower() for f in matching_files)
    return extensions


def print_possible_commands():
    print("""
Usage: 
TempoCLI.exe <GAME_NAME> <PRESET_NAME> <SCRIPT_ARG>
main.py <GAME_NAME> <PRESET_NAME> <SCRIPT_ARG>

Available SCRIPT_ARGs:
- test_mods_all
- test_mods
""")
    getch()
    
    sys.exit(1)


def get_unreal_engine_version(engine_path):
    override_automatic_version_finding = settings['engine_info']['override_automatic_version_finding']
    if override_automatic_version_finding:
        unreal_engine_major_version = settings['engine_info']['unreal_engine_major_version']
        unreal_engine_minor_version = settings['engine_info']['unreal_engine_minor_version']
        return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'
    else:
        version_file_path = os.path.join(engine_path, 'Engine', 'Build', 'Build.version')
        utilities.check_file_exists(version_file_path)
        with open(version_file_path, 'r') as f:
            version_info = json.load(f)
            unreal_engine_major_version = version_info.get('MajorVersion', 0)
            unreal_engine_minor_version = version_info.get('MinorVersion', 0)
            return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'


def get_is_game_iostore():
    is_game_iostore = False
    file_extensions = utilities.get_file_extensions(get_game_paks_dir())
    for file_extension in file_extensions:
        if file_extension == 'ucas':
            is_game_iostore = True
        elif file_extension == 'utoc':
            is_game_iostore = True
    return is_game_iostore


def get_game_paks_dir():
    game_exe_path = settings['game_info']['game_exe_path']
    game_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(game_exe_path)))))
    uproject = settings['engine_info']['unreal_project_file']
    uproject_name = os.path.basename(uproject)[:-9]
    if settings['alt_uproject_name_in_game_dir']['use_alt_method']:
        alt_dir_name = settings['alt_uproject_name_in_game_dir']['name']
        dir = f'{game_dir}/{alt_dir_name}/Content/Paks'
    else:
        dir = f'{game_dir}/{uproject_name}/Content/Paks'
    return dir


def get_win_dir_type():
    engine_dir = settings['engine_info']['unreal_engine_dir']
    ue_version = get_unreal_engine_version(engine_dir)
    if ue_version.startswith('5'):
        print('starts with 5')
        return PackagingDirType.WINDOWS
    else:
        return PackagingDirType.WINDOWS_NO_EDITOR


def is_game_ue5():
    return get_win_dir_type() == PackagingDirType.WINDOWS


def is_game_ue4():
    return get_win_dir_type() == PackagingDirType.WINDOWS_NO_EDITOR


def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def get_do_files_have_same_hash(file_path_one, file_path_two):
    hash_one = get_file_hash(file_path_one)
    hash_two = get_file_hash(file_path_two)
    return hash_one == hash_two


def get_game_window_title():
    return os.path.splitext(get_game_process_name())[0]


def get_game_engine_path():
    engine_dir = settings['engine_info']['unreal_engine_dir']
    test = get_win_dir_type()
    if test == PackagingDirType.WINDOWS_NO_EDITOR:
        engine_path_suffix = '/Engine/Binaries/Win64/UE4Editor.exe'
    else:
        engine_path_suffix = '/Engine/Binaries/Win64/UnrealEditor.exe'
    engine_exe = f'{engine_dir}{engine_path_suffix}'
    return engine_exe


def open_game_engine():
    ScriptState.set_script_state(ScriptStateType.PRE_ENGINE_OPEN)
    command = get_game_engine_path()
    args = settings['engine_info']['engine_launch_args']
    run_app(command, ExecutionMode.ASYNC, args)
    ScriptState.set_script_state(ScriptStateType.POST_ENGINE_OPEN)


def close_game_engine():
    ScriptState.set_script_state(ScriptStateType.PRE_ENGINE_CLOSE)
    if get_win_dir_type() == PackagingDirType.WINDOWS_NO_EDITOR:
        game_engine_processes = get_processes_by_substring('UE4Editor')
    else:
        game_engine_processes = get_processes_by_substring('UnrealEditor')
    for process_info in game_engine_processes:
        kill_process(process_info['name'])
    ScriptState.set_script_state(ScriptStateType.POST_ENGINE_CLOSE)


def is_toggle_engine_during_testing_in_use():
    return settings['engine_info']['toggle_engine_during_testing']


def run_app(exe_path, exec_mode, args={}, working_dir=None):
    command = exe_path
    for arg in args:
        command = f'{command} {arg}'
    print(command)
    if exec_mode == ExecutionMode.SYNC:
        subprocess.run(command, cwd=working_dir)
    elif exec_mode == ExecutionMode.ASYNC:
        subprocess.Popen(command, cwd=working_dir, start_new_session=True)


def get_engine_window_title():
    uproject_path = settings['engine_info']['unreal_project_file']
    proc_name_prefix = get_process_name(uproject_path)[:-9]
    proc_name_suffix = 'Unreal Editor'
    engine_proc_name = f'{proc_name_prefix} - {proc_name_suffix}'
    return engine_proc_name


def get_engine_process_name():
    exe_path = get_game_engine_path()
    return get_process_name(exe_path)
