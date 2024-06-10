import json
import enums
# from settings import SCRIPT_DIR, GAME_NAME, PRESET_NAME


# SETTINGS_JSON = f'{SCRIPT_DIR}/presets/{GAME_NAME}/{PRESET_NAME}/settings.json'

import os
import sys


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


SETTINGS_JSON = f'{SCRIPT_DIR}/presets/default/default/settings.json'


def load_settings():
    with open(SETTINGS_JSON, 'r') as file:
        return json.load(file)

def save_settings(settings):
    with open(SETTINGS_JSON, 'w') as file:
        json.dump(settings, file, indent=2)

settings = load_settings()


def set_general_info_override_default_working_dir(input: bool):
    settings["general_info"]["override_default_working_dir"] = input
    save_settings(settings)


def set_general_info_working_dir(dir: str):
    settings["general_info"]["working_dir"] = dir
    save_settings(settings)


def set_general_info_window_title(window_title: str):
    settings["general_info"]["window_title"] = window_title
    save_settings(settings)


def set_engine_info_unreal_engine_dir(dir: str):
    settings["engine_info"]["unreal_engine_dir"] = dir
    save_settings(settings)


def set_engine_info_unreal_project_file(dir: str):
    settings["engine_info"]["unreal_project_file"] = dir
    save_settings(settings)


def set_engine_info_toggle_engine_during_testing(input: bool):
    settings["engine_info"]["toggle_engine_during_testing"] = input
    save_settings(settings)


def set_engine_info_resave_packages_and_fix_up_redirectors_before_engine_open(input: bool):
    settings["engine_info"]["resave_packages_and_fix_up_redirectors_before_engine_open"] = input
    save_settings(settings)


def set_engine_info_use_unversioned_cooked_content(input: bool):
    settings["engine_info"]["use_unversioned_cooked_content"] = input
    save_settings(settings)


def set_engine_info_clear_uproject_saved_cooked_dir_before_tests(input: bool):
    settings["engine_info"]["clear_uproject_saved_cooked_dir_before_tests"] = input
    save_settings(settings)


def set_engine_info_always_build_project(input: bool):
    settings["engine_info"]["always_build_project"] = input
    save_settings(settings)


def set_engine_info_override_automatic_version_finding(input: bool):
    settings["engine_info"]["override_automatic_version_finding"] = input
    save_settings(settings)


def set_engine_info_unreal_engine_major_version(input: int):
    settings["engine_info"]["unreal_engine_major_version"] = str(input)
    save_settings(settings)


def set_engine_info_unreal_engine_minor_version(input: int):
    settings["engine_info"]["unreal_engine_minor_version"] = str(input)
    save_settings(settings)


def set_game_info_game_exe_path(dir: str):
    settings["game_info"]["game_exe_path"] = dir
    save_settings(settings)


def set_game_info_launch_type(enum: enums.GameLaunchType):
    settings["game_info"]["launch_type"] = enum.value
    save_settings(settings)


def set_game_info_override_automatic_launcher_exe_finding(input: bool):
    settings["game_info"]["override_automatic_launcher_exe_finding"] = input
    save_settings(settings)


def set_game_info_game_launcher_exe(exe_path: str):
    settings["game_info"]["game_launcher_exe"] = exe_path
    save_settings(settings)


def set_game_info_game_id(input_id: int):
    settings["game_info"]["game_id"] = input_id
    save_settings(settings)


def set_game_info_skip_launching_game(input: bool):
    settings["game_info"]["skip_launching_game"] = input
    save_settings(settings)


def set_game_info_override_automatic_window_title_finding(input: bool):
    settings["game_info"]["override_automatic_window_title_finding"] = input
    save_settings(settings)


def set_game_info_window_title_override_string(window_title: str):
    settings["game_info"]["window_title_override_string"] = window_title
    save_settings(settings)


def set_alt_uproject_name_in_game_dir_use_alt_method(input: bool):
    settings["alt_uproject_name_in_game_dir"]["use_alt_method"] = input
    save_settings(settings)


def set_alt_uproject_name_in_game_dir_name(dir_name: str):
    settings["alt_uproject_name_in_game_dir"]["name"] = dir_name
    save_settings(settings)


def set_repak_info_repak_path(dir: str):
    settings["repak_info"]["repak_path"] = dir
    save_settings(settings)


def set_repak_info_override_automatic_version_finding(input: bool):
    settings["repak_info"]["override_automatic_version_finding"] = input
    save_settings(settings)


def set_repak_info_repak_version(input: str):
    settings["repak_info"]["repak_version"] = input
    save_settings(settings)


def set_process_kill_info_auto_close_game(input: bool):
    settings["process_kill_info"]["auto_close_game"] = input
    save_settings(settings)


def add_entry_to_engine_info_launch_args(arg: str):
    settings["engine_info"]["engine_launch_args"].append(arg)
    save_settings(settings)


