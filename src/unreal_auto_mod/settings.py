import os
import sys
import time
import pyjson5 as json

import psutil
import win_man_py.win_man_enums

import mods
import enums

import win_man_py
import gen_py_utils.gen_py_utils as gen_utils


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

    with open(settings_json_path, 'r') as file:
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
    import utilities
    import log_py.log_py as log
    import ue_dev_py_utils.ue_dev_py_utils as ue_dev_utils

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
    import utilities
    import log_py.log_py as log
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
    with open(settings_json, 'r') as file:
        return json.load(file)


def save_settings(settings_json: str):
    with open(settings_json, 'w') as file:
        json.dump(settings, file, indent=2)


def pass_settings(settings_json: str):
    load_settings(settings_json)


def test_mods(settings_json: str, *input_mod_names: str):
    load_settings(settings_json)
    global mod_names
    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    mods.create_mods()


def test_mods_all(settings_json: str):
    load_settings(settings_json)
    global mod_names
    for entry in settings['mod_pak_info']:
        mod_names.append(entry['mod_name'])
    mods.create_mods()


def set_general_info_override_default_working_dir(settings_json: str, input: bool):
    settings["general_info"]["override_default_working_dir"] = input
    save_settings(pass_settings(settings_json))


def set_general_info_working_dir(settings_json: str, dir: str):
    settings["general_info"]["working_dir"] = dir
    save_settings(pass_settings(settings_json))


def set_general_info_window_title(settings_json: str, window_title: str):
    settings["general_info"]["window_title"] = window_title
    save_settings(pass_settings(settings_json))


def set_engine_info_unreal_engine_dir(settings_json: str, dir: str):
    settings["engine_info"]["unreal_engine_dir"] = dir
    save_settings(pass_settings(settings_json))


def set_engine_info_unreal_project_file(settings_json: str, dir: str):
    settings["engine_info"]["unreal_project_file"] = dir
    save_settings(pass_settings(settings_json))


def set_engine_info_toggle_engine_during_testing(settings_json: str, input: bool):
    settings["engine_info"]["toggle_engine_during_testing"] = input
    save_settings(pass_settings(settings_json))


def set_engine_info_resave_packages_and_fix_up_redirectors_before_engine_open(settings_json: str, input: bool):
    settings["engine_info"]["resave_packages_and_fix_up_redirectors_before_engine_open"] = input
    save_settings(pass_settings(settings_json))


def set_engine_info_use_unversioned_cooked_content(settings_json: str, input: bool):
    settings["engine_info"]["use_unversioned_cooked_content"] = input
    save_settings(pass_settings(settings_json))


def set_engine_info_clear_uproject_saved_cooked_dir_before_tests(settings_json: str, input: bool):
    settings["engine_info"]["clear_uproject_saved_cooked_dir_before_tests"] = input
    save_settings(pass_settings(settings_json))


def set_engine_info_always_build_project(settings_json: str, input: bool):
    settings["engine_info"]["always_build_project"] = input
    save_settings(pass_settings(settings_json))


def set_engine_info_override_automatic_version_finding(settings_json: str, input: bool):
    settings["engine_info"]["override_automatic_version_finding"] = input
    save_settings(pass_settings(settings_json))


def set_engine_info_unreal_engine_major_version(settings_json: str, input: int):
    settings["engine_info"]["unreal_engine_major_version"] = str(input)
    save_settings(pass_settings(settings_json))


def set_engine_info_unreal_engine_minor_version(settings_json: str, input: int):
    settings["engine_info"]["unreal_engine_minor_version"] = str(input)
    save_settings(pass_settings(settings_json))


def set_game_info_game_exe_path(settings_json: str, dir: str):
    settings["game_info"]["game_exe_path"] = dir
    save_settings(pass_settings(settings_json))


def set_game_info_launch_type(settings_json: str, enum: enums.GameLaunchType):
    settings["game_info"]["launch_type"] = enum.value
    save_settings(pass_settings(settings_json))


def set_game_info_override_automatic_launcher_exe_finding(settings_json: str, input: bool):
    settings["game_info"]["override_automatic_launcher_exe_finding"] = input
    save_settings(pass_settings(settings_json))


def set_game_info_game_launcher_exe(settings_json: str, exe_path: str):
    settings["game_info"]["game_launcher_exe"] = exe_path
    save_settings(pass_settings(settings_json))


def set_game_info_game_id(settings_json: str, input_id: int):
    settings["game_info"]["game_id"] = input_id
    save_settings(pass_settings(settings_json))


