import sys
import argparse
import settings_configurator


def main():
    parser = argparse.ArgumentParser(description='UnrealAutoMod CLI Information')

  
    alt_exe_parser = parser.add_subparsers(dest='alt_exe_entry')


    alt_exe_parser_name = 'add_entry_to_alt_exe_entry'
    alt_exe_parser_help = 'takes in settings.json path, then alt_exe_path'
    alt_exe_parser_description = 'adds an entry to the alt_exe_methods section of the setting.json'

    add_entry_to_alt_exe_entry_parser = alt_exe_parser.add_parser(name=alt_exe_parser_name, help=alt_exe_parser_help, description=alt_exe_parser_description)
    add_entry_to_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_entry_to_alt_exe_entry_parser.add_argument('alt_exe_path', help='Path to the executable') 
    add_entry_to_alt_exe_entry_parser.add_argument('script_state', help='Corresponding Str value from the ScriptStateType enum') 
    add_entry_to_alt_exe_entry_parser.add_argument('execution_mode', help='Corresponding Str value from the ExecutionMode enum') 
    add_entry_to_alt_exe_entry_parser.add_argument('variable_args', nargs='+', help='List of one or more Str args to pass to the exe when launched') 


    rm_ae_name = 'remove_entry_from_alt_exe_entry'
    rm_ae_help = 'takes in settings.json path, then alt_exe_path'
    rm_ae_description = 'removes an entry from the alt_exe_methods section of the setting.json'
    remove_entry_from_alt_exe_entry_parser = alt_exe_parser.add_parser(name=rm_ae_name, help=rm_ae_help, description=rm_ae_description)
    remove_entry_from_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_entry_from_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')    
    
    
    ss_ae_name = 'set_script_state_in_alt_exe_entry'
    ss_ae_help = 'takes in settings.json path, alt_exe_path, then ScriptStateType enum str value'
    ss_ae_description = 'sets the script_state value in the corresponding entry in the settings.json'
    set_script_state_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name=ss_ae_name, help=ss_ae_help, description=ss_ae_description)
    set_script_state_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_script_state_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    set_script_state_in_alt_exe_entry_parser.add_argument('script_state', help='ScriptStateType enum str value')   

    
    ap_ae_name = 'set_alt_exe_path_in_alt_exe_entry'
    ap_ae_help = 'takes in settings.json path, before_alt_exe_path, then after_alt_exe_path'
    ap_ae_description = 'sets the alt_exe_path in the corresponding entry in the settings.json'
    set_alt_exe_path_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name=ap_ae_name, help=ap_ae_help, description=ap_ae_description)
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')  
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')


    em_ae_name = 'set_execution_mode_in_alt_exe_entry'
    em_ae_help = 'takes in settings.json path, alt_exe_path, then ExecutionMode enum str value'
    em_ae_description = 'sets the execution_mode value in the corresponding entry in the settings.json'
    set_exec_mode_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name=em_ae_name, help=em_ae_help, description=em_ae_description)
    set_exec_mode_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_exec_mode_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    set_exec_mode_in_alt_exe_entry_parser.add_argument('execution_mode', help='ExecutionMode enum str value') 

    
    aa_ae_name = 'add_args_to_alt_exe_entry'
    aa_ae_help = 'takes in settings.json path, alt_exe_path, then one or more string args'
    aa_ae_description = 'adds one or more string args to the corresponding entry in the settings.json'
    add_args_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name=aa_ae_name, help=aa_ae_help, description=aa_ae_description)
    add_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    add_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')
   

    rm_args_ae_name = 'remove_args_from_alt_exe_entry'
    rm_args_ae_help = 'takes in settings.json path, alt_exe_path, then one or more string args'
    rm_args_ae_description = 'removes one or more string args to the corresponding entry in the settings.json'
    remove_args_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name=rm_args_ae_name, help=rm_args_ae_help, description=rm_args_ae_description)
    remove_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    remove_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')


    args = parser.parse_args()
    if args.alt_exe_entry == 'add_entry_to_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        script_state = sys.argv[4]
        exec_mode = sys.argv[5]
        args = sys.argv[6:]
        settings_configurator.add_alt_exe_entry(json_path, script_state, alt_exe_path, exec_mode, args)
    elif args.alt_exe_entry == 'remove_entry_from_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]    
        settings_configurator.remove_alt_exe_entry(json_path, alt_exe_path)
    elif args.alt_exe_entry == 'set_script_state_in_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        script_state = sys.argv[4]       
        settings_configurator.set_script_state_in_alt_exe_entry(json_path, alt_exe_path, script_state)
    elif args.alt_exe_entry == 'set_alt_exe_path_in_alt_exe_entry':
        json_path = sys.argv[2]
        before_alt_exe_path = sys.argv[3]
        after_alt_exe_path = sys.argv[4]
        settings_configurator.set_alt_exe_path_in_alt_exe_entry(json_path, before_alt_exe_path, after_alt_exe_path)
    elif args.alt_exe_entry == 'set_execution_mode_in_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        exec_mode = sys.argv[4]
        settings_configurator.set_execution_mode_in_alt_exe_entry(json_path, alt_exe_path, exec_mode)
    elif args.alt_exe_entry == 'add_args_to_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        args = sys.argv[4:]
        settings_configurator.add_arg_to_variable_list_in_alt_exe_entry(json_path, alt_exe_path, args)
    elif args.alt_exe_entry == 'remove_args_from_alt_exe_entry':
        json_path = sys.argv[2]
        alt_exe_path = sys.argv[3]
        args = sys.argv[4:]
        settings_configurator.remove_arg_from_variable_list_in_alt_exe_entry(json_path, alt_exe_path, args)


if __name__ == "__main__":
    main()
