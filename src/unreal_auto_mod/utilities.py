from __init__ import *


from enums import ExecutionMode, ScriptStateType, CompressionType, get_enum_from_val

from log_py import log_py as log
from ue_dev_py_utils import ue_dev_py_utils as unreal_dev_utils
from gen_py_utils import gen_py_utils as general_utils

import settings

def is_script_state_used(state: ScriptStateType) -> bool:
    if isinstance(settings.settings, dict):
        if "process_kill_info" in settings.settings:
            process_kill_info = settings.settings.get("process_kill_info", {})
            if "processes" in process_kill_info:
                for process in process_kill_info["processes"]:
                    if isinstance(state, ScriptStateType):
                        state = state.value
                    if process.get("script_state") == state:
                        return True

        if "auto_move_windows" in settings.settings:
            for window in get_auto_move_windows():
                if isinstance(state, ScriptStateType):
                    state = state.value
                if window.get("script_state") == state:
                    return True

        if "alt_exe_methods" in settings.settings:
            for method in get_alt_exe_methods():
                if isinstance(state, ScriptStateType):
                    state = state.value
                if method.get("script_state") == state:
                    return True

    return False


def get_repak_version_str() -> str:
    settings.settings['repak_info']['repak_version']


def is_unreal_pak_packing_enum_in_use():
    is_in_use = False
    for entry in get_mod_info_list():
        if entry['packing_type'] == "unreal_pak":
            is_in_use = True
    return is_in_use


def get_should_ship_uproject_steps():
    return settings.settings['engine_info']['skip_uproject_steps']


def get_is_using_repak_path_override() -> bool:
    return settings.settings['repak_info']['override_default_repak_path']


def get_repak_path_override() -> str:
    return settings.settings['repak_info']['repak_path_override']


def get_game_info_launch_type_enum_str_value() -> str:
    return settings.settings['game_info']['launch_type']


def get_game_id() -> int:
    return settings.settings['game_info']['game_id']


def get_game_launcher_exe_path() -> str:
    return settings.settings['game_info']['game_launcher_exe']


def get_game_launch_params() -> list:
    return settings.settings['game_info']['launch_params']


def get_override_automatic_launcher_exe_finding() -> bool:
    return settings.settings['game_info']['override_automatic_launcher_exe_finding']


def get_auto_move_windows():
    return settings.settings["auto_move_windows"]


def get_engine_launch_args() -> list:
    return settings.settings['engine_info']['engine_launch_args']


def get_alt_exe_methods() -> list:
    return settings.settings['alt_exe_methods']


def get_is_using_unversioned_cooked_content() -> bool:
    return settings.settings['engine_info']['use_unversioned_cooked_content']


def get_mod_info_list() -> list:
    return settings.settings['mod_pak_info']


def get_game_exe_path() -> str:
    game_exe_path = settings.settings['game_info']['game_exe_path']
    general_utils.check_file_exists(game_exe_path)
    return game_exe_path


def get_is_using_alt_dir_name() -> bool:
    return settings.settings['alt_uproject_name_in_game_dir']['use_alt_method']


def get_alt_packing_dir_name() -> str:
    return settings.settings['alt_uproject_name_in_game_dir']['name']


def get_game_process_name():
    return unreal_dev_utils.get_game_process_name(get_game_exe_path())


def get_process_to_kill_info_list() -> list:
    return settings.settings['process_kill_info']['processes']


def kill_processes(state: ScriptStateType):
    current_state = state.value if isinstance(state, ScriptStateType) else state
    for process_info in get_process_to_kill_info_list():
        target_state = process_info.get('script_state')
        if target_state == current_state:
            if process_info['use_substring_check']:
                proc_name_substring = process_info['process_name']
                for proc_info in general_utils.get_processes_by_substring(proc_name_substring):
                    proc_name = proc_info['name']
                    general_utils.kill_process(proc_name)
            else:
                proc_name = process_info['process_name']
                general_utils.kill_process(proc_name)


def get_override_automatic_version_finding() -> bool:
    return settings.settings['engine_info']['override_automatic_version_finding']


def custom_get_unreal_engine_version(engine_path: str) -> str:
    if get_override_automatic_version_finding():
        unreal_engine_major_version = settings.settings['engine_info']['unreal_engine_major_version']
        unreal_engine_minor_version = settings.settings['engine_info']['unreal_engine_minor_version']
        return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'
    else:
        return unreal_dev_utils.get_unreal_engine_version(engine_path)
    

def custom_get_game_dir():
    return unreal_dev_utils.get_game_dir(get_game_exe_path())


def custom_get_game_paks_dir() -> str:
    alt_game_dir = os.path.dirname(custom_get_game_dir())
    if get_is_using_alt_dir_name():
        return f'{alt_game_dir}/{get_alt_packing_dir_name()}/Content/Paks'
    else:
        if not get_should_ship_uproject_steps():
            return unreal_dev_utils.get_game_paks_dir(get_uproject_file(), custom_get_game_dir())
        else:
            return f'{os.path.dirname(os.path.dirname(os.path.dirname(get_game_exe_path())))}/Content/Paks'


def get_unreal_engine_dir() -> str:
    ue_dir = settings.settings['engine_info']['unreal_engine_dir']
    general_utils.check_file_exists(ue_dir)
    return ue_dir


def is_toggle_engine_during_testing_in_use() -> bool:
    return settings.settings['engine_info']['toggle_engine_during_testing']


