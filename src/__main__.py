import sys
import argparse
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


    alt_exe_parser_name = 'add_entry_to_alt_exe_info'
    alt_exe_parser_help = ''
    alt_exe_parser_description = ''
    add_entry_to_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=alt_exe_parser_name, help=alt_exe_parser_help, description=alt_exe_parser_description)
    add_entry_to_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_entry_to_alt_exe_entry_parser.add_argument('alt_exe_path', help='Path to the executable') 
    add_entry_to_alt_exe_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum') 
    add_entry_to_alt_exe_entry_parser.add_argument('execution_mode', help='Corresponding Str value from the ExecutionMode enum') 
    add_entry_to_alt_exe_entry_parser.add_argument('variable_args', nargs='+', help='List of one or more Str args to pass to the exe when launched') 


    rm_ae_name = 'remove_entry_from_alt_exe_info'
    rm_ae_help = ''
    rm_ae_description = ''
    remove_entry_from_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=rm_ae_name, help=rm_ae_help, description=rm_ae_description)
    remove_entry_from_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_entry_from_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')    
    
    
    ss_ae_name = 'set_script_state_in_alt_exe_entry'
    ss_ae_help = ''
    ss_ae_description = ''
    set_script_state_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=ss_ae_name, help=ss_ae_help, description=ss_ae_description)
    set_script_state_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_script_state_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    set_script_state_in_alt_exe_entry_parser.add_argument('script_state', help='ScriptStateType enum str value')   

    
    ap_ae_name = 'set_alt_exe_path_in_alt_exe_entry'
    ap_ae_help = ''
    ap_ae_description = ''
    set_alt_exe_path_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=ap_ae_name, help=ap_ae_help, description=ap_ae_description)
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')  
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')


    em_ae_name = 'set_execution_mode_in_alt_exe_entry'
    em_ae_help = ''
    em_ae_description = ''
    set_exec_mode_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=em_ae_name, help=em_ae_help, description=em_ae_description)
    set_exec_mode_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_exec_mode_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    set_exec_mode_in_alt_exe_entry_parser.add_argument('execution_mode', help='ExecutionMode enum str value') 

    
    aa_ae_name = 'add_args_to_alt_exe_entry'
    aa_ae_help = ''
    aa_ae_description = ''
    add_args_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=aa_ae_name, help=aa_ae_help, description=aa_ae_description)
    add_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    add_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')
   

    rm_args_ae_name = 'remove_args_from_alt_exe_entry'
    rm_args_ae_help = ''
    rm_args_ae_description = ''
    remove_args_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=rm_args_ae_name, help=rm_args_ae_help, description=rm_args_ae_description)
    remove_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    remove_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')


    owd_name = 'set_override_working_dir'
    owd_help = ''
    owd_description = ''
    override_working_dir_parser = unreal_auto_mod_parser.add_parser(name=owd_name, help=owd_help, description=owd_description)
    override_working_dir_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_working_dir_parser.add_argument('override_value', help='true/false string value')
    

    wd_name = 'set_working_dir'
    wd_help = ''
    wd_description = ''
    working_dir_parser = unreal_auto_mod_parser.add_parser(name=wd_name, help=wd_help, description=wd_description)
    working_dir_parser.add_argument('settings_json_path', help='Path to settings.json')
    working_dir_parser.add_argument('working_dir', help='Path to working_dir')
    

    wt_name = 'set_window_title'
    wt_help = ''
    wt_description = ''
    window_title_parser = unreal_auto_mod_parser.add_parser(name=wt_name, help=wt_help, description=wt_description)
    window_title_parser.add_argument('settings_json_path', help='Path to settings.json')
    window_title_parser.add_argument('window_title', help='window title Str')


    am_aun_name = 'set_use_alt_uproject_name'
    am_aun_help = ''
    am_aun_description = ''
    use_alt_method_in_alt_uproject_parser = unreal_auto_mod_parser.add_parser(name=am_aun_name, help=am_aun_help, description=am_aun_description)
    use_alt_method_in_alt_uproject_parser.add_argument('settings_json_path', help='Path to settings.json')
    use_alt_method_in_alt_uproject_parser.add_argument('override_value', help='true/false string value')


    am_augn_name = 'set_alt_uproject_name'
    am_augn_help = ''
    am_augn_description = ''
    alt_method_alt_uproject_name_parser = unreal_auto_mod_parser.add_parser(name=am_augn_name, help=am_augn_help, description=am_augn_description)
    alt_method_alt_uproject_name_parser.add_argument('settings_json_path', help='Path to settings.json')
    alt_method_alt_uproject_name_parser.add_argument('alt_project_name', help='uproject name Str')


    rpp_name = 'set_repak_path'
    rpp_help = ''
    rpp_description = ''
    repak_path_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name=rpp_name, help=rpp_help, description=rpp_description)
    repak_path_in_repak_info_parser.add_argument('settings_json_path', help='Path to settings.json')
    repak_path_in_repak_info_parser.add_argument('repak_path', help='Path to repak exe')


    rpo_name = 'set_override_automatic_repak_version_finding'
    rpo_help = ''
    rpo_description = ''
    override_automatic_version_finding_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name=rpo_name, help=rpo_help, description=rpo_description)
    override_automatic_version_finding_in_repak_info_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_automatic_version_finding_in_repak_info_parser.add_argument('override_value', help='true/false string value')


    rpv_name = 'set_repak_version'
    rpv_help = ''
    rpv_description = ''
    repak_version_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name=rpv_name, help=rpv_help, description=rpv_description)
    repak_version_in_repak_info_parser.add_argument('settings_json_path', help='Path to settings.json')
    repak_version_in_repak_info_parser.add_argument('repak_version', help='repak version in Str')


    ei_ued_name = 'set_unreal_engine_dir'
    ei_ued_help = ''
    ei_ued_description = ''
    engine_info_unreal_engine_dir_parser = unreal_auto_mod_parser.add_parser(name=ei_ued_name, help=ei_ued_help, description=ei_ued_description)
    engine_info_unreal_engine_dir_parser.add_argument('settings_json_path', help='Path to settings.json')
    engine_info_unreal_engine_dir_parser.add_argument('unreal_engine_dir', help='Path to unreal engine directory')


    ei_uep_name = 'set_unreal_project_path'
    ei_uep_help = ''
    ei_uep_description = ''
    engine_info_unreal_engine_project_parser = unreal_auto_mod_parser.add_parser(name=ei_uep_name, help=ei_uep_help, description=ei_uep_description)
    engine_info_unreal_engine_project_parser.add_argument('settings_json_path', help='Path to settings.json')
    engine_info_unreal_engine_project_parser.add_argument('unreal_engine_uproject', help='Path to unreal engine uproject file')


    ei_te_name = 'set_toggle_engine_during_testing'
    ei_te_help = ''
    ei_te_description = ''
    toggle_engine_parser = unreal_auto_mod_parser.add_parser(name=ei_te_name, help=ei_te_help, description=ei_te_description)
    toggle_engine_parser.add_argument('settings_json_path', help='Path to settings.json')
    toggle_engine_parser.add_argument('override_value', help='true/false string value')


    ei_rsfu_name = 'set_resave_packages_and_fix_up_redirectors_before_engine_open'
    ei_rsfu_help = ''
    ei_rsfu_description = ''
    toggle_engine_parser = unreal_auto_mod_parser.add_parser(name=ei_rsfu_name, help=ei_rsfu_help, description=ei_rsfu_description)
    toggle_engine_parser.add_argument('settings_json_path', help='Path to settings.json')
    toggle_engine_parser.add_argument('override_value', help='true/false string value')


    ei_aela_name = 'add_engine_launch_args'
    ei_aela_help = ''
    ei_aela_description = ''
    add_engine_args_parser = unreal_auto_mod_parser.add_parser(name=ei_aela_name, help= ei_aela_help, description=ei_aela_description)
    add_engine_args_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_engine_args_parser.add_argument('engine_args', help='one or more string args')


    ei_rela_name = 'remove_engine_launch_args'
    ei_rela_help = ''
    ei_rela_description = ''
    add_engine_args_parser = unreal_auto_mod_parser.add_parser(name=ei_rela_name, help= ei_rela_help, description=ei_rela_description)
    add_engine_args_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_engine_args_parser.add_argument('engine_args', help='one or more string args')


    ei_aeca_name = 'add_cook_and_packaging_args'
    ei_aeca_help = ''
    ei_aeca_description = ''
    cook_and_packaging_parser = unreal_auto_mod_parser.add_parser(name=ei_aeca_name, help= ei_aeca_help, description=ei_aeca_description)
    cook_and_packaging_parser.add_argument('settings_json_path', help='Path to settings.json')
    cook_and_packaging_parser.add_argument('cook_and_packaging_args', help='one or more string args')


    ei_reca_name = 'remove_cook_and_packaging_args'
    ei_reca_help = ''
    ei_reca_description = ''
    cook_and_packaging_args_parser = unreal_auto_mod_parser.add_parser(name=ei_reca_name, help= ei_reca_help, description=ei_reca_description)
    cook_and_packaging_args_parser.add_argument('settings_json_path', help='Path to settings.json')
    cook_and_packaging_args_parser.add_argument('cook_and_packaging_args', help='one or more string args')


    ei_uuvc_name = 'set_use_unversioned_cooked_content'
    ei_uuvc_help = ''
    ei_uuvc_description = ''
    use_unversioned_cooked_content_parser = unreal_auto_mod_parser.add_parser(name=ei_uuvc_name, help= ei_uuvc_help, description=ei_uuvc_description)
    use_unversioned_cooked_content_parser.add_argument('settings_json_path', help='Path to settings.json')
    use_unversioned_cooked_content_parser.add_argument('override_value', help='true/false string value')


    ei_cusv_name = 'set_clear_uproject_saved_cooked_dir_before_tests'
    ei_cusv_help = ''
    ei_cusv_description = ''
    clear_uproject_saved_cooked_dir_before_tests_parser = unreal_auto_mod_parser.add_parser(name=ei_cusv_name, help= ei_cusv_help, description=ei_cusv_description)
    clear_uproject_saved_cooked_dir_before_tests_parser.add_argument('settings_json_path', help='Path to settings.json')
    clear_uproject_saved_cooked_dir_before_tests_parser.add_argument('override_value', help='true/false string value')


    ei_abu_name = 'set_always_build_project'
    ei_abu_help = ''
    ei_abu_description = ''
    always_build_project_parser = unreal_auto_mod_parser.add_parser(name=ei_abu_name, help= ei_abu_help, description=ei_abu_description)
    always_build_project_parser.add_argument('settings_json_path', help='Path to settings.json')
    always_build_project_parser.add_argument('override_value', help='true/false string value')


    ei_oavf_name = 'set_override_automatic_engine_version_finding'
    ei_oavf_help = ''
    ei_oavf_description = ''
    override_automatic_version_finding_parser = unreal_auto_mod_parser.add_parser(name=ei_oavf_name, help= ei_oavf_help, description=ei_oavf_description)
    override_automatic_version_finding_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_automatic_version_finding_parser.add_argument('override_value', help='true/false string value')


    ei_ue_maj_v_name = 'set_unreal_engine_major_version'
    ei_ue_maj_v_help = ''
    ei_ue_maj_v_description = ''
    unreal_engine_major_version_parser = unreal_auto_mod_parser.add_parser(name=ei_ue_maj_v_name, help= ei_ue_maj_v_help, description=ei_ue_maj_v_description)
    unreal_engine_major_version_parser.add_argument('settings_json_path', help='Path to settings.json')
    unreal_engine_major_version_parser.add_argument('ue_maj_ver', help='UE major version int')


    ei_ue_min_v_name = 'set_unreal_engine_minor_version'
    ei_ue_min_v_help = ''
    ei_ue_min_v_description = ''
    unreal_engine_minor_version_parser = unreal_auto_mod_parser.add_parser(name=ei_ue_min_v_name, help= ei_ue_min_v_help, description=ei_ue_min_v_description)
    unreal_engine_minor_version_parser.add_argument('settings_json_path', help='Path to settings.json')
    unreal_engine_minor_version_parser.add_argument('ue_min_ver', help='UE minor version int')


    gi_gp_name = 'set_game_path'
    gi_gp_help = ''
    gi_gp_description = ''
    game_path_parser = unreal_auto_mod_parser.add_parser(name=gi_gp_name, help= gi_gp_help, description=gi_gp_description)
    game_path_parser.add_argument('settings_json_path', help='Path to settings.json')
    game_path_parser.add_argument('game_path', help="Path to the game's win64_exe, or equivalent")


    gi_glt_name = 'set_game_launch_type'
    gi_glt_help = ''
    gi_glt_description = ''
    game_launch_type_parser = unreal_auto_mod_parser.add_parser(name=gi_glt_name, help= gi_glt_help, description=gi_glt_description)   
    game_launch_type_parser.add_argument('settings_json_path', help='Path to settings.json')
    game_launch_type_parser.add_argument('game_launch_type', help='Corresponding Str value from game launch type enum')


    gi_oalef_name = 'set_override_automatic_launcher_finding'
    gi_oalef_help = ''
    gi_oalef_description = ''
    override_automatic_launcher_parser = unreal_auto_mod_parser.add_parser(name=gi_oalef_name, help= gi_oalef_help, description=gi_oalef_description)
    override_automatic_launcher_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_automatic_launcher_parser.add_argument('override_value', help='true/false string value')


    gi_glp_name = 'set_game_launcher_path'
    gi_glp_help = ''
    gi_glp_description = ''
    game_launcher_path_parser = unreal_auto_mod_parser.add_parser(name=gi_glp_name, help= gi_glp_help, description=gi_glp_description)
    game_launcher_path_parser.add_argument('settings_json_path', help='Path to settings.json')
    game_launcher_path_parser.add_argument('game_launcher_path', help='Path to the game launcher exe')


    gi_gid_name = 'set_game_id'
    gi_gid_help = ''
    gi_gid_description = ''
    game_id_parser = unreal_auto_mod_parser.add_parser(name=gi_gid_name, help= gi_gid_help, description=gi_gid_description)
    game_id_parser.add_argument('settings_json_path', help='Path to settings.json')
    game_id_parser.add_argument('game_id', help='game id of the game for the launcher, Str')


    gi_slg_name = 'set_skip_game_launch'
    gi_slg_help = ''
    gi_slg_description = ''
    skip_launching_game_parser = unreal_auto_mod_parser.add_parser(name=gi_slg_name, help= gi_slg_help, description=gi_slg_description)
    skip_launching_game_parser.add_argument('settings_json_path', help='Path to settings.json')
    skip_launching_game_parser.add_argument('override_value', help='true/false string value')


    gi_oawtf_name = 'set_override_automatic_window_title_finding'
    gi_oawtf_help = ''
    gi_oawtf_description = ''
    override_automatic_window_title_finding_parser = unreal_auto_mod_parser.add_parser(name=gi_oawtf_name, help= gi_oawtf_help, description=gi_oawtf_description)
    override_automatic_window_title_finding_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_automatic_window_title_finding_parser.add_argument('override_value', help='true/false string value')


    gi_wtos_name = 'set_window_title_override_string'
    gi_wtos_help = ''
    gi_wtos_description = ''
    window_title_override_string_parser = unreal_auto_mod_parser.add_parser(name=gi_wtos_name, help= gi_wtos_help, description=gi_wtos_description)
    window_title_override_string_parser.add_argument('settings_json_path', help='Path to settings.json')
    window_title_override_string_parser.add_argument('window_title_override_string', help='window title Str to be used by the override')


    gi_apglp_name = 'add_params_to_game_launch_params'
    gi_apglp_help = ''
    gi_apglp_description = ''
    add_params_to_game_launch_params_parser = unreal_auto_mod_parser.add_parser(name=gi_apglp_name, help= gi_apglp_help, description=gi_apglp_description)
    add_params_to_game_launch_params_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_params_to_game_launch_params_parser.add_argument('launch_params', help='list of Str to add to game launch param list')


    gi_rpglp_name = 'remove_params_from_game_launch_params'
    gi_rpglp_help = ''
    gi_rpglp_description = ''
    remove_params_from_game_launch_params_parser = unreal_auto_mod_parser.add_parser(name=gi_rpglp_name, help= gi_rpglp_help, description=gi_rpglp_description)
    remove_params_from_game_launch_params_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_params_from_game_launch_params_parser.add_argument('launch_params', help='list of Str to remove from game launch param list')


    pki_acg_name = 'set_auto_close_game'
    pki_acg_help = ''
    pki_acg_description = ''
    auto_close_game_parser = unreal_auto_mod_parser.add_parser(name=pki_acg_name, help= pki_acg_help, description=pki_acg_description)
    auto_close_game_parser.add_argument('settings_json_path', help='Path to settings.json')
    auto_close_game_parser.add_argument('override_value', help='true/false string value')
    

    pki_ae_name = 'add_entry_to_process_info'
    pki_ae_help = ''
    pki_ae_description = ''
    add_pki_entry_parser = unreal_auto_mod_parser.add_parser(name=pki_ae_name, help= pki_ae_help, description=pki_ae_description)
    add_pki_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_pki_entry_parser.add_argument('process_name', help='process name in Str')
    add_pki_entry_parser.add_argument('use_substring_check', help='true/false string value')
    add_pki_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')
   

    pki_re_name = 'remove_entry_from_process_info'
    pki_re_help = ''
    pki_re_description = ''
    remove_pki_entry_parser = unreal_auto_mod_parser.add_parser(name=pki_re_name, help= pki_re_help, description=pki_re_description)
    remove_pki_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_pki_entry_parser.add_argument('process_name', help='process name in Str')
    

    pki_pn_name = 'set_process_name_in_process_info_entry'
    pki_pn_help = ''
    pki_pn_description = ''
    process_name_parser = unreal_auto_mod_parser.add_parser(name=pki_pn_name, help= pki_pn_help, description=pki_pn_description)
    process_name_parser.add_argument('settings_json_path', help='Path to settings.json')
    process_name_parser.add_argument('process_name', help='process name in Str')
    

    pki_uss_name = 'set_use_substring_check_in_process_info_entry'
    pki_uss_help = ''
    pki_uss_description = ''
    pki_use_substring_check_parser = unreal_auto_mod_parser.add_parser(name=pki_uss_name, help= pki_uss_help, description=pki_uss_description)
    pki_use_substring_check_parser.add_argument('settings_json_path', help='Path to settings.json')
    pki_use_substring_check_parser.add_argument('process_name', help='process name in Str')
    pki_use_substring_check_parser.add_argument('use_substring_check', help='true/false string value')
    

    pki_ss_name = 'set_script_state_in_process_info_entry'
    pki_ss_help = ''
    pki_ss_description = ''
    pki_script_state_parser = unreal_auto_mod_parser.add_parser(name=pki_ss_name, help= pki_ss_help, description=pki_ss_description)
    pki_script_state_parser.add_argument('settings_json_path', help='Path to settings.json')
    pki_script_state_parser.add_argument('process_name', help='process name in Str')
    pki_script_state_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')


    amw_ae_name = 'add_entry_to_window_management'
    amw_ae_help = ''
    amw_ae_description = ''
    awm_add_entry_parser = unreal_auto_mod_parser.add_parser(name=amw_ae_name, help= amw_ae_help, description=amw_ae_description)
    awm_add_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    awm_add_entry_parser.add_argument('window_name', help='Window name Str')
    awm_add_entry_parser.add_argument('use_substring_check', help='true/false string value')
    awm_add_entry_parser.add_argument('window_behaviour', help='Corresponding Str value from the WindowAction enum')
    awm_add_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')
    awm_add_entry_parser.add_argument('monitor_index', help='monitor index Int')
    awm_add_entry_parser.add_argument('resolution_x', help='x resolution Int')
    awm_add_entry_parser.add_argument('resolution_y', help='y resolution Int')
    

    amw_re_name = 'remove_entry_from_window_management'
    amw_re_help = ''
    amw_re_description = ''
    amw_re_parser = unreal_auto_mod_parser.add_parser(name=amw_re_name, help= amw_re_help, description=amw_re_description)
    amw_re_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_re_parser.add_argument('window_name', help='Window name Str')
    

    amw_wn_name = 'set_window_name_in_window_management_entry'
    amw_wn_help = ''
    amw_wn_description = ''
    amw_wn_parser = unreal_auto_mod_parser.add_parser(name=amw_wn_name, help= amw_wn_help, description=amw_wn_description)
    amw_wn_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_wn_parser.add_argument('window_name', help='Window name Str')


    amw_uss_name = 'set_use_substring_check_in_window_management_entry'
    amw_uss_help = ''
    amw_uss_description = ''
    amw_uss_parser = unreal_auto_mod_parser.add_parser(name=amw_uss_name, help= amw_uss_help, description=amw_uss_description)
    amw_uss_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_wn_parser.add_argument('window_name', help='Window name Str')
    amw_uss_parser.add_argument('use_substring_check', help='true/false string value')


    amw_wb_name = 'set_window_behaviour_in_window_management_entry'
    amw_wb_help = ''
    amw_wb_description = ''
    amw_wb_parser = unreal_auto_mod_parser.add_parser(name=amw_wb_name, help= amw_wb_help, description=amw_wb_description)
    amw_wb_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_wn_parser.add_argument('window_name', help='Window name Str')
    amw_wb_parser.add_argument('window_behaviour', help='Corresponding Str value from the WindowAction enum')
    

    amw_ss_name = 'set_script_state_in_window_management_entry'
    amw_ss_help = ''
    amw_ss_description = ''
    amw_ss_parser = unreal_auto_mod_parser.add_parser(name=amw_ss_name, help= amw_ss_help, description=amw_ss_description)
    amw_ss_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_ss_parser.add_argument('window_name', help='Window name Str')
    amw_ss_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum')
    

    amw_mi_name = 'set_monitor_index_in_window_management_entry'
    amw_mi_help = ''
    amw_mi_description = ''
    amw_mi_parser = unreal_auto_mod_parser.add_parser(name=amw_mi_name, help= amw_mi_help, description=amw_mi_description)
    amw_mi_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_mi_parser.add_argument('window_name', help='Window name Str')
    amw_mi_parser.add_argument('monitor_index', help='monitor index Int')

    

    amw_srx_name = 'set_resolution_x_in_window_management_entry'
    amw_srx_help = ''
    amw_srx_description = ''
    amw_srx_parser = unreal_auto_mod_parser.add_parser(name=amw_srx_name, help= amw_srx_help, description=amw_srx_description)
    amw_srx_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_srx_parser.add_argument('window_name', help='Window name Str')
    amw_srx_parser.add_argument('resolution_x', help='x resolution Int')
    

    amw_sry_name = 'set_resolution_y_in_window_management_entry'
    amw_sry_help = ''
    amw_sry_description = ''
    amw_sry_parser = unreal_auto_mod_parser.add_parser(name=amw_sry_name, help= amw_sry_help, description=amw_sry_description)
    amw_sry_parser.add_argument('settings_json_path', help='Path to settings.json')
    amw_sry_parser.add_argument('window_name', help='Window name Str')
    amw_sry_parser.add_argument('resolution_y', help='y resolution Int')


    mod_info_ae_name = 'add_entry_to_mod_list'
    mod_info_ae_help = ''
    mod_info_ae_description = ''
    mod_info_ae_parser = unreal_auto_mod_parser.add_parser(name=mod_info_ae_name, help= mod_info_ae_help, description=mod_info_ae_description)
    mod_info_ae_parser.add_argument('settings_json_path', help='Path to settings.json')
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
    

    mod_info_re_name = 'remove_entry_from_mod_list'
    mod_info_re_help = ''
    mod_info_re_description = ''
    mod_info_re_parser = unreal_auto_mod_parser.add_parser(name=mod_info_re_name, help= mod_info_re_help, description=mod_info_re_description)
    mod_info_re_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_re_parser.add_argument('mod_name', help='Mod name Str')
    

    mod_info_mn_name = 'set_mod_name_in_mod_list_entry'
    mod_info_mn_help = ''
    mod_info_mn_description = ''
    mod_info_mn_parser = unreal_auto_mod_parser.add_parser(name=mod_info_mn_name, help= mod_info_mn_help, description=mod_info_mn_description)
    mod_info_mn_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_mn_parser.add_argument('before_mod_name', help='Mod name Str')
    mod_info_mn_parser.add_argument('after_mod_name', help='Mod name Str')
    

    mod_info_pds_name = 'set_pak_dir_structure_in_mod_list_entry'
    mod_info_pds_help = ''
    mod_info_pds_description = ''
    mod_info_pds_parser = unreal_auto_mod_parser.add_parser(name=mod_info_pds_name, help= mod_info_pds_help, description=mod_info_pds_description)
    mod_info_pds_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_pds_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_pds_parser.add_argument('pak_dir_structure', help='pak folder structure Str')
    

    mod_info_mndt_name = 'set_mod_name_dir_type_in_mod_list_entry'
    mod_info_mndt_help = ''
    mod_info_mndt_description = ''
    mod_info_mndt_parser = unreal_auto_mod_parser.add_parser(name=mod_info_mndt_name, help= mod_info_mndt_help, description=mod_info_mndt_description)
    mod_info_mndt_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_mndt_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_mndt_parser.add_argument('mod_name_dir_type', help='Corresponding Str value from UnrealModTreeType enum')
    

    mod_info_mndno_name = 'set_use_mod_name_dir_name_override_in_mod_list_entry'
    mod_info_mndno_help = ''
    mod_info_mndno_description = ''
    mod_info_mndno_parser = unreal_auto_mod_parser.add_parser(name=mod_info_mndno_name, help= mod_info_mndno_help, description=mod_info_mndno_description)
    mod_info_mndno_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_mndno_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_mndno_parser.add_argument('use_mod_name_dir_name_override', help='true/false string value')
    

    mod_info_mndnon_name = 'set_mod_name_dir_name_override_in_mod_list_entry'
    mod_info_mndnon_help = ''
    mod_info_mndnon_description = ''
    mod_info_mndnon_parser = unreal_auto_mod_parser.add_parser(name=mod_info_mndnon_name, help= mod_info_mndnon_help, description=mod_info_mndnon_description)
    mod_info_mndnon_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_mndnon_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_mndnon_parser.add_argument('mod_name_dir_name_override', help='Mod name dir Str')
    

    mod_info_pcn_name = 'set_pak_chunk_num_in_mod_list_entry'
    mod_info_pcn_help = ''
    mod_info_pcn_description = ''
    mod_info_pcn_parser = unreal_auto_mod_parser.add_parser(name=mod_info_pcn_name, help= mod_info_pcn_help, description=mod_info_pcn_description)
    mod_info_pcn_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_pcn_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_pcn_parser.add_argument('pak_chunk_num', help='pak chunk Int')
    

    mod_info_pt_name = 'set_packing_type_in_mod_list_entry'
    mod_info_pt_help = ''
    mod_info_pt_description = ''
    mod_info_pt_parser = unreal_auto_mod_parser.add_parser(name=mod_info_pt_name, help= mod_info_pt_help, description=mod_info_pt_description)
    mod_info_pt_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_pt_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_pt_parser.add_argument('packing_type', help='Corresponding Str value from PackingType enum')
    

    mod_info_ct_name = 'set_compression_type_in_mod_list_entry'
    mod_info_ct_help = ''
    mod_info_ct_description = ''
    mod_info_ct_parser = unreal_auto_mod_parser.add_parser(name=mod_info_ct_name, help= mod_info_ct_help, description=mod_info_ct_description)
    mod_info_ct_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_ct_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_ct_parser.add_argument('compression_type', help='Corresponding Str value from CompressionType enum')
    

    mod_info_ie_name = 'set_is_enabled_in_mod_list_entry'
    mod_info_ie_help = ''
    mod_info_ie_description = ''
    mod_info_ie_parser = unreal_auto_mod_parser.add_parser(name=mod_info_ie_name, help= mod_info_ie_help, description=mod_info_ie_description)
    mod_info_ie_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_ie_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_ie_parser.add_argument('is_enabled', help='true/false string value')
    

    mod_info_atp_name = 'add_tree_paths_to_mod_list_entry'
    mod_info_atp_help = ''
    mod_info_atp_description = ''
    mod_info_atp_parser = unreal_auto_mod_parser.add_parser(name=mod_info_atp_name, help= mod_info_atp_help, description=mod_info_atp_description)
    mod_info_atp_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_atp_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_atp_parser.add_argument('manually_specified_assets_tree_paths', help='A list of one or more Str paths')
    

    mod_info_rat_name = 'remove_trees_paths_from_mod_list_entry'
    mod_info_rat_help = ''
    mod_info_rat_description = ''
    mod_info_rat_parser = unreal_auto_mod_parser.add_parser(name=mod_info_rat_name, help= mod_info_rat_help, description=mod_info_rat_description)
    mod_info_rat_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_rat_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_rat_parser.add_argument('manually_specified_assets_tree_paths', help='A list of one or more Str paths')
    

    mod_info_aap_name = 'add_asset_paths_to_mod_list_entry'
    mod_info_aap_help = ''
    mod_info_aap_description = ''
    mod_info_aap_parser = unreal_auto_mod_parser.add_parser(name=mod_info_aap_name, help= mod_info_aap_help, description=mod_info_aap_description)
    mod_info_aap_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_aap_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_aap_parser.add_argument('manually_specified_assets_asset_paths', help='A list of one or more Str paths')
    

    mod_info_rap_name = 'remove_asset_paths_from_mod_list_entry'
    mod_info_rap_help = ''
    mod_info_rap_description = ''
    mod_info_rap_parser = unreal_auto_mod_parser.add_parser(name=mod_info_rap_name, help= mod_info_rap_help, description=mod_info_rap_description)
    mod_info_rap_parser.add_argument('settings_json_path', help='Path to settings.json')
    mod_info_rap_parser.add_argument('mod_name', help='Mod name Str')
    mod_info_rap_parser.add_argument('manually_specified_assets_asset_paths', help='A list of one or more Str paths')


    test_mods_name = 'test_mods'
    test_mods_help = ''
    test_mods_description = ''
    test_mods_parser = unreal_auto_mod_parser.add_parser(name=test_mods_name, help=test_mods_help, description=test_mods_description)
    test_mods_parser.add_argument('settings_json_path', help='Path to settings.json')
    test_mods_parser.add_argument('mod_names', help='list of mod_names, strings')


    test_mods_all_name = 'test_mods_all'
    test_mods_all_help = ''
    test_mods_all_description = ''
    test_mods_all_parser = unreal_auto_mod_parser.add_parser(name=test_mods_all_name, help=test_mods_all_help, description=test_mods_all_description)
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