def set_game_info_skip_launching_game(settings_json: str, input: bool):
    settings["game_info"]["skip_launching_game"] = input
    save_settings(pass_settings(settings_json))


def set_game_info_override_automatic_window_title_finding(settings_json: str, input: bool):
    settings["game_info"]["override_automatic_window_title_finding"] = input
    save_settings(pass_settings(settings_json))


def set_game_info_window_title_override_string(settings_json: str, window_title: str):
    settings["game_info"]["window_title_override_string"] = window_title
    save_settings(pass_settings(settings_json))


def set_alt_uproject_name_in_game_dir_use_alt_method(settings_json: str, input: bool):
    settings["alt_uproject_name_in_game_dir"]["use_alt_method"] = input
    save_settings(pass_settings(settings_json))


def set_alt_uproject_name_in_game_dir_name(settings_json: str, dir_name: str):
    settings["alt_uproject_name_in_game_dir"]["name"] = dir_name
    save_settings(pass_settings(settings_json))


def set_repak_info_repak_path(settings_json: str, dir: str):
    settings["repak_info"]["repak_path"] = dir
    save_settings(pass_settings(settings_json))


def set_repak_info_override_automatic_version_finding(settings_json: str, input: bool):
    settings["repak_info"]["override_automatic_version_finding"] = input
    save_settings(pass_settings(settings_json))


def set_repak_info_repak_version(settings_json: str, input: str):
    settings["repak_info"]["repak_version"] = input
    save_settings(pass_settings(settings_json))


def set_process_kill_info_auto_close_game(settings_json: str, input: bool):
    settings["process_kill_info"]["auto_close_game"] = input
    save_settings(pass_settings(settings_json))


def add_entries_to_engine_info_launch_args(settings_json: str, args: list):
    for arg in args:
        settings["engine_info"]["engine_launch_args"].append(arg)
    save_settings(pass_settings(settings_json))


def remove_entries_from_engine_info_launch_args(settings_json: str, args: list):
    for arg in args:
        settings["engine_info"]["engine_launch_args"].remove(arg)
    save_settings(pass_settings(settings_json))


def add_entries_to_engine_info_cook_and_packaging(settings_json: str, args: list):
    for arg in args:
        settings["engine_info"]["engine_cook_and_packaging_args"].append(arg)
    save_settings(pass_settings(settings_json))


def remove_entries_from_engine_info_cook_and_packaging(settings_json: str, args: list):
    for arg in args:
        settings["engine_info"]["engine_cook_and_packaging_args"].remove(arg)
    save_settings(pass_settings(settings_json))


def add_entries_to_game_info_launch_params(settings_json: str, args: list):
    for arg in args:
        settings["game_info"]["launch_params"].append(arg)
    save_settings(pass_settings(settings_json))


def remove_entries_from_game_info_launch_params(settings_json: str, args: list):
    for arg in args:
        settings["game_info"]["launch_params"].remove(arg)
    save_settings(pass_settings(settings_json))


def set_script_state_in_alt_exe_entry(settings_json: str, alt_exe_path: str, script_state: enums.ScriptStateType):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entry['script_state'] = script_state.value
    save_settings(pass_settings(settings_json))


def set_alt_exe_path_in_alt_exe_entry(settings_json: str, before_exe_path: str, after_exe_path):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == before_exe_path:
            entry['alt_exe_path'] = after_exe_path
    save_settings(pass_settings(settings_json))


def set_execution_mode_in_alt_exe_entry(settings_json: str, alt_exe_path: str, exec_mode: enums.ExecutionMode):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entry['execution_mode'] = exec_mode.value
    save_settings(pass_settings(settings_json))


def add_arg_to_variable_list_in_alt_exe_entry(settings_json: str, alt_exe_path: str, args: list):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            for arg in args:
                entry['variable_args'].append(arg)
    save_settings(pass_settings(settings_json))


def remove_args_from_variable_list_in_alt_exe_entry(settings_json: str, alt_exe_path: str, args: list):
    entries_to_remove = []
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entries_to_remove.append(entry)
    for entry in entries_to_remove:
        args_to_remove = []
        variable_args = entry['variable_args']
        for variable_arg in variable_args:
            for arg in args:
                if variable_arg == arg:
                    args_to_remove.append(variable_arg)
        for arg_to_remove in args_to_remove:
            variable_args.remove(arg_to_remove)
    save_settings(pass_settings(settings_json))


def set_process_name_in_process_entry(settings_json: str, before_process_name: str, after_process_name: str):
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == before_process_name:
            process['process_name'] = after_process_name
    save_settings(pass_settings(settings_json))


