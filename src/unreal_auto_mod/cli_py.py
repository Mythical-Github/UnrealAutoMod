import sys

from unreal_auto_mod import log_py as log


def cli_logic(cli_data):
    commands_module = cli_data['module']
    cli_info_dict = cli_data['commands']

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
