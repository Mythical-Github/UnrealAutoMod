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


    remove_entry_from_alt_exe_entry_parser = alt_exe_parser.add_parser(name='remove_entry_from_alt_exe_entry', help='takes in settings.json path, then alt_exe_path', description='removes an entry from the alt_exe_methods section of the setting.json')
    remove_entry_from_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_entry_from_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')    
    
    
    set_script_state_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name='set_script_state_in_alt_exe_entry', help='takes in settings.json path, alt_exe_path, then ScriptStateType enum str value', description='sets the script_state value in the corresponding entry in the settings.json')
    set_script_state_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_script_state_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    set_script_state_in_alt_exe_entry_parser.add_argument('script_state', help='ScriptStateType enum str value')   

  
    set_alt_exe_path_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name='set_alt_exe_path_in_alt_exe_entry', help='takes in settings.json path, before_alt_exe_path, then after_alt_exe_path', description='sets the alt_exe_path in the corresponding entry in the settings.json')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')  
    set_alt_exe_path_in_alt_exe_entry_parser.add_argument('after_alt_exe_path', help='after alt_exe_path of the entry')
    

    alt_exe_parser.add_parser(name='set_execution_mode_in_alt_exe_entry', help='takes in settings.json path, alt_exe_path, then ExecutionMode enum str value', description='sets the execution_mode value in the corresponding entry in the settings.json')
   
   
    add_args_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name='add_args_to_alt_exe_entry', help='takes in settings.json path, then one or more string args', description='adds one or more string args to the corresponding entry in the settings.json')
    add_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    add_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')       
    add_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')
   

    remove_args_in_alt_exe_entry_parser = alt_exe_parser.add_parser(name='remove_args_from_alt_exe_entry', help='takes in settings.json path, then one or more string args', description='removes one or more string args to the corresponding entry in the settings.json')
    remove_args_in_alt_exe_entry_parser.add_argument('settings_json_path', help='Path to settings.json')
    remove_args_in_alt_exe_entry_parser.add_argument('alt_exe_path', help='alt_exe_path of the entry')   
    remove_args_in_alt_exe_entry_parser.add_argument('args', nargs='+', help='One or more string args')


    args = parser.parse_args()
    if args.alt_exe_entry == 'add_entry_to_alt_exe_entry':
        settings_configurator.add_alt_exe_entry()
    elif args.alt_exe_entry == 'remove_entry_from_alt_exe_entry':
        settings_configurator.remove_alt_exe_entry()
    elif args.alt_exe_entry == 'set_script_state_in_alt_exe_entry':
        settings_configurator.set_script_state_in_alt_exe_entry()
    elif args.alt_exe_entry == 'set_alt_exe_path_in_alt_exe_entry':
        settings_configurator.set_alt_exe_path_in_alt_exe_entry()
    elif args.alt_exe_entry == 'set_execution_mode_in_alt_exe_entry':
        settings_configurator.set_execution_mode_in_alt_exe_entry()
    elif args.alt_exe_entry == 'add_args_to_alt_exe_entry':
        settings_configurator.add_arg_to_variable_list_in_alt_exe_entry()
    elif args.alt_exe_entry == 'remove_args_from_alt_exe_entry':
        settings_configurator.remove_arg_from_variable_list_in_alt_exe_entry()


if __name__ == "__main__":
    main()
