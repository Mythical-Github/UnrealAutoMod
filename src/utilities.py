import os
import sys
import glob
import json
import psutil
import utilities
import subprocess
from msvcrt import getch
from settings import settings
from script_states import ScriptState
from enums import PackagingDirType, ExecutionMode, ScriptStateType, CompressionType, get_enum_from_val


def check_file_exists(file_path: str) -> bool:
    if os.path.exists(file_path):
        return True
    else:
        raise FileNotFoundError(f'Settings file "{file_path}" not found.')


# def check_file_exists(file_path: str) -> bool:
#     return os.path.exists(file_path)


def get_process_name(exe_path: str) -> str:
    filename = os.path.basename(exe_path)
    return filename


def get_game_process_name() -> str:
    process = settings['game_info']['game_exe_path']
    return get_process_name(process)


def kill_process(process_name: str):
    if is_process_running(process_name):
        os.system(f'taskkill /f /im {process_name}')


def is_process_running(process_name: str) -> bool:
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def get_processes_by_substring(substring: str) -> list:
    all_processes = psutil.process_iter(['pid', 'name'])
    matching_processes = [proc.info for proc in all_processes if substring.lower() in proc.info['name'].lower()]
    return matching_processes


def kill_processes(state: ScriptStateType):
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


def get_unreal_engine_version(engine_path: str) -> str:
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


def get_is_game_iostore() -> bool:
    is_game_iostore = False
    file_extensions = utilities.get_file_extensions(get_game_paks_dir())
    for file_extension in file_extensions:
        if file_extension == 'ucas':
            is_game_iostore = True
        elif file_extension == 'utoc':
            is_game_iostore = True
    return is_game_iostore


def get_game_paks_dir() -> str:
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


def get_win_dir_type() -> PackagingDirType:
    engine_dir = settings['engine_info']['unreal_engine_dir']
    ue_version = get_unreal_engine_version(engine_dir)
    if ue_version.startswith('5'):
        print('starts with 5')
        return PackagingDirType.WINDOWS
    else:
        return PackagingDirType.WINDOWS_NO_EDITOR


def is_game_ue5() -> bool:
    return get_win_dir_type() == PackagingDirType.WINDOWS


def is_game_ue4() -> bool:
    return get_win_dir_type() == PackagingDirType.WINDOWS_NO_EDITOR


def get_file_hash(file_path: str) -> str:
    import hashlib
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def get_do_files_have_same_hash(file_path_one: str, file_path_two: str) -> bool:
    hash_one = get_file_hash(file_path_one)
    hash_two = get_file_hash(file_path_two)
    return hash_one == hash_two


def get_game_window_title() -> str:
    return os.path.splitext(get_game_process_name())[0]


def get_game_engine_path() -> str:
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


def is_toggle_engine_during_testing_in_use() -> bool:
    return settings['engine_info']['toggle_engine_during_testing']


def run_app(exe_path: str, exec_mode: ExecutionMode, args: str = {}, working_dir: str = None):
    command = exe_path
    for arg in args:
        command = f'{command} {arg}'
    print(f'{command} was ran with {exec_mode} enum')
    if exec_mode == ExecutionMode.SYNC:
        subprocess.run(command, cwd=working_dir)
    elif exec_mode == ExecutionMode.ASYNC:
        subprocess.Popen(command, cwd=working_dir, start_new_session=True)
    

def get_engine_window_title() -> str:
    uproject_path = settings['engine_info']['unreal_project_file']
    proc_name_prefix = get_process_name(uproject_path)[:-9]
    proc_name_suffix = 'Unreal Editor'
    engine_proc_name = f'{proc_name_prefix} - {proc_name_suffix}'
    return engine_proc_name


def get_engine_process_name() -> str:
    exe_path = get_game_engine_path()
    return get_process_name(exe_path)


def get_files_in_tree(tree_path: str) -> list:
    return glob.glob(tree_path + '/**/*', recursive=True)


def get_file_extensions(file_path: str) -> list:
    directory, file_name = os.path.split(file_path)
    if not os.path.exists(directory):
        print(f'Error: Directory "{directory}" does not exist.')
        return []

    file_name_no_ext, _ = os.path.splitext(file_name)
    pattern = os.path.join(directory, file_name_no_ext + '*')
    matching_files = glob.glob(pattern)
    extensions = set(os.path.splitext(f)[1].lower() for f in matching_files)
    return list(extensions)


