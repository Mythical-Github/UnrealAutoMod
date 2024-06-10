import sys
import argparse
import settings_configurator


def main():
    parser = argparse.ArgumentParser(description='UnrealAutoMod CLI Information')

  
    unreal_auto_mod_parser = parser.add_subparsers(dest='unreal_auto_mod_parser')


    alt_exe_parser_name = 'add_entry_to_alt_exe_entry'
    alt_exe_parser_help = 'takes in settings.json path, then alt_exe_path'
    alt_exe_parser_description = 'adds an entry to the alt_exe_methods section of the setting.json'
    add_entry_to_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=alt_exe_parser_name, help=alt_exe_parser_help, description=alt_exe_parser_description)
    add_entry_to_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_entry_to_alt_exe_entry_parser.add_argument('alt_exe_path', help='Path to the executable') 
    add_entry_to_alt_exe_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum') 
    add_entry_to_alt_exe_entry_parser.add_argument('execution_mode', help='Corresponding Str value from the ExecutionMode enum') 
    add_entry_to_alt_exe_entry_parser.add_argument('variable_args', nargs='+', help='List of one or more Str args to pass to the exe when launched') 


    rm_ae_name = 'remove_entry_from_alt_exe_entry'
    rm_ae_help = 'takes in settings.json path, then alt_exe_path'
    rm_ae_description = 'removes an entry from the alt_exe_methods section of the setting.json'
    remove_entry_from_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=rm_ae_name, help=rm_ae_help, description=rm_ae_description)
    remove_entry_from_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_entry_from_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')    
    
    
    ss_ae_name = 'set_script_state_in_alt_exe_entry'
    ss_ae_help = 'takes in settings.json path, alt_exe_path, then ScriptStateType enum str value'
    ss_ae_description = 'sets the script_state value in the corresponding entry in the settings.json'
    set_script_state_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=ss_ae_name, help=ss_ae_help, description=ss_ae_description)
    set_script_state_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_script_state_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    set_script_state_in_alt_exe_entry_parser.add_argument('script_state', help='ScriptStateType enum str value')   

    
    ap_ae_name = 'set_alt_exe_path_in_alt_exe_entry'
    ap_ae_help = 'takes in settings.json path, before_alt_exe_path, then after_alt_exe_path'
    ap_ae_description = 'sets the alt_exe_path in the corresponding entry in the settings.json'
    set_alt_exe_path_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=ap_ae_name, help=ap_ae_help, description=ap_ae_description)
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')  
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')


    em_ae_name = 'set_execution_mode_in_alt_exe_entry'
    em_ae_help = 'takes in settings.json path, alt_exe_path, then ExecutionMode enum str value'
    em_ae_description = 'sets the execution_mode value in the corresponding entry in the settings.json'
    set_exec_mode_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=em_ae_name, help=em_ae_help, description=em_ae_description)
    set_exec_mode_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_exec_mode_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    set_exec_mode_in_alt_exe_entry_parser.add_argument('execution_mode', help='ExecutionMode enum str value') 

    
    aa_ae_name = 'add_args_to_alt_exe_entry'
    aa_ae_help = 'takes in settings.json path, alt_exe_path, then one or more string args'
    aa_ae_description = 'adds one or more string args to the corresponding entry in the settings.json'
    add_args_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=aa_ae_name, help=aa_ae_help, description=aa_ae_description)
    add_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    add_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')
   

    rm_args_ae_name = 'remove_args_from_alt_exe_entry'
    rm_args_ae_help = 'takes in settings.json path, alt_exe_path, then one or more string args'
    rm_args_ae_description = 'removes one or more string args to the corresponding entry in the settings.json'
    remove_args_in_alt_exe_entry_parser = unreal_auto_mod_parser.add_parser(name=rm_args_ae_name, help=rm_args_ae_help, description=rm_args_ae_description)
    remove_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    remove_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')


    owd_name = 'set_override_working_dir'
    owd_help = 'takes in true/false STR'
    owd_description = 'set whether or not to override the working dir default dir'
    override_working_dir_parser = unreal_auto_mod_parser.add_parser(name=owd_name, help=owd_help, description=owd_description)
    override_working_dir_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_working_dir_parser.add_argument('override_value', help='true/false string value')
    

    wd_name = 'set_working_dir'
    wd_help = 'Path to working_dir'
    wd_description = 'Sets the working dir path, the working dir override uses'
    working_dir_parser = unreal_auto_mod_parser.add_parser(name=wd_name, help=wd_help, description=wd_description)
    working_dir_parser.add_argument('settings_json_path', help='Path to settings.json')
    working_dir_parser.add_argument('working_dir', help='Path to working_dir')
    

    wt_name = 'set_window_title'
    wt_help = 'takes in window title Str'
    wt_description = 'overrides the default script window title'
    window_title_parser = unreal_auto_mod_parser.add_parser(name=wt_name, help=wt_help, description=wt_description)
    window_title_parser.add_argument('settings_json_path', help='Path to settings.json')
    window_title_parser.add_argument('window_title', help='window title Str')


    am_aun_name = 'set_use_alt_uproject_name'
    am_aun_help = 'takes in true/false STR'
    am_aun_description = 'set whether or not to use alt method in alt uproject name in game dir'
    use_alt_method_in_alt_uproject_parser = unreal_auto_mod_parser.add_parser(name=am_aun_name, help=am_aun_help, description=am_aun_description)
    use_alt_method_in_alt_uproject_parser.add_argument('settings_json_path', help='Path to settings.json')
    use_alt_method_in_alt_uproject_parser.add_argument('override_value', help='true/false string value')


    am_augn_name = 'set_alt_uproject_name'
    am_augn_help = 'takes in uproject name STR'
    am_augn_description = 'sets alternative uproject name for packing structures'
    alt_method_alt_uproject_name_parser = unreal_auto_mod_parser.add_parser(name=am_augn_name, help=am_augn_help, description=am_augn_description)
    alt_method_alt_uproject_name_parser.add_argument('settings_json_path', help='Path to settings.json')
    alt_method_alt_uproject_name_parser.add_argument('alt_project_name', help='uproject name Str')


    rpp_name = 'set_repak_path'
    rpp_help = 'takes in repak path Str'
    rpp_description = 'sets the repak path in the repak info section'
    repak_path_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name=rpp_name, help=rpp_help, description=rpp_description)
    repak_path_in_repak_info_parser.add_argument('settings_json_path', help='Path to settings.json')
    repak_path_in_repak_info_parser.add_argument('repak_path', help='Path to repak exe')


    rpo_name = 'set_override_automatic_version_finding'
    rpo_help = 'takes in true/false Str value'
    rpo_description = 'sets whether or not to use the repak version override in the repak info section'
    override_automatic_version_finding_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name=rpo_name, help=rpo_help, description=rpo_description)
    override_automatic_version_finding_in_repak_info_parser.add_argument('settings_json_path', help='Path to settings.json')
    override_automatic_version_finding_in_repak_info_parser.add_argument('override_value', help='true/false string value')


    rpv_name = 'set_repak_version'
    rpv_help = 'takes in repak version Str'
    rpv_description = 'sets the repak version for use with manual override in the repak info section'
    repak_version_in_repak_info_parser = unreal_auto_mod_parser.add_parser(name=rpv_name, help=rpv_help, description=rpv_description)
    repak_version_in_repak_info_parser.add_argument('settings_json_path', help='Path to settings.json')
    repak_version_in_repak_info_parser.add_argument('repak_version', help='repak version in Str')


    ei_ued_name = 'set_unreal_engine_dir'
    ei_ued_help = ''
    ei_ued_description = ''
    engine_info_unreal_engine_dir_parser = unreal_auto_mod_parser.add_parser(name=ei_ued_name, help=ei_ued_help, description=ei_ued_description)
    engine_info_unreal_engine_dir_parser.add_argument('settings_json_path', help='Path to settings.json')
    engine_info_unreal_engine_dir_parser.add_argument('unreal_engine_dir', help='Path to unreal engine directory')


    ei_uep_name = 'set_unreal_project'
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


    ei_oavf_name = 'set_override_automatic_version_finding'
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


    gi_oalef_name = 'set_override_automatic_launcher_exe_finding'
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


    gi_slg_name = 'set_skip_launching_game'
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
    

    # pki__name = ''
    # pki__help = ''
    # pki__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=pki__name, help= pki__help, description=pki__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # pki__name = ''
    # pki__help = ''
    # pki__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=pki__name, help= pki__help, description=pki__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # pki__name = ''
    # pki__help = ''
    # pki__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=pki__name, help= pki__help, description=pki__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # pki__name = ''
    # pki__help = ''
    # pki__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=pki__name, help= pki__help, description=pki__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # pki__name = ''
    # pki__help = ''
    # pki__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=pki__name, help= pki__help, description=pki__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')


    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # amw__name = ''
    # amw__help = ''
    # amw__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=amw__name, help= amw__help, description=amw__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')


    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')
    

    # mod_info__name = ''
    # mod_info__help = ''
    # mod_info__description = ''
    # _parser = unreal_auto_mod_parser.add_parser(name=mod_info__name, help= mod_info__help, description=mod_info__description)
    # _parser.add_argument('settings_json_path', help='Path to settings.json')
    # _parser.add_argument('', help='')


    args = parser.parse_args()


    if args.unreal_auto_mod_parser == 'add_entry_to_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        script_state = sys.argv[4]
        exec_mode = sys.argv[5]
        args = sys.argv[6:]
        settings_configurator.add_alt_exe_entry(json_path, script_state, alt_exe_path, exec_mode, args)
    elif args.unreal_auto_mod_parser == 'remove_entry_from_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]    
        settings_configurator.remove_alt_exe_entry(json_path, alt_exe_path)
    elif args.unreal_auto_mod_parser == 'set_script_state_in_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        script_state = sys.argv[4]       
        settings_configurator.set_script_state_in_alt_exe_entry(json_path, alt_exe_path, script_state)
    elif args.unreal_auto_mod_parser == 'set_alt_exe_path_in_alt_exe_entry':
        json_path = sys.argv[2]
        before_alt_exe_path = sys.argv[3]
        after_alt_exe_path = sys.argv[4]
        settings_configurator.set_alt_exe_path_in_alt_exe_entry(json_path, before_alt_exe_path, after_alt_exe_path)
    elif args.unreal_auto_mod_parser == 'set_execution_mode_in_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        exec_mode = sys.argv[4]
        settings_configurator.set_execution_mode_in_alt_exe_entry(json_path, alt_exe_path, exec_mode)
    elif args.unreal_auto_mod_parser == 'add_args_to_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        args = sys.argv[4:]
        settings_configurator.add_arg_to_variable_list_in_alt_exe_entry(json_path, alt_exe_path, args)
    elif args.unreal_auto_mod_parser == 'remove_args_from_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        args = sys.argv[4:]
        settings_configurator.remove_arg_from_variable_list_in_alt_exe_entry(json_path, alt_exe_path, args)
    elif args.unreal_auto_mod_parser == 'set_override_working_dir_in_general_info':
        json_path = sys.argv[2]
        override_value = sys.argv[3]
        settings_configurator.set_general_info_override_default_working_dir(json_path, override_value)
    elif args.unreal_auto_mod_parser == 'set_working_dir_in_general_info':
        json_path = sys.argv[2]
        working_dir = sys.argv[3]
        settings_configurator.set_general_info_working_dir(json_path, working_dir)
    elif args.unreal_auto_mod_parser == 'set_window_title_in_general_info':
        json_path = sys.argv[2]
        window_title = sys.argv[3]
        settings_configurator.set_general_info_window_title(json_path, window_title)
    elif args.unreal_auto_mod_parser == 'set_use_alt_method_in_alt_uproject_name_in_game_dir':
        json_path = sys.argv[2]
        override_value = sys.argv[3]
        settings_configurator.set_alt_uproject_name_in_game_dir_use_alt_method(json_path, override_value)
    elif args.unreal_auto_mod_parser == 'set_alt_uproject_name_in_alt_uproject_name_in_game_dir':
        json_path = sys.argv[2]
        uproject_str = sys.argv[3]
        settings_configurator.set_alt_uproject_name_in_game_dir_name(json_path, uproject_str)
    elif args.unreal_auto_mod_parser == 'set_repak_path_in_repak_info':
        json_path = sys.argv[2]
        repak_path = sys.argv[3]
        settings_configurator.set_repak_info_repak_path(json_path, repak_path)
    elif args.unreal_auto_mod_parser == 'set_override_automatic_version_finding_in_repak_info':
        json_path = sys.argv[2]
        override_string = sys.argv[3]
        settings_configurator.set_repak_info_override_automatic_version_finding(json_path, override_string)
    elif args.unreal_auto_mod_parser == 'set_repak_version_in_repak_info':
        json_path = sys.argv[2]
        repak_version_string = sys.argv[3]
        settings_configurator.set_repak_info_repak_version(json_path, repak_version_string)
    elif args.unreal_auto_mod_parser == 'set_unreal_engine_dir_in_engine_info':
        json_path = sys.argv[2]
        unreal_engine_dir = sys.argv[3]
        settings_configurator.set_engine_info_unreal_engine_dir(json_path, unreal_engine_dir)
    elif args.unreal_auto_mod_parser == 'set_unreal_project_file_in_engine_info':
        json_path = sys.argv[2]
        uproject_file = sys.argv[3]
        settings_configurator.set_engine_info_unreal_project_file(json_path, uproject_file)
    elif args.unreal_auto_mod_parser == 'set_toggle_engine_during_testing':
        json_path = sys.argv[2]
        override_value = sys.argv[3]
        settings_configurator.set_engine_info_toggle_engine_during_testing(json_path, override_value)
    elif args.unreal_auto_mod_parser == 'set_resave_packages_and_fix_up_redirectors_before_engine_open':
        json_path = sys.argv[2]
        override_value = sys.argv[3]
        settings_configurator.set_engine_info_resave_packages_and_fix_up_redirectors_before_engine_open(json_path, override_value)


if __name__ == "__main__":
    main()
