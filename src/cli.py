import json
import sys

import settings


def cli_logic():
    cli_json = f'{settings.SCRIPT_DIR}/cli.json'
    with open(cli_json, 'r') as file:
        cli_info_dict = json.load(file)

    args = sys.argv
    cli_args = sys.argv[1:]

    if len(sys.argv) < 2:
        for key in cli_info_dict.keys():
            print(key)
        sys.exit()

    if sys.argv[1] == '-h':
        for key in cli_info_dict.keys():
            print(key)
        sys.exit()

    if sys.argv[2] == '-h':
        arg = sys.argv[1]
        for entry_key in cli_info_dict:
            if entry_key == arg:
                arg_help_pairs_list = cli_info_dict[entry_key]['arg_help_pairs']
                for arg_help_dict in arg_help_pairs_list:
                    arg_help_dict_keys = list(arg_help_dict.keys())
                    if arg_help_dict_keys:
                        arg_name = arg_help_dict_keys[0]
                        arg_help = arg_help_dict[arg_name]
                        print(f'arg: {arg_name}    help: {arg_help}')
        sys.exit()


    for entry in cli_info_dict.keys():
        for arg in args:
            if arg == entry:
                function_name = cli_info_dict[entry]['function_name']
                if function_name:
                    function = getattr(settings, function_name)
                    print(f'called function: {function_name}')
                    print('cli args:')
                    cli_args[0], cli_args[1] = cli_args[1], cli_args[0]
                    for arg in cli_args:
                        print(f'arg: {arg}')
                    function(*cli_args[1:])
    