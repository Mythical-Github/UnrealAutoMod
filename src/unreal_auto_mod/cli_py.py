import argparse

from rich_argparse import RichHelpFormatter

from unreal_auto_mod import settings


def cli_logic():
    parser_description = 'Mod Build Tools/Automation scripts for Unreal Engine modding supports 4.0-5.5'
    parser_program_name = 'unreal_auto_mod'

    parser = argparse.ArgumentParser(
        prog=parser_program_name,
        description=parser_description,
        formatter_class=RichHelpFormatter
    )

    sub_parser = parser.add_subparsers(dest='command')


    build_parser = sub_parser.add_parser('build', help='Builds the uproject specified within the settings JSON', formatter_class=RichHelpFormatter)
    build_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cook_parser = sub_parser.add_parser('cook', help='Cooks content for the uproject specified within the settings JSON', formatter_class=RichHelpFormatter)
    cook_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_parser = sub_parser.add_parser('cleanup', help='Cleans up the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_parser.add_argument('settings_json', help='Path to the settings JSON file')

    upload_changes_to_repo_parser = sub_parser.add_parser('upload_changes_to_repo', help='Uploads latest changes of the git project to the github repo and branch specified within the settings JSON', formatter_class=RichHelpFormatter)
    upload_changes_to_repo_parser.add_argument('settings_json', help='Path to the settings JSON file')

    open_latest_log_parser = sub_parser.add_parser('open_latest_log', help='Open the latest log file', formatter_class=RichHelpFormatter)
    open_latest_log_parser.add_argument('settings_json', help='Path to the settings JSON file')

    run_game_parser = sub_parser.add_parser('run_game', help='Run the game', formatter_class=RichHelpFormatter)
    run_game_parser.add_argument('settings_json', help='Path to the settings JSON file')

    test_mods_parser = sub_parser.add_parser('test_mods', help='Run tests for specific mods', formatter_class=RichHelpFormatter)
    test_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    test_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    test_mods_all_parser = sub_parser.add_parser('test_mods_all', help='Run tests for all mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    test_mods_all_parser.add_argument('settings_json', help='Path to the settings JSON file')

    create_mods_parser = sub_parser.add_parser('create_mods', help='Creates mods for the specified mod names', formatter_class=RichHelpFormatter)
    create_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    create_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    create_mods_all_parser = sub_parser.add_parser('create_mods_all', help='Creates mods for all enabled mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    create_mods_all_parser.add_argument('settings_json', help='Path to the settings JSON file')

    create_mod_releases_parser = sub_parser.add_parser('create_mod_releases', help='Create one or more mod releases', formatter_class=RichHelpFormatter)
    create_mod_releases_parser.add_argument('settings_json', help='Path to the settings JSON file')
    create_mod_releases_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    create_mod_releases_all_parser = sub_parser.add_parser('create_mod_releases_all', help='Creates mod releases for all mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    create_mod_releases_all_parser.add_argument('settings_json', help='Path to the settings JSON file')

    install_fmodel_parser = sub_parser.add_parser('install_fmodel', help='Install Fmodel', formatter_class=RichHelpFormatter)
    install_fmodel_parser.add_argument('output_directory', help='Path to the output directory')

    install_umodel_parser = sub_parser.add_parser('install_umodel', help='Install Umodel', formatter_class=RichHelpFormatter)
    install_umodel_parser.add_argument('output_directory', help='Path to the output directory')

    install_stove_parser = sub_parser.add_parser('install_stove', help='Install Stove', formatter_class=RichHelpFormatter)
    install_stove_parser.add_argument('output_directory', help='Path to the output directory')

    install_spaghetti_parser = sub_parser.add_parser('install_spaghetti', help='Install Spaghetti', formatter_class=RichHelpFormatter)
    install_spaghetti_parser.add_argument('output_directory', help='Path to the output directory')

    install_uasset_gui_parser = sub_parser.add_parser('install_uasset_gui', help='Install UAssetGUI', formatter_class=RichHelpFormatter)
    install_uasset_gui_parser.add_argument('output_directory', help='Path to the output directory')

    install_kismet_analyzer_parser = sub_parser.add_parser('install_kismet_analyzer', help='Install Kismet Analyzer', formatter_class=RichHelpFormatter)
    install_kismet_analyzer_parser.add_argument('output_directory', help='Path to the output directory')


    args = parser.parse_args()

    command_function_map = {
        'build': settings.build,
        'cook': settings.cook,
        'cleanup': settings.cleanup,
        'upload_changes_to_repo': settings.upload_changes_to_repo,
        'open_latest_log': settings.open_latest_log,
        'run_game': settings.run_game,
        'test_mods': settings.test_mods,
        'test_mods_all': settings.test_mods_all,
        'create_mods_all': settings.create_mods_all,
        'create_mod_releases': settings.create_mod_releases,
        'create_mod_releases_all': settings.create_mod_releases_all,
        'install_fmodel': settings.install_fmodel,
        'install_umodel': settings.install_umodel,
        'install_stove': settings.install_stove,
        'install_spaghetti': settings.install_spaghetti,
        'install_uasset_gui': settings.install_uasset_gui,
        'install_kismet_analyzer': settings.install_kismet_analyzer
    }

    if args.command in command_function_map:
        if args.command == 'build':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'cook':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'cleanup':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'upload_changes_to_repo':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'open_latest_log':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'run_game':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'test_mods':
            command_function_map[args.command](args.settings_json, args.mod_names)
        elif args.command == 'test_mods_all':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'create_mods':
            command_function_map[args.command](args.settings_json, args.mod_names)
        elif args.command == 'create_mods_all':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'create_mod_releases':
            command_function_map[args.command](args.settings_json, args.mod_names)
        elif args.command == 'create_mod_releases_all':
            command_function_map[args.command](args.output_directory)
        elif args.command == 'install_fmodel':
            command_function_map[args.command](args.output_directory)
        elif args.command == 'install_umodel':
            command_function_map[args.command](args.output_directory)
        elif args.command == 'install_stove':
            command_function_map[args.command](args.output_directory)
        elif args.command == 'install_spaghetti':
            command_function_map[args.command](args.output_directory)
        elif args.command == 'install_uasset_gui':
            command_function_map[args.command](args.output_directory)
        elif args.command == 'install_kismet_analyzer':
            command_function_map[args.command](args.output_directory)
    else:
        print(f'Unknown command: {args.command}')
        parser.print_help()