def remove_entry_from_engine_info_launch_args(arg: str):
    settings["engine_info"]["engine_launch_args"].remove(arg)
    save_settings(settings)


def add_entry_to_engine_info_cook_and_packaging(arg: str):
    settings["engine_info"]["engine_cook_and_packaging_args"].append(arg)
    save_settings(settings)


def remove_entry_from_engine_info_cook_and_packaging(arg: str):
    settings["engine_info"]["engine_cook_and_packaging_args"].remove(arg)
    save_settings(settings)


def add_entry_to_game_info_launch_params(arg: str):
    settings["game_info"]["launch_params"].append(arg)
    save_settings(settings)


def remove_entry_from_game_info_launch_params(arg: str):
    settings["game_info"]["launch_params"].remove(arg)
    save_settings(settings)


def set_script_state_in_alt_exe_entry(alt_exe_path: str, script_state: enums.ScriptStateType):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entry['script_state'] = script_state.value
    save_settings(settings)


def set_alt_exe_path_in_alt_exe_entry(before_exe_path: str, after_exe_path):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == before_exe_path:
            entry['alt_exe_path'] = after_exe_path
    save_settings(settings)


def set_execution_mode_in_alt_exe_entry(alt_exe_path: str, exec_mode: enums.ExecutionMode):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entry['execution_mode'] = exec_mode.value
    save_settings(settings)


def add_arg_to_variable_list_in_alt_exe_entry(alt_exe_path: str, arg: str):
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entry['variable_args'].append(arg)
    save_settings(settings)


def remove_arg_to_variable_list_in_alt_exe_entry(alt_exe_path: str, arg: str):
    entries_to_remove = []
    alt_exe_path_entries = settings["alt_exe_methods"]
    for entry in alt_exe_path_entries:
        if entry['alt_exe_path'] == alt_exe_path:
            entries_to_remove.append(entry)
    for entry in entries_to_remove:
        args_to_remove = []
        variable_args = entry['variable_args']
        for variable_arg in variable_args:
            if variable_arg == arg:
                args_to_remove.append(variable_arg)
        for arg_to_remove in args_to_remove:
            variable_args.remove(arg_to_remove)
    save_settings(settings)


def set_process_name_in_process_entry(before_process_name: str, after_process_name: str):
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == before_process_name:
            process['process_name'] = after_process_name
    save_settings(settings)


def set_use_substring_check_in_process_entry(process_name: str, use_substring_check: bool):
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == process_name:
            process['use_substring_check'] = use_substring_check
    save_settings(settings)


def set_script_state_in_process_entry(process_name: str, script_state: enums.ScriptStateType):
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == process_name:
            process['script_state'] = script_state.value
    save_settings(settings)


def set_window_name_in_window_management_entry(before_window_name: str, after_window_name: str):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == before_window_name:
            window_entry['window_name'] = after_window_name
    save_settings(settings)


def set_use_substring_check_in_window_management_entry(window_name: str, use_substring_check: bool):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['use_substring_check'] = use_substring_check
    save_settings(settings)


def set_script_state_in_window_management_entry(window_name: str, script_state: enums.ScriptStateType):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['script_state'] = script_state.value
    save_settings(settings)


def set_window_state_in_window_management_entry(window_name: str, window_state: enums.WindowAction):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['window_behaviour'] = window_state.value
    save_settings(settings)


def set_monitor_index_in_window_management_entry(window_name: str, monitor_index: int):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['monitor'] = monitor_index
    save_settings(settings)


def set_resolution_x_in_window_management_entry(window_name: str, resolution: int):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['resolution']['x'] = resolution
    save_settings(settings)


def set_resolution_y_in_window_management_entry(window_name: str, resolution: int):
    for window_entry in settings["auto_move_windows"]:
        if window_entry['window_name'] == window_name:
            window_entry['resolution']['y'] = resolution
    save_settings(settings)