def set_use_substring_check_in_process_entry(settings_json: str, process_name: str, use_substring_check: bool):
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == process_name:
            process['use_substring_check'] = use_substring_check
    save_settings(pass_settings(settings_json))


def set_script_state_in_process_entry(settings_json: str, process_name: str, script_state: enums.ScriptStateType):
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == process_name:
            process['script_state'] = script_state.value
    save_settings(pass_settings(settings_json))


def set_window_name_in_window_management_entry(settings_json: str, before_window_name: str, after_window_name: str):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == before_window_name:
            window_entry['window_name'] = after_window_name
    save_settings(pass_settings(settings_json))


def set_use_substring_check_in_window_management_entry(settings_json: str, window_name: str, use_substring_check: bool):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['use_substring_check'] = use_substring_check
    save_settings(pass_settings(settings_json))


def set_script_state_in_window_management_entry(settings_json: str, window_name: str,
                                                script_state: enums.ScriptStateType):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['script_state'] = script_state.value
    save_settings(pass_settings(settings_json))


def set_window_state_in_window_management_entry(settings_json: str, window_name: str, window_state: win_man_py.win_man_enums.WindowAction):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['window_behaviour'] = window_state.value
    save_settings(pass_settings(settings_json))


def set_monitor_index_in_window_management_entry(settings_json: str, window_name: str, monitor_index: int):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['monitor'] = monitor_index
    save_settings(pass_settings(settings_json))


def set_resolution_x_in_window_management_entry(settings_json: str, window_name: str, resolution: int):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['resolution']['x'] = resolution
    save_settings(pass_settings(settings_json))


def set_resolution_y_in_window_management_entry(settings_json: str, window_name: str, resolution: int):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['resolution']['y'] = resolution
    save_settings(pass_settings(settings_json))


def set_mod_name_in_mod_pak_info_entry(settings_json: str, before_mod_name: str, after_mod_name: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == before_mod_name:
            info['mod_name'] = after_mod_name
    save_settings(pass_settings(settings_json))


def set_pak_dir_structure_in_mod_pak_info_entry(settings_json: str, mod_name: str, pak_dir_structure: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['pak_dir_structure'] = pak_dir_structure
    save_settings(pass_settings(settings_json))


def set_mod_name_dir_type_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                mod_name_dir_type: enums.UnrealModTreeType):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['mod_name_dir_type'] = mod_name_dir_type.value
    save_settings(pass_settings(settings_json))


def set_use_mod_name_dir_name_override_in_mod_pak_info_entry(settings_json: str, mod_name: str, input: bool):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['use_mod_name_dir_name_override'] = input
    save_settings(pass_settings(settings_json))


def set_mod_name_dir_name_override_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                         mod_name_dir_name_override: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['mod_name_dir_name_override'] = mod_name_dir_name_override
    save_settings(pass_settings(settings_json))


def set_pak_chunk_num_in_mod_pak_info_entry(settings_json: str, mod_name: str, pak_chunk_num: int):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['pak_chunk_num'] = pak_chunk_num
    save_settings(pass_settings(settings_json))


def set_packing_type_in_mod_pak_info_entry(settings_json: str, mod_name: str, packing_type: enums.PackingType):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['packing_type'] = packing_type.value
    save_settings(pass_settings(settings_json))


def set_compression_type_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                               compression_type: enums.CompressionType):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['compression_type'] = compression_type.value
    save_settings(pass_settings(settings_json))


def set_is_enabled_in_mod_pak_info_entry(settings_json: str, mod_name: str, input: bool):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['is_enabled'] = input
    save_settings(pass_settings(settings_json))


def add_tree_paths_to_manually_specified_assets_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                                      tree_paths: list):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            for tree_path in tree_paths:
                info['manually_specified_assets']['tree_paths'].append(tree_path)
    save_settings(pass_settings(settings_json))


def remove_tree_paths_from_manually_specified_assets_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                                           tree_paths: list):
    if "mod_pak_info" not in settings:
        return
    for info in settings["mod_pak_info"]:
        if info.get('mod_name') == mod_name and 'manually_specified_assets' in info:
            paths = info['manually_specified_assets'].get('tree_paths', [])
            for path in paths[:]:
                for tree_path in tree_paths:
                    if path == tree_path:
                        paths.remove(path)
    save_settings(pass_settings(settings_json))


def add_asset_paths_to_manually_specified_assets_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                                       asset_paths: list):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            for asset_path in asset_paths:
                info['manually_specified_assets']['asset_paths'].append(asset_path)
    save_settings(pass_settings(settings_json))


