from settings import *


def test_alt_exe_entry_logic():
    add_alt_exe_entry(enums.ScriptStateType.CONSTANT, "test", enums.ExecutionMode.ASYNC, ["test", "test3"])
    set_alt_exe_path_in_alt_exe_entry("test", "test2")
    set_script_state_in_alt_exe_entry("test2", enums.ScriptStateType.PRE_ALL)
    set_execution_mode_in_alt_exe_entry("test2", enums.ExecutionMode.SYNC)
    add_arg_to_variable_list_in_alt_exe_entry("test2", "ayo")
    add_arg_to_variable_list_in_alt_exe_entry("test2", "ayo2")
    remove_args_from_variable_list_in_alt_exe_entry("test2", "ayo")


def test_mod_pak_entry_logic():
    args = ['testing', 'testing', enums.UnrealModTreeType.MODS, False, 'override', 1, enums.PackingType.REPAK,
            enums.CompressionType.ZLIB, True, ['test', 'test2'], ['test3', 'test4']]
    add_mod_pak_entry(*args)
    set_mod_name_in_mod_pak_info_entry('testing', 'testing2')
    set_pak_dir_structure_in_mod_pak_info_entry('testing2', 'yo')
    set_mod_name_dir_type_in_mod_pak_info_entry('testing2', enums.UnrealModTreeType.MODS)
    set_use_mod_name_dir_name_override_in_mod_pak_info_entry('testing2', 'overidden_name')
    set_pak_chunk_num_in_mod_pak_info_entry('testing2', 2)
    set_packing_type_in_mod_pak_info_entry('testing2', enums.PackingType.ENGINE)
    set_compression_type_in_mod_pak_info_entry('testing2', enums.CompressionType.ZLIB)
    set_is_enabled_in_mod_pak_info_entry('testing2', False)
    add_tree_paths_to_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test2')
    add_asset_paths_to_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test2')
    add_tree_paths_to_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test3')
    add_asset_paths_to_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test3')
    remove_tree_paths_from_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test2')
    remove_asset_paths_from_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test2')
    remove_tree_paths_from_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test3')
    remove_asset_paths_from_manually_specified_assets_in_mod_pak_info_entry('testing2', 'test3')


def test_process_kill_entry_logic():
    add_process_kill_entry('testing', True, enums.ScriptStateType.CONSTANT)
    set_process_name_in_process_entry('testing', 'testing2')
    set_use_substring_check_in_process_entry('testing2', False)
    set_script_state_in_process_entry('testing2', enums.ScriptStateType.POST_COOKING)


def test_window_management():
    add_window_management_entry('test', True, enums.WindowAction.MOVE, enums.ScriptStateType.CONSTANT, 0, 500, 500)
    set_window_name_in_window_management_entry('test', 'test2')
    set_window_state_in_window_management_entry('test2', enums.WindowAction.MIN)
    set_script_state_in_window_management_entry('test2', enums.ScriptStateType.CONSTANT)
    set_monitor_index_in_window_management_entry('test2', 1)
    set_use_substring_check_in_window_management_entry('test2', False)
    set_resolution_x_in_window_management_entry('test2', 600)
    set_resolution_y_in_window_management_entry('test2', 700)


def create_test_settings():
    test_alt_exe_entry_logic()
    test_mod_pak_entry_logic()
    test_process_kill_entry_logic()
    test_window_management()


def destroy_test_settings():
    remove_window_management_entry('test2')
    remove_process_kill_entry('testing2')
    remove_mod_pak_entry('testing2')
    remove_alt_exe_entry('test2')


create_test_settings()
# destroy_test_settings()
