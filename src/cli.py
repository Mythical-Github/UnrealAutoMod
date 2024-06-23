import argparse
import json
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
    cli_json = f'{settings.SCRIPT_DIR}/cli.json'
    with open(cli_json, 'r') as file:
        cli_info_dict = json.load(file)
    
    for entry_key in cli_info_dict:
        arg_help_pairs_list = cli_info_dict[entry_key]['arg_help_pairs']
        for arg_help_dict in arg_help_pairs_list:
            arg_help_dict_keys = list(arg_help_dict.keys())
            if arg_help_dict_keys:
                arg_name = arg_help_dict_keys[0]
                arg_help = arg_help_dict[arg_name]
                parser.add_argument(arg_name, help=arg_help)
            else:
                print("Dictionary is empty or has no keys.")
    args = sys.argv
    cli_args = sys.argv[1:]

    for key in cli_info_dict.keys():
        for arg in args:
            if arg == key:
                function_name = cli_info_dict[key]['function_name']
                if function_name:
                    function = getattr(settings, function_name)
                    print(f'called function: {function_name}')
                    print('cli args:')
                    cli_args[0], cli_args[1] = cli_args[1], cli_args[0]
                    for arg in cli_args:
                        print(f'arg: {arg}')
                    function(*cli_args[1:])
    