def remove_asset_paths_from_manually_specified_assets_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                                            asset_paths: list):
    if "mod_pak_info" not in settings:
        return
    for info in settings["mod_pak_info"]:
        if info.get('mod_name') == mod_name and 'manually_specified_assets' in info:
            paths = info['manually_specified_assets'].get('asset_paths', [])
            for path in paths[:]:
                for asset_path in asset_paths:
                    if path == asset_path:
                        paths.remove(path)
    save_settings(pass_settings(settings_json))


def add_process_kill_entry(settings_json: str, process_name: str, use_substring_check: bool,
                           script_state: enums.ScriptStateType):
    new_entry = {
        "process_name": process_name,
        "use_substring_check": use_substring_check,
        "script_state": script_state.value
    }
    settings["process_kill_info"]["processes"].append(new_entry)
    save_settings(pass_settings(settings_json))


def add_window_management_entry(settings_json: str, window_name: str, use_substring_check: bool,
                                window_behaviour: win_man_py.win_man_enums.WindowAction, script_state: enums.ScriptStateType,
                                monitor_index: int, resolution_x: int, resolution_y: int):
    new_entry = {
        "window_name": window_name,
        "use_substring_check": use_substring_check,
        "window_behaviour": window_behaviour.value,
        "script_state": script_state.value,
        "monitor": monitor_index,
        "resolution": {
            "x": resolution_x,
            "y": resolution_y
        }
    }
    settings["auto_move_windows"].append(new_entry)
    save_settings(pass_settings(settings_json))


def add_alt_exe_entry(settings_json: str, script_state: enums.ScriptStateType, alt_exe_path: str,
                      exec_mode: enums.ExecutionMode, args: list):
    new_entry = {
        "script_state": script_state.value,
        "alt_exe_path": alt_exe_path,
        "execution_mode": exec_mode.value,
        "variable_args": args
    }
    settings["alt_exe_methods"].append(new_entry)
    save_settings(pass_settings(settings_json))


def remove_mod_pak_entry(settings_json: str, mod_name: str):
    entries_to_remove = []
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            entries_to_remove.append(info)
    for entry in entries_to_remove:
        settings["mod_pak_info"].remove(entry)
    save_settings(pass_settings(settings_json))


def remove_process_kill_entry(settings_json: str, process_name: str):
    process_names_to_remove = []
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == process_name:
            process_names_to_remove.append(process)
    for process_name in process_names_to_remove:
        settings["process_kill_info"]["processes"].remove(process)
    save_settings(pass_settings(settings_json))


def remove_window_management_entry(settings_json: str, window_name: str):
    entries_to_remove = []
    for entry in settings["auto_move_windows"]:
        if entry['window_name'] == window_name:
            entries_to_remove.append(entry)
    for entry in entries_to_remove:
        settings["auto_move_windows"].remove(entry)
    save_settings(pass_settings(settings_json))


def remove_alt_exe_entry(settings_json: str, alt_exe_path: str):
    entries_to_remove = []
    for setting in settings["alt_exe_methods"]:
        setting_to_check = setting['alt_exe_path']
        if setting_to_check == alt_exe_path:
            entries_to_remove.append(setting)
    for entry in entries_to_remove:
        settings["alt_exe_methods"].remove(entry)
    save_settings(pass_settings(settings_json))


def add_mod_pak_entry(settings_json: str, mod_name: str, pak_dir_structure: str,
                      mod_name_dir_type: enums.UnrealModTreeType, use_mod_name_dir_name_override: bool,
                      mod_name_dir_name_override: str, pak_chunk_num: int, packing_type: enums.CompressionType,
                      compression_type: enums.CompressionType, is_enabled: bool, asset_paths: list, tree_paths: list):
    new_entry = {
        "mod_name": mod_name,
        "pak_dir_structure": pak_dir_structure,
        "mod_name_dir_type": mod_name_dir_type.value,
        "use_mod_name_dir_name_override": use_mod_name_dir_name_override,
        "mod_name_dir_name_override": mod_name_dir_name_override,
        "pak_chunk_num": pak_chunk_num,
        "packing_type": packing_type.value,
        "compression_type": compression_type.value,
        "is_enabled": is_enabled,
        "manually_specified_assets": {
            "tree_paths": tree_paths,
            "asset_paths": asset_paths
        }
    }
    settings["mod_pak_info"].append(new_entry)
    save_settings(pass_settings(settings_json))


# add the stuff below this to the cli json if not already in there