def get_game_content_dir():
    return os.path.dirname(get_game_paks_dir())


def get_game_dir():
    return os.path.dirname(get_game_content_dir())


def get_uproject_file() -> str:
    return settings['engine_info']['unreal_project_file']


def get_uproject_name() -> str:
    return os.path.splitext(os.path.basename(get_uproject_file()))[0]


def get_uproject_file_dir() -> str:
    return os.path.dirname(get_uproject_file())


def get_win_dir_str() -> str:
    win_dir_type = 'Windows'
    if is_game_ue4():
        win_dir_type = f'{win_dir_type}NoEditor'
    return win_dir_type


def get_cooked_uproject_dir() -> str:
    return f'{get_uproject_file_dir()}/Saved/Cooked/{get_win_dir_str()}/{get_uproject_name()}'


def get_mod_files(mod_name: str) -> dict:
    cooked_uproject_dir = utilities.get_cooked_uproject_dir()
    from packing import get_mod_pak_entry
    mod_pak_info = get_mod_pak_entry(mod_name)
    file_dict = {}

    for asset in mod_pak_info['manually_specified_assets']['asset_paths']:
        base_path = f'{cooked_uproject_dir}/{asset}'
        for extension in utilities.get_file_extensions(base_path):
            before_path = f'{base_path}{extension}'
            after_path = f'{utilities.get_game_dir()}/{asset}{extension}'
            file_dict[before_path] = after_path

    for tree in mod_pak_info['manually_specified_assets']['tree_paths']:
        tree_path = f'{cooked_uproject_dir}/{tree}'
        for entry in utilities.get_files_in_tree(tree_path):
            if os.path.isfile(entry):
                base_entry = os.path.splitext(entry)[0]
                for extension in utilities.get_file_extensions(entry):
                    before_path = f'{base_entry}{extension}'
                    relative_path = os.path.relpath(base_entry, cooked_uproject_dir)  # Get the relative path
                    after_path = f'{utilities.get_game_dir()}/{relative_path}{extension}'
                    file_dict[before_path] = after_path
    
    persistant_mod_dir = get_persistant_mod_dir(mod_name)

    for root, _, files in os.walk(persistant_mod_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, persistant_mod_dir)
            game_dir = utilities.get_game_dir()
            game_dir = os.path.dirname(game_dir)
            game_dir_path = os.path.join(game_dir, relative_path)
            print(f'before path: {file_path}')
            print(f'after path: {game_dir_path}')
            file_dict[file_path] = game_dir_path

    return file_dict


def get_cooked_mod_file_paths(mod_name: str) -> list:
    return list((get_mod_files(mod_name)).keys())


def get_game_mod_file_paths(mod_name: str) -> list:
    return list((get_mod_files(mod_name)).values())


def get_unreal_engine_dir() -> str:
    return settings['engine_info']['unreal_engine_dir']


def get_mod_pak_info_list() -> list:
    return settings['mod_pak_info']


def get_pak_dir_structure(mod_name: str) -> str:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return info['pak_dir_structure']
    return None


def get_mod_compression_type(mod_name: str) -> CompressionType:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            compresion_str = info['compression_type']
            return get_enum_from_val(CompressionType, compresion_str)
    return None


def get_mod_pak_info(mod_name:str) -> dict:
    for info in get_mod_pak_info_list:
        if info['mod_name'] == mod_name:
            return dict(info)
    return None


def is_mod_name_in_list(mod_name: str) -> bool:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == 'mod_name':
            return True
    return False


def get_mod_name_dir(mod_name: str) -> dir:
    if is_mod_name_in_list(mod_name):
        return f'{get_uproject_file_dir}/Saved/Cooked/Mods/{mod_name}'


def get_mod_name_dir_files(mod_name: str) -> list:
    return get_files_in_tree(get_mod_name_dir(mod_name))


def get_persistant_mod_dir(mod_name: str) -> str:
    dir = get_uproject_file_dir()
    from settings import GAME_NAME, PRESET_NAME
    prefix = f'{dir}/Plugins/Tempo/Tools/Tempo/presets/{GAME_NAME}'
    suffix = f'{PRESET_NAME}/mod_packaging/persistent_files/{mod_name}'
    return f'{prefix}/{suffix}'


def get_persistant_mod_files(mod_name: str) -> list:
    return get_files_in_tree(get_persistant_mod_dir(mod_name))
 