import argparse
import sys

import settings


class CustomArgumentParser(argparse.ArgumentParser):
    def format_help(self):
        formatter = self._get_formatter()
        formatter.add_text(self.description)
        positionals = [action for action in self._actions if action.option_strings == []]
        if positionals:
            formatter.start_section('positional arguments')
            formatter.add_arguments(positionals)
            formatter.end_section()
        formatter.add_text(self.epilog)

        return formatter.format_help()

    def print_help(self, file=None):
        print(self.format_help(), file=file)


def cli_logic():
    parser = CustomArgumentParser()

    unreal_auto_mod_parser = parser.add_subparsers(dest='unreal_auto_mod_parser')

    add_entry_to_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='add_entry_to_alt_exe_info')
    add_entry_to_alt_exe_entry_parser.add_argument('alt_exe_path', help='Path to the executable')
    add_entry_to_alt_exe_entry_parser.add_argument('script_state',
                                                   help='Corresponding Str value from the ScriptStateType enum')
    add_entry_to_alt_exe_entry_parser.add_argument('execution_mode',
                                                   help='Corresponding Str value from the ExecutionMode enum')
    add_entry_to_alt_exe_entry_parser.add_argument('variable_args', nargs='+',
                                                   help='List of one or more Str args to pass to the exe when launched')

    remove_entry_from_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='remove_entry_from_alt_exe_info')
    remove_entry_from_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')

    set_script_state_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='set_script_state_in_alt_exe_entry')
    set_script_state_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')
    set_script_state_in_alt_exe_entry_parser.add_argument('script_state', help='ScriptStateType enum str value')

    set_alt_exe_path_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='set_alt_exe_path_in_alt_exe_entry')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')

    set_exec_mode_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='set_execution_mode_in_alt_exe_entry')
    set_exec_mode_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')
    set_exec_mode_in_alt_exe_entry_parser.add_argument('execution_mode', help='ExecutionMode enum str value')

    add_args_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='add_args_to_alt_exe_entry')
    add_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')
    add_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')

    remove_args_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name='remove_args_from_alt_exe_entry')
    remove_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')
    remove_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')


    override_working_dir_parser = unreal_auto_mod_parser.add_parser(name='set_override_working_dir')
    override_working_dir_parser.add_argument('override_value', help='true/false string value')


    working_dir_parser = unreal_auto_mod_parser.add_parser(name='set_working_dir')
    working_dir_parser.add_argument('working_dir', help='Path to working_dir')

 
    window_title_parser = unreal_auto_mod_parser.add_parser(name='set_window_title')
    window_title_parser.add_argument('window_title', help='window title Str')

    use_alt_method_in_alt_uproject_parser = unreal_auto_mod_parser.add_parser(name='set_use_alt_uproject_name')
    use_alt_method_in_alt_uproject_parser.add_argument('override_value', help='true/false string value')

    alt_method_alt_uproject_name_parser = unreal_auto_mod_parser.add_parser(name='set_alt_uproject_name')
    alt_method_alt_uproject_name_parser.add_argument('alt_project_name', help='uproject name Str')

    repak_path_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name='set_repak_path')
    repak_path_in_repak_info_parser.add_argument('repak_path', help='Path to repak exe')

    override_automatic_version_finding_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name='set_override_automatic_repak_version_finding')
    override_automatic_version_finding_in_repak_info_parser.add_argument('override_value',
                                                                         help='true/false string value')

    repak_version_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name='set_repak_version')
    repak_version_in_repak_info_parser.add_argument('repak_version', help='repak version in Str')

    engine_info_unreal_engine_dir_parser = unreal_auto_mod_parser.add_parser(name='set_unreal_engine_dir')
    engine_info_unreal_engine_dir_parser.add_argument('unreal_engine_dir', help='Path to unreal engine directory')

    engine_info_unreal_engine_project_parser = unreal_auto_mod_parser.add_parser(name='set_unreal_project_path')
    engine_info_unreal_engine_project_parser.add_argument('unreal_engine_uproject',
                                                          help='Path to unreal engine uproject file')

    toggle_engine_parser = unreal_auto_mod_parser.add_parser(name='set_toggle_engine_during_testing')
    toggle_engine_parser.add_argument('override_value', help='true/false string value')

    toggle_engine_parser = unreal_auto_mod_parser.add_parser(name='set_resave_packages_and_fix_up_redirectors_before_engine_open')
    toggle_engine_parser.add_argument('override_value', help='true/false string value')

    add_engine_args_parser = unreal_auto_mod_parser.add_parser(name='add_engine_launch_args')
    add_engine_args_parser.add_argument('engine_args', help='one or more string args')

    add_engine_args_parser = unreal_auto_mod_parser.add_parser(name='remove_engine_launch_args')
    add_engine_args_parser.add_argument('engine_args', help='one or more string args')

    cook_and_packaging_parser = unreal_auto_mod_parser.add_parser(name='add_cook_and_packaging_args')
    cook_and_packaging_parser.add_argument('cook_and_packaging_args', help='one or more string args')

    cook_and_packaging_args_parser = unreal_auto_mod_parser.add_parser(name='remove_cook_and_packaging_args')
    cook_and_packaging_args_parser.add_argument('cook_and_packaging_args', help='one or more string args')

    use_unversioned_cooked_content_parser = unreal_auto_mod_parser.add_parser(name='set_use_unversioned_cooked_content')
    use_unversioned_cooked_content_parser.add_argument('override_value', help='true/false string value')

    clear_uproject_saved_cooked_dir_before_tests_parser = unreal_auto_mod_parser.add_parser(name='set_clear_uproject_saved_cooked_dir_before_tests')
    clear_uproject_saved_cooked_dir_before_tests_parser.add_argument('override_value', help='true/false string value')

    always_build_project_parser = unreal_auto_mod_parser.add_parser(name='set_always_build_project')
    always_build_project_parser.add_argument('override_value', help='true/false string value')

    override_automatic_version_finding_parser = unreal_auto_mod_parser.add_parser(name='set_override_automatic_engine_version_finding')
    override_automatic_version_finding_parser.add_argument('override_value', help='true/false string value')

    unreal_engine_major_version_parser = unreal_auto_mod_parser.add_parser(name='set_unreal_engine_major_version')
    unreal_engine_major_version_parser.add_argument('ue_maj_ver', help='UE major version int')

    unreal_engine_minor_version_parser = unreal_auto_mod_parser.add_parser(name='set_unreal_engine_minor_version')
    unreal_engine_minor_version_parser.add_argument('ue_min_ver', help='UE minor version int')

    game_path_parser = unreal_auto_mod_parser.add_parser(name='set_game_path')
    game_path_parser.add_argument('game_path', help="Path to the game's win64_exe, or equivalent")

    game_launch_type_parser = unreal_auto_mod_parser.add_parser(name='set_game_launch_type')
    game_launch_type_parser.add_argument('game_launch_type', help='Corresponding Str value from game launch type enum')

    override_automatic_launcher_parser = unreal_auto_mod_parser.add_parser(name='set_override_automatic_launcher_finding')
    override_automatic_launcher_parser.add_argument('override_value', help='true/false string value')

    game_launcher_path_parser = unreal_auto_mod_parser.add_parser(name='set_game_launcher_path')
    game_launcher_path_parser.add_argument('game_launcher_path', help='Path to the game launcher exe')

    game_id_parser = unreal_auto_mod_parser.add_parser(name='set_game_id')
    game_id_parser.add_argument('game_id', help='game id of the game for the launcher, Str')

    skip_launching_game_parser = unreal_auto_mod_parser.add_parser(name='set_skip_game_launch')
    skip_launching_game_parser.add_argument('override_value', help='true/false string value')

    override_automatic_window_title_finding_parser = unreal_auto_mod_parser.add_parser(name='set_override_automatic_window_title_finding')
    override_automatic_window_title_finding_parser.add_argument('override_value', help='true/false string value')

    window_title_override_string_parser = unreal_auto_mod_parser.add_parser(name='set_window_title_override_string')
    window_title_override_string_parser.add_argument('window_title_override_string',
                                                     help='window title Str to be used by the override')

    add_params_to_game_launch_params_parser = unreal_auto_mod_parser.add_parser(name='add_params_to_game_launch_params')
    add_params_to_game_launch_params_parser.add_argument('launch_params',
                                                         help='list of Str to add to game launch param list')

    remove_params_from_game_launch_params_parser = unreal_auto_mod_parser.add_parser(name='remove_params_from_game_launch_params')
    remove_params_from_game_launch_params_parser.add_argument('launch_params',
                                                              help='list of Str to remove from game launch param list')

    auto_close_game_parser = unreal_auto_mod_parser.add_parser(name='set_auto_close_game')
    auto_close_game_parser.add_argument('override_value', help='true/false string value')

    add_pki_entry_parser = unreal_auto_mod_parser.add_parser(name='add_entry_to_process_info')
    add_pki_entry_parser.add_argument('process_name', help='process name in Str')
    add_pki_entry_parser.add_argument('use_substring_check', help='true/false string value')
    add_pki_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')

    remove_pki_entry_parser = unreal_auto_mod_parser.add_parser(name='remove_entry_from_process_info')
    remove_pki_entry_parser.add_argument('process_name', help='process name in Str')

    process_name_parser = unreal_auto_mod_parser.add_parser(name='set_process_name_in_process_info_entry')
    process_name_parser.add_argument('process_name', help='process name in Str')

    pki_use_substring_check_parser = unreal_auto_mod_parser.add_parser(name='set_use_substring_check_in_process_info_entry')
    pki_use_substring_check_parser.add_argument('process_name', help='process name in Str')
    pki_use_substring_check_parser.add_argument('use_substring_check', help='true/false string value')
 
    pki_script_state_parser = unreal_auto_mod_parser.add_parser(name='set_script_state_in_process_info_entry')
    pki_script_state_parser.add_argument('process_name', help='process name in Str')
    pki_script_state_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')

    awm_add_entry_parser = unreal_auto_mod_parser.add_parser(name='add_entry_to_window_management')
    awm_add_entry_parser.add_argument('window_name', help='Window name Str')
    awm_add_entry_parser.add_argument('use_substring_check', help='true/false string value')
    awm_add_entry_parser.add_argument('window_behaviour', help='Corresponding Str value from the WindowAction enum')
    awm_add_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')
    awm_add_entry_parser.add_argument('monitor_index', help='monitor index Int')
    awm_add_entry_parser.add_argument('resolution_x', help='x resolution Int')
    awm_add_entry_parser.add_argument('resolution_y', help='y resolution Int')

    amw_re_parser = unreal_auto_mod_parser.add_parser(name='remove_entry_from_window_management')
    amw_re_parser.add_argument('window_name', help='Window name Str')

    amw_wn_parser = unreal_auto_mod_parser.add_parser(name='set_window_name_in_window_management_entry')
    amw_wn_parser.add_argument('window_name', help='Window name Str')

    amw_uss_parser = unreal_auto_mod_parser.add_parser(name='set_use_substring_check_in_window_management_entry')
    amw_wn_parser.add_argument('window_name', help='Window name Str')
    amw_uss_parser.add_argument('use_substring_check', help='true/false string value')

    amw_wb_parser = unreal_auto_mod_parser.add_parser('set_window_behaviour_in_window_management_entry')
    amw_wn_parser.add_argument('window_name', help='Window name Str')
    amw_wb_parser.add_argument('window_behaviour', help='Corresponding Str value from the WindowAction enum')

    amw_ss_parser = unreal_auto_mod_parser.add_parser(name='set_script_state_in_window_management_entry')
    amw_ss_parser.add_argument('window_name', help='Window name Str')
    amw_ss_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')

    amw_mi_parser = unreal_auto_mod_parser.add_parser(name='set_monitor_index_in_window_management_entry')
    amw_mi_parser.add_argument('window_name', help='Window name Str')
    amw_mi_parser.add_argument('monitor_index', help='monitor index Int')

    amw_srx_parser = unreal_auto_mod_parser.add_parser(name='set_resolution_x_in_window_management_entry')
    amw_srx_parser.add_argument('window_name', help='Window name Str')
    amw_srx_parser.add_argument('resolution_x', help='x resolution Int')

    amw_sry_parser = unreal_auto_mod_parser.add_parser(name='set_resolution_y_in_window_management_entry')
    amw_sry_parser.add_argument('window_name', help='Window name Str')
    amw_sry_parser.add_argument('resolution_y', help='y resolution Int')

    mod_info_ae_parser = unreal_auto_mod_parser.add_parser(name='add_entry_to_mod_list')
    mod_info_ae_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_ae_parser.add_argument('pak_dir_structure', help='pak folder structure Str')
    mod_info_ae_parser.add_argument('mod_name_dir_type', help='Corresponding Str value from UnrealModTreeType enum')
    mod_info_ae_parser.add_argument('use_mod_name_dir_name_override', help='true/false string value')
    mod_info_ae_parser.add_argument('mod_name_dir_name_override', help='Mod name dir Str')
    mod_info_ae_parser.add_argument('pak_chunk_num', help='pak chunk Int')
    mod_info_ae_parser.add_argument('packing_type', help='Corresponding Str value from PackingType enum')
    mod_info_ae_parser.add_argument('compression_type', help='Corresponding Str value from CompressionType enum')
    mod_info_ae_parser.add_argument('is_enabled', help='true/false string value')
    mod_info_ae_parser.add_argument('manually_specified_assets_tree_paths', help='A list of one or more Str paths')
    mod_info_ae_parser.add_argument('manually_specified_assets_asset_paths', help='A list of one or more Str paths')

    mod_info_re_parser = unreal_auto_mod_parser.add_parser(name='remove_entry_from_mod_list')
    mod_info_re_parser.add_argument('mod_name', help='Mod name Str')

    mod_info_mn_parser = unreal_auto_mod_parser.add_parser(name='set_mod_name_in_mod_list_entry')
    mod_info_mn_parser.add_argument('before_mod_name', help='Mod name Str')
    mod_info_mn_parser.add_argument('after_mod_name', help='Mod name Str')

    mod_info_pds_parser = unreal_auto_mod_parser.add_parser(name='set_pak_dir_structure_in_mod_list_entry')
    mod_info_pds_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_pds_parser.add_argument('pak_dir_structure', help='pak folder structure Str')

    mod_info_mndt_parser = unreal_auto_mod_parser.add_parser(name='set_mod_name_dir_type_in_mod_list_entry')
    mod_info_mndt_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_mndt_parser.add_argument('mod_name_dir_type', help='Corresponding Str value from UnrealModTreeType enum')

    mod_info_mndno_parser = unreal_auto_mod_parser.add_parser(name='set_use_mod_name_dir_name_override_in_mod_list_entry')
    mod_info_mndno_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_mndno_parser.add_argument('use_mod_name_dir_name_override', help='true/false string value')

    mod_info_mndnon_parser = unreal_auto_mod_parser.add_parser(name='set_mod_name_dir_name_override_in_mod_list_entry')
    mod_info_mndnon_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_mndnon_parser.add_argument('mod_name_dir_name_override', help='Mod name dir Str')

    mod_info_pcn_parser = unreal_auto_mod_parser.add_parser(name='set_pak_chunk_num_in_mod_list_entry')
    mod_info_pcn_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_pcn_parser.add_argument('pak_chunk_num', help='pak chunk Int')

    mod_info_pt_parser = unreal_auto_mod_parser.add_parser(name='set_packing_type_in_mod_list_entry')
    mod_info_pt_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_pt_parser.add_argument('packing_type', help='Corresponding Str value from PackingType enum')

    mod_info_ct_parser = unreal_auto_mod_parser.add_parser(name='set_compression_type_in_mod_list_entry')
    mod_info_ct_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_ct_parser.add_argument('compression_type', help='Corresponding Str value from CompressionType enum')

    mod_info_ie_parser = unreal_auto_mod_parser.add_parser(name='set_is_enabled_in_mod_list_entry')
    mod_info_ie_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_ie_parser.add_argument('is_enabled', help='true/false string value')

    mod_info_atp_parser = unreal_auto_mod_parser.add_parser(name='add_tree_paths_to_mod_list_entry')
    mod_info_atp_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_atp_parser.add_argument('manually_specified_assets_tree_paths', help='A list of one or more Str paths')

    mod_info_rat_parser = unreal_auto_mod_parser.add_parser(name='remove_trees_paths_from_mod_list_entry')
    mod_info_rat_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_rat_parser.add_argument('manually_specified_assets_tree_paths', help='A list of one or more Str paths')

    mod_info_aap_parser = unreal_auto_mod_parser.add_parser(name='add_asset_paths_to_mod_list_entry')
    mod_info_aap_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_aap_parser.add_argument('manually_specified_assets_asset_paths', help='A list of one or more Str paths')

    mod_info_rap_parser = unreal_auto_mod_parser.add_parser(name='remove_asset_paths_from_mod_list_entry')
    mod_info_rap_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_rap_parser.add_argument('manually_specified_assets_asset_paths', help='A list of one or more Str paths')

    test_mods_parser = unreal_auto_mod_parser.add_parser(name='test_mods')
    test_mods_parser.add_argument('mod_names', help='list of mod_names, strings')

    test_mods_all_parser = unreal_auto_mod_parser.add_parser(name='test_mods_all')
    test_mods_all_parser.add_argument('settings_json_path', help='Path to settings.json')

    args = parser.parse_args()
    cli_args = sys.argv[2:]

    unreal_auto_mod_parser_dict = {
        'add_entry_to_alt_exe_info': 'add_alt_exe_entry',
        'remove_entry_from_alt_exe_info': 'remove_alt_exe_entry',
        'set_script_state_in_alt_exe_entry': 'set_script_state_in_alt_exe_entry',
        'set_alt_exe_path_in_alt_exe_entry': 'set_alt_exe_path_in_alt_exe_entry',
        'set_execution_mode_in_alt_exe_entry': 'set_execution_mode_in_alt_exe_entry',
        'add_args_to_alt_exe_entry': 'add_arg_to_variable_list_in_alt_exe_entry',
        'remove_args_from_alt_exe_entry': 'remove_arg_from_variable_list_in_alt_exe_entry',
        'set_override_working_dir': 'set_general_info_override_default_working_dir',
        'set_working_dir': 'set_general_info_working_dir',
        'set_window_title': 'set_general_info_window_title',
        'set_use_alt_uproject_name': 'set_alt_uproject_name_in_game_dir_use_alt_method',
        'set_alt_uproject_name': 'set_alt_uproject_name_in_game_dir_name',
        'set_repak_path': 'set_repak_info_repak_path',
        'set_override_automatic_repak_version_finding': 'set_repak_info_override_automatic_version_finding',
        'set_repak_version': 'set_repak_info_repak_version',
        'set_unreal_engine_dir': 'set_engine_info_unreal_engine_dir',
        'set_unreal_project_path': 'set_engine_info_unreal_project_file',
        'set_toggle_engine_during_testing': 'set_engine_info_toggle_engine_during_testing',
        'set_resave_packages_and_fix_up_redirectors_before_engine_open': 'set_engine_info_resave_packages_and_fix_up_redirectors_before_engine_open',
        'add_engine_launch_args': 'add_entry_to_engine_info_launch_args',
        'remove_engine_launch_args': 'remove_entry_from_engine_info_launch_args',
        'add_cook_and_packaging_args': 'add_entry_to_engine_info_cook_and_packaging',
        'remove_cook_and_packaging_args': 'remove_entry_from_engine_info_cook_and_packaging',
        'set_use_unversioned_cooked_content': 'set_engine_info_use_unversioned_cooked_content',
        'set_clear_uproject_saved_cooked_dir_before_tests': 'set_engine_info_clear_uproject_saved_cooked_dir_before_tests',
        'set_always_build_project': 'set_engine_info_always_build_project',
        'set_override_automatic_engine_version_finding': 'set_engine_info_override_automatic_version_finding',
        'set_unreal_engine_major_version': 'set_engine_info_unreal_engine_major_version',
        'set_unreal_engine_minor_version': 'set_engine_info_unreal_engine_minor_version',
        'set_game_path': 'set_game_info_game_exe_path',
        'set_game_launch_type': 'set_game_info_launch_type',
        'set_override_automatic_launcher_finding': 'set_game_info_override_automatic_launcher_exe_finding',
        'set_game_launcher_path': 'set_game_info_game_launcher_exe',
        'set_game_id': 'set_game_info_game_id',
        'set_skip_game_launch': 'set_game_info_skip_launching_game',
        'set_override_automatic_window_title_finding': 'set_game_info_override_automatic_window_title_finding',
        'set_window_title_override_string': 'set_game_info_override_automatic_window_title_finding',
        'add_params_to_game_launch_params': 'add_entry_to_game_info_launch_params',
        'remove_params_from_game_launch_params': 'remove_entry_from_game_info_launch_params',
        'set_auto_close_game': 'set_process_kill_info_auto_close_game',
        'add_entry_to_process_info': 'add_process_kill_entry',
        'remove_entry_from_process_info': 'remove_process_kill_entry',
        'set_process_name_in_process_entry': 'set_process_name_in_process_entry',
        'set_use_substring_check_in_process_entry': 'set_use_substring_check_in_process_info_entry',
        'set_script_state_in_process_entry': 'set_script_state_in_process_info_entry',
        'add_entry_to_window_management': 'add_entry_to_window_management',
        'remove_entry_from_window_management': 'remove_entry_from_window_management',
        'set_window_name_in_window_management_entry': 'set_window_name_in_window_management_entry',
        'set_use_substring_check_in_window_management_entry': 'set_use_substring_check_in_window_management_entry',
        'set_window_behaviour_in_window_management_entry': 'set_window_behaviour_in_window_management_entry',
        'set_script_state_in_window_management_entry': 'set_script_state_in_window_management_entry',
        'set_monitor_index_in_window_management_entry': 'set_monitor_index_in_window_management_entry',
        'set_resolution_x_in_window_management_entry': 'set_resolution_x_in_window_management_entry',
        'set_resolution_y_in_window_management_entry': 'set_resolution_y_in_window_management_entry',
        'add_entry_to_mod_list': 'add_entry_to_mod_list',
        'remove_entry_from_mod_list': 'remove_entry_from_mod_list',
        'set_mod_name_in_mod_list_entry': 'set_mod_name_in_mod_list_entry',
        'set_pak_dir_structure_in_mod_list_entry': 'set_pak_dir_structure_in_mod_list_entry',
        'set_mod_name_dir_type_in_mod_list_entry': 'set_mod_name_dir_type_in_mod_list_entry',
        'set_use_mod_name_dir_name_override_in_mod_list_entry': 'set_use_mod_name_dir_name_override_in_mod_list_entry',
        'set_mod_name_dir_name_override_in_mod_list_entry': 'set_mod_name_dir_name_override_in_mod_list_entry',
        'set_pak_chunk_num_in_mod_list_entry': 'set_pak_chunk_num_in_mod_list_entry',
        'set_packing_type_in_mod_list_entry': 'set_packing_type_in_mod_list_entry',
        'set_compression_type_in_mod_list_entry': 'set_compression_type_in_mod_list_entry',
        'set_is_enabled_in_mod_list_entry': 'set_is_enabled_in_mod_list_entry',
        'add_tree_paths_to_mod_list_entry': 'add_tree_paths_to_mod_list_entry',
        'remove_trees_paths_from_mod_list_entry': 'remove_trees_paths_from_mod_list_entry',
        'add_asset_paths_to_mod_list_entry': 'add_asset_tree_paths_to_mod_list_entry',
        'remove_asset_paths_from_mod_list_entry': 'remove_asset_tree_paths_from_mod_list_entry',
        'test_mods': 'test_mods',
        'test_mods_all': 'test_mods_all'
    }

    for key in unreal_auto_mod_parser_dict.keys():
        if args.unreal_auto_mod_parser == key:
            function_name = unreal_auto_mod_parser_dict[key]
            if function_name:
                function = getattr(settings, function_name)
                print(f'called function: {function_name}')
                print('cli args:')
                for arg in cli_args:
                    print(f'arg: {arg}')

                function(*cli_args)


if __name__ == "__main__":
    cli_logic()