def open_stove(settings_json: str):
    load_settings(settings_json)
    import utilities
    if not os.path.isfile(utilities.does_stove_exist()):
        utilities.install_stove()
    utilities.run_app(utilities.get_stove_path(),)


def open_spaghetti(settings_json: str):
    load_settings(settings_json)
    import utilities
    if not os.path.isfile(utilities.get_spaghetti_path()):
        utilities.install_spaghetti()
    utilities.run_app(utilities.get_spaghetti_path())


def open_kismet_analyzer(settings_json: str):
    load_settings(settings_json)
    import utilities
    # add shell stuff to run app later or something
    if not os.path.isfile(utilities.get_kismet_analyzer_path()):
        utilities.install_kismet_analyzer()
    import subprocess
    kismet_analyzer_path = utilities.get_kismet_analyzer_path()
    kismet_directory = os.path.dirname(kismet_analyzer_path)
    command = f'cd /d "{kismet_directory}" && "{kismet_analyzer_path}" -h && set ka=kismet-analyzer.exe && cmd /k'
    subprocess.run(command, shell=True)


def open_ide(settings_json: str):
    load_settings(settings_json)
    import utilities
    utilities.run_app(utilities.get_ide_path())


def open_blender(settings_json: str):
    load_settings(settings_json)
    import utilities
    utilities.run_app(utilities.get_blender_path())


def open_uasset_gui(settings_json: str):
    load_settings(settings_json)
    import utilities
    if not os.path.isfile(utilities.get_uasset_gui_path()):
        utilities.install_uasset_gui()
    utilities.run_app(utilities.get_uasset_gui_path())


def open_latest_log(settings_json: str):
    load_settings(settings_json)
    import utilities
    file_to_open = f'{utilities.get_uproject_unreal_auto_mod_resources_dir()}/UnrealAutoMod/logs/latest.log'
    gen_utils.open_file_in_default(file_to_open)


def open_settings_json(settings_json: str):
    load_settings(settings_json)
    gen_utils.open_file_in_default(settings.settings_json)


def run_game(settings_json: str):
    load_settings(settings_json)
    import game_runner
    game_runner.run_game()


def open_downloads_dir(settings_json: str):
    load_settings(settings_json)
    downloads_dir = f"{os.path.expanduser('~')}/Downloads"
    gen_utils.open_dir_in_file_browser(downloads_dir)


def open_unreal_auto_mod_dir(settings_json: str):
    load_settings(settings_json)
    import utilities
    gen_utils.open_dir_in_file_browser(utilities.get_uproject_unreal_auto_mod_dir())


def open_game_dir(settings_json: str):
    load_settings(settings_json)
    import utilities
    gen_utils.open_dir_in_file_browser(utilities.custom_get_game_dir())


def open_game_binaries_dir(settings_json: str):
    load_settings(settings_json)
    import utilities
    gen_utils.open_dir_in_file_browser(os.path.dirname(utilities.get_game_exe_path()))


def open_game_paks_dir(settings_json: str):
    load_settings(settings_json)
    import utilities
    gen_utils.open_dir_in_file_browser(utilities.custom_get_game_paks_dir())


def open_uproject_dir(settings_json: str):
    load_settings(settings_json)
    import utilities
    gen_utils.open_dir_in_file_browser(utilities.get_uproject_dir())


def open_umodel(settings_json: str):
    load_settings(settings_json)
    import utilities
    if not os.path.isfile(utilities.does_umodel_exist()):
        utilities.install_umodel()
    # Sets dir, so it's the dir opened by default in umodel
    os.chdir(os.path.dirname(utilities.custom_get_game_dir()))
    utilities.run_app(utilities.get_umodel_path())


def open_unreal_docs_website(settings_json: str):
    load_settings(settings_json)
    gen_utils.open_website('https://dev.epicgames.com/documentation/en-us/unreal-engine/')


def open_google_website(settings_json: str):
    load_settings(settings_json)
    gen_utils.open_website('https://www.google.com/')


def open_youtube_website(settings_json: str):
    load_settings(settings_json)
    gen_utils.open_website('https://www.youtube.com/')


def open_github_website(settings_json: str):
    load_settings(settings_json)
    gen_utils.open_website('https://github.com/')


def open_persistent_mods_dir(settings_json: str):
    load_settings(settings_json)
    import utilities
    gen_utils.open_dir_in_file_browser(utilities.get_persistent_mods_dir())


def open_fmodel(settings_json: str):
    load_settings(settings_json)
    import utilities
    if not os.path.isfile(utilities.get_fmodel_path()):
        utilities.install_fmodel()
    utilities.run_app(utilities.get_fmodel_path())