def set_mod_name_in_mod_pak_info_entry(before_mod_name: str, after_mod_name: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == before_mod_name:
            info['mod_name'] = after_mod_name
    save_settings(settings)


def set_pak_dir_structure_in_mod_pak_info_entry(mod_name: str, pak_dir_structure: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['pak_dir_structure'] = pak_dir_structure
    save_settings(settings)


def set_mod_name_dir_type_in_mod_pak_info_entry(mod_name: str, mod_name_dir_type: enums.UnrealModTreeType):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['mod_name_dir_type'] = mod_name_dir_type.value
    save_settings(settings)


def set_use_mod_name_dir_name_override_in_mod_pak_info_entry(mod_name: str, input: bool):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['use_mod_name_dir_name_override'] = input
    save_settings(settings)


def set_mod_name_dir_name_override_in_mod_pak_info_entry(mod_name: str, mod_name_dir_name_override: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['mod_name_dir_name_override'] = mod_name_dir_name_override
    save_settings(settings)


def set_pak_chunk_num_in_mod_pak_info_entry(mod_name: str, pak_chunk_num: int):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['pak_chunk_num'] = pak_chunk_num
    save_settings(settings)


def set_packing_type_in_mod_pak_info_entry(mod_name: str, packing_type: enums.PackingType):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['packing_type'] = packing_type.value
    save_settings(settings)


def set_compression_type_in_mod_pak_info_entry(mod_name: str, compression_type: enums.CompressionType):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['compression_type'] = compression_type.value
    save_settings(settings)


def set_is_enabled_in_mod_pak_info_entry(mod_name: str, input: bool):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['is_enabled'] = input
    save_settings(settings)


def add_tree_path_to_manually_specified_assets_in_mod_pak_info_entry(mod_name: str, tree_path: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['manually_specified_assets']['tree_paths'].append(tree_path)
    save_settings(settings)


def remove_tree_path_to_manually_specified_assets_in_mod_pak_info_entry(mod_name: str, tree_path: str):
    if "mod_pak_info" not in settings:
        return
    for info in settings["mod_pak_info"]:
        if info.get('mod_name') == mod_name and 'manually_specified_assets' in info:
            paths = info['manually_specified_assets'].get('tree_paths', [])
            for path in paths[:]:
                if path == tree_path:
                    paths.remove(path)
    save_settings(settings)



def add_asset_path_to_manually_specified_assets_in_mod_pak_info_entry(mod_name: str, asset_path: str):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            info['manually_specified_assets']['asset_paths'].append(asset_path)
    save_settings(settings)


def remove_asset_path_to_manually_specified_assets_in_mod_pak_info_entry(mod_name: str, asset_path: str):
    if "mod_pak_info" not in settings:
        return
    for info in settings["mod_pak_info"]:
        if info.get('mod_name') == mod_name and 'manually_specified_assets' in info:
            paths = info['manually_specified_assets'].get('asset_paths', [])
            for path in paths[:]:
                if path == asset_path:
                    paths.remove(path)
    save_settings(settings)


def add_mod_pak_entry(mod_name: str, pak_dir_structure: str, mod_name_dir_type: enums.UnrealModTreeType, use_mod_name_dir_name_override: bool, mod_name_dir_name_override: str, pak_chunk_num: int, packing_type: enums.CompressionType, compression_type: enums.CompressionType, is_enabled: bool, asset_paths: list, tree_paths: list):
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
    save_settings(settings)


def add_process_kill_entry(process_name: str, use_substring_check: bool, script_state: enums.ScriptStateType):
    new_entry = {
        "process_name": process_name,
        "use_substring_check": use_substring_check,
        "script_state": script_state.value
    }
    settings["process_kill_info"]["processes"].append(new_entry)
    save_settings(settings)


def add_window_management_entry(window_name: str, use_substring_check: bool, window_behaviour: enums.WindowAction, script_state: enums.ScriptStateType, monitor_index: int, resolution_x: int, resolution_y: int):
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
    save_settings(settings)


def add_alt_exe_entry(script_state: enums.ScriptStateType, alt_exe_path: str, exec_mode: enums.ExecutionMode, args: list):
    new_entry = {
        "script_state": script_state.value,
        "alt_exe_path": alt_exe_path,
        "execution_mode": exec_mode.value,
        "variable_args": args
    }
    settings["alt_exe_methods"].append(new_entry)
    save_settings(settings)


def remove_mod_pak_entry(mod_name: str):
    entries_to_remove = []
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            entries_to_remove.append(info)
    for entry in entries_to_remove:
        settings["mod_pak_info"].remove(entry)
    save_settings(settings)


def remove_process_kill_entry(process_name: str):
    process_names_to_remove = []
    for process in settings["process_kill_info"]["processes"]:
        if process['process_name'] == process_name:
            process_names_to_remove.append(process)
    for process_name in process_names_to_remove:
        settings["process_kill_info"]["processes"].remove(process)
    save_settings(settings)


def remove_window_management_entry(window_name: str):
    entries_to_remove = []
    for entry in settings["auto_move_windows"]:
        if entry['window_name'] == window_name:
            entries_to_remove.append(entry)
    for entry in entries_to_remove:
        settings["auto_move_windows"].remove(entry)
    save_settings(settings)


def remove_alt_exe_entry(alt_exe_path: str):
    entries_to_remove = []
    for setting in settings["alt_exe_methods"]:
        setting_to_check = setting['alt_exe_path']
        if setting_to_check == alt_exe_path:
            entries_to_remove.append(setting)
    for entry in entries_to_remove:
        settings["alt_exe_methods"].remove(entry)
    save_settings(settings)


def add_mod_pak_entry(mod_name: str, pak_dir_structure: str, mod_name_dir_type: enums.UnrealModTreeType, use_mod_name_dir_name_override: bool, mod_name_dir_name_override: str, pak_chunk_num: int, packing_type: enums.PackingType, compression_type: enums.CompressionType, is_enabled: bool, asset_paths: list, tree_paths: list):
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
    save_settings(settings)
