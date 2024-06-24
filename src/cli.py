import json
import sys
import os

import settings


def cli_logic():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    cli_json = os.path.join(base_path, 'cli.json')

    with open(cli_json, 'r') as file:
        cli_info_dict = json.load(file)

    args = sys.argv
    cli_args = sys.argv[1:]

    if len(sys.argv) < 2:
        for key in cli_info_dict.keys():
            print('Args:')
            print(f'Arg: {key}')
        sys.exit()

    if sys.argv[1] == '-h':
        for key in cli_info_dict.keys():
            print('Args:')
            print(f'Arg: {key}')
        sys.exit()

    if sys.argv[2] == '-h':
        arg = sys.argv[1]
        for entry_key in cli_info_dict:
            if entry_key == arg:
                arg_help_pairs_list = cli_info_dict[entry_key]['arg_help_pairs']
                print('Args:')
                for arg_help_dict in arg_help_pairs_list:
                    arg_help_dict_keys = list(arg_help_dict.keys())
                    if arg_help_dict_keys:
                        arg_name = arg_help_dict_keys[0]
                        arg_help = arg_help_dict[arg_name]
                        print(f'Arg: {arg_name}    Help: {arg_help}')
        sys.exit()


    for entry in cli_info_dict.keys():
        for arg in args:
            if arg == entry:
                function_name = cli_info_dict[entry]['function_name']
                if function_name:
                    function = getattr(settings, function_name)
                    print(f'Function: {function_name} was called')
                    print('Args:')
                    cli_args[0], cli_args[1] = cli_args[1], cli_args[0]
                    for arg in cli_args:
                        print(f'Arg: {arg}')
                    function(*cli_args[1:])
    