def get_uproject_file() -> str:
    uproject_file = settings.settings['engine_info']['unreal_project_file']
    return uproject_file


def get_use_mod_name_dir_name_override(mod_name: str) -> bool:
    return get_mod_pak_info(mod_name)['use_mod_name_dir_name_override']


def get_mod_name_dir_name_override(mod_name: str) -> bool:
    return get_mod_pak_info(mod_name)['mod_name_dir_name_override']


def get_mod_name_dir_name(mod_name: str) -> str:
    if get_use_mod_name_dir_name_override(mod_name):
        return get_mod_name_dir_name_override(mod_name)
    else:
        return mod_name


def get_mod_pak_info_list() -> list:
    return settings.settings['mod_pak_info']


def get_pak_dir_structure(mod_name: str) -> str:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return info['pak_dir_structure']
    return None


def get_mod_compression_type(mod_name: str) -> CompressionType:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            compression_str = info['compression_type']
            return get_enum_from_val(CompressionType, compression_str)
    return None


def get_unreal_mod_tree_type_str(mod_name: str) -> str:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return info['mod_name_dir_type']
    return None


def get_mod_pak_info(mod_name: str) -> dict:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return dict(info)
    return None


def is_mod_name_in_list(mod_name: str) -> bool:
    for info in get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return True
    return False


def get_mod_name_dir(mod_name: str) -> dir:
    if is_mod_name_in_list(mod_name):
        return f'{unreal_dev_utils.get_uproject_dir(get_uproject_file())}/Saved/Cooked/{get_unreal_mod_tree_type_str(mod_name)}/{mod_name}'
    return None


def get_mod_name_dir_files(mod_name: str) -> list:
    return general_utils.get_files_in_tree(get_mod_name_dir(mod_name))


def get_persistant_mod_dir(mod_name: str) -> str:
    return f'{settings.settings_json_dir}/mod_packaging/persistent_files/{mod_name}'


def get_persistant_mod_files(mod_name: str) -> list:
    return general_utils.get_files_in_tree(get_persistant_mod_dir(mod_name))


def get_fix_up_redirectors_before_engine_open() -> bool:
    return settings.settings['engine_info']['resave_packages_and_fix_up_redirectors_before_engine_open']


def get_is_overriding_default_working_dir() -> bool:
    return settings.settings['general_info']['override_default_working_dir']


def get_override_working_dir() -> str:
    return settings.settings['general_info']['working_dir']


def get_working_dir() -> str:
    if get_is_overriding_default_working_dir():
        working_dir = get_override_working_dir()
    else:
        working_dir = f'{settings.SCRIPT_DIR}/working_dir'
    if not os.path.isdir(working_dir):
        os.makedirs(working_dir)
    return working_dir


def clean_working_dir():
    working_dir = get_working_dir()
    if os.path.isdir(working_dir):
        try:
            shutil.rmtree(working_dir)
        except Exception as e:
            log.log_message(f"Error: {e}")


def get_clear_uproject_saved_cooked_dir_before_tests() -> bool:
    return settings.settings['engine_info']['clear_uproject_saved_cooked_dir_before_tests']


def get_skip_launching_game() -> bool:
    return settings.settings['game_info']['skip_launching_game']


def get_auto_move_windows() -> dict:
    return settings.settings['auto_move_windows']


def get_always_build_project() -> str:
    return settings.settings['engine_info']['always_build_project']


def get_engine_cook_and_packaging_args() -> list:
    return settings.settings['engine_info']['engine_cook_and_packaging_args']


def get_is_overriding_automatic_version_finding() -> bool:
    return settings.settings['repak_info']['override_automatic_version_finding']


def get_override_automatic_window_title_finding() -> bool:
    return settings.settings['game_info']['override_automatic_window_title_finding']


def get_window_title_override_string() -> str:
    return settings.settings['game_info']['window_title_override_string']


def filter_file_paths(paths_dict: dict) -> dict:
    filtered_dict = {}
    path_dict_keys = paths_dict.keys()
    for path_dict_key in path_dict_keys:
        if os.path.isfile(path_dict_key):
            filtered_dict[path_dict_key] = paths_dict[path_dict_key]
    return filtered_dict


def get_game_window_title() -> str:
    if get_override_automatic_window_title_finding():
        return get_window_title_override_string()
    else:
        unreal_dev_utils.get_game_process_name(get_game_exe_path())


def run_app(exe_path: str, exec_mode: ExecutionMode = ExecutionMode.SYNC, args: list = [], working_dir: str = None):
    if exec_mode == ExecutionMode.SYNC:
        command = exe_path
        if working_dir:
            command = f'"{working_dir}/{command}"'
        for arg in args:
            command = f'{command} {arg}'
        log.log_message(f'Command: {command} running with the {exec_mode} enum')
        if working_dir:
            if os.path.isdir(working_dir):
                os.chdir(working_dir)

        process = subprocess.Popen(command, cwd=working_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
        
        for line in iter(process.stdout.readline, ''):
            log.log_message(line.strip())

        process.stdout.close()
        process.wait()
        log.log_message(f'Command: {command} finished')

    elif exec_mode == ExecutionMode.ASYNC:
        command = exe_path
        command = f'"{command}"'
        for arg in args:
            command = f'{command} {arg}'
        log.log_message(f'Command: {command} started with the {exec_mode} enum')
        subprocess.Popen(command, cwd=working_dir, start_new_session=True, shell=True)


def get_running_time():
    return time.time() - settings.start_time
