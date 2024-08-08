import os
import sys
import json
import importlib

from python_logging import log


default_json_location = f'{os.getcwd()}/cli.json'

def get_resource_path(relative_path):
    try:
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
        return os.path.join(base_path, relative_path)
    except Exception as e:
        log.log_message(f"Error obtaining resource path: {e}")
        return relative_path


def set_json_location(json_path: str):
    global default_json_location
    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        
        json_filename = os.path.basename(json_path)
        
        default_json_location = os.path.join(base_path, json_filename)
    else:
        default_json_location = json_path


def cli_logic():
    cli_json = get_resource_path(default_json_location)

    with open(cli_json, 'r') as file:
        data = json.load(file)

    module_name = data['module_name']
    cli_info_dict = data['commands']

    args = sys.argv[1:]

    def display_help():
        log.log_message('Args:')
        for key in cli_info_dict.keys():
            log.log_message(f'Arg: {key}')
        sys.exit()

    if '-h' in args:
        if len(args) == 1:
            display_help()
        elif len(args) >= 2 and args[1] == '-h':
            arg = args[0]
            if arg in cli_info_dict:
                arg_help_pairs_list = cli_info_dict[arg].get('arg_help_pairs', [])
                log.log_message('Args:')
                for arg_help_dict in arg_help_pairs_list:
                    arg_name, arg_help = list(arg_help_dict.items())[0]
                    log.log_message(f'Arg: {arg_name}    Help: {arg_help}')
            sys.exit()

    commands_module = importlib.import_module(module_name)

    for entry in cli_info_dict.keys():
        if entry in args:
            function_name = cli_info_dict[entry]['function_name']
            if function_name:
                function = getattr(commands_module, function_name)
                log.log_message(f'Function: {function_name} was called')
                log.log_message('Args:')
                cli_args = args[:]
                cli_args.remove(entry)
                for arg in cli_args:
                    log.log_message(f'Arg: {arg}')
                function(*cli_args)
                sys.exit()

    log.log_message('Invalid argument or missing argument.')
    display_help()
