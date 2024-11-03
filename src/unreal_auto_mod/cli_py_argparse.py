import argparse
import sys

from unreal_auto_mod import log_py as log


def cli_logic(cli_info_dict):
    root_parser = argparse.ArgumentParser()
    subparsers = root_parser.add_subparsers(dest="_function_name")

    for command, data in cli_info_dict['commands'].items():
        parser = subparsers.add_parser(command)
        for arg_help_pair in data["arg_help_pairs"]:
            [(name, help)] = arg_help_pair.items()
            parser.add_argument(name, help=help)

    args = root_parser.parse_args()
    function_name = cli_info_dict['commands'][args._function_name]['function_name']
    del args._function_name

    function = getattr(cli_info_dict['module'], function_name)
    cli_args = list(vars(args).values())

    log.log_message(f'Function: {function_name} was called')
    log.log_message('Args:')
    for arg in cli_args:
        log.log_message(f'Arg: {arg}')
    function(*cli_args)
    sys.exit()
