import argparse
import os
import sys
from pathlib import Path

from rich_argparse import RichHelpFormatter

from unreal_auto_mod import settings

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


    default_releases_dir = os.path.normpath(os.path.join(settings.settings_json_dir, 'mod_packaging', 'releases'))
    default_output_releases_dir = os.path.normpath(os.path.join(SCRIPT_DIR, 'dist'))


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

    cleanup_full_parser = sub_parser.add_parser('cleanup_full', help='Cleans up the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_full_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_cooked_parser = sub_parser.add_parser('cleanup_cooked', help='Cleans up the directories made from cooking of the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_cooked_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_build_parser = sub_parser.add_parser('cleanup_build', help='Cleans up the directories made from building of the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_build_parser.add_argument('settings_json', help='Path to the settings JSON file')

    upload_changes_to_repo_parser = sub_parser.add_parser('upload_changes_to_repo', help='Uploads latest changes of the git project to the github repo and branch specified within the settings JSON', formatter_class=RichHelpFormatter)
    upload_changes_to_repo_parser.add_argument('settings_json', help='Path to the settings JSON file')

    resync_dir_with_repo_parser = sub_parser.add_parser('resync_dir_with_repo', help='Cleans up and resyncs a git project to the github repo and branch specified within the settings JSON', formatter_class=RichHelpFormatter)
    resync_dir_with_repo_parser.add_argument('settings_json', help='Path to the settings JSON file')

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
    create_mod_releases_parser.add_argument('--base_files_directory', help="Path to dir tree who's content to pack alongside the mod for release", default=default_releases_dir)
    create_mod_releases_parser.add_argument('--output_directory', help='Path to the output directory', default=default_output_releases_dir)

    create_mod_releases_all_parser = sub_parser.add_parser('create_mod_releases_all', help='Creates mod releases for all mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    create_mod_releases_all_parser.add_argument('settings_json', help='Path to the settings JSON file')
    create_mod_releases_all_parser.add_argument('--base_files_directory', help="Path to dir tree who's content to pack alongside the mod for release", default=default_releases_dir)
    create_mod_releases_all_parser.add_argument('--output_directory', help='Path to the output directory', default=default_output_releases_dir)

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

    resave_packages_and_fix_up_redirectors_parser = sub_parser.add_parser('resave_packages_and_fix_up_redirectors', help='Resaves packages and fixes up redirectors for the project', formatter_class=RichHelpFormatter)
    resave_packages_and_fix_up_redirectors_parser.add_argument('settings_json', help='Path to the settings JSON file')


    args = parser.parse_args()

    command_function_map = {
        'build': settings.build,
        'cook': settings.cook,
        'cleanup_full': settings.cleanup_full,
        'cleanup_cooked': settings.cleanup_cooked,
        'cleanup_build': settings.cleanup_build,
        'resync_dir_with_repo': settings.resync_dir_with_repo,
        'upload_changes_to_repo': settings.upload_changes_to_repo,
        'open_latest_log': settings.open_latest_log,
        'run_game': settings.run_game,
        'test_mods': settings.test_mods,
        'test_mods_all': settings.test_mods_all,
        'create_mods': settings.create_mods,
        'create_mods_all': settings.create_mods_all,
        'create_mod_releases': settings.create_mod_releases,
        'create_mod_releases_all': settings.create_mod_releases_all,
        'resave_packages_and_fix_up_redirectors': settings.resave_packages_and_fix_up_redirectors,
        'install_fmodel': settings.install_fmodel,
        'install_umodel': settings.install_umodel,
        'install_stove': settings.install_stove,
        'install_spaghetti': settings.install_spaghetti,
        'install_uasset_gui': settings.install_uasset_gui,
        'install_kismet_analyzer': settings.install_kismet_analyzer
    }

    settings.init_thread_system()

    if args.command in command_function_map:
        if args.command == 'build' or args.command == 'cook' or (args.command == 'cleanup_full' or args.command == 'cleanup_cooked') or (args.command == 'cleanup_build' or args.command == 'upload_changes_to_repo' or (args.command == 'open_latest_log' or args.command == 'run_game')):
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
            command_function_map[args.command](args.settings_json, args.mod_names, args.base_files_directory, args.output_directory)
        elif args.command == 'create_mod_releases_all':
            command_function_map[args.command](args.output_directory, args.base_files_directory, args.output_directory)
        elif args.command == 'resave_packages_and_fix_up_redirectors':
            command_function_map[args.command](args.settings_json)
        elif args.command == 'install_fmodel' or args.command == 'install_umodel' or (args.command == 'install_stove' or args.command == 'install_spaghetti') or (args.command == 'install_uasset_gui' or args.command == 'install_kismet_analyzer'):
            command_function_map[args.command](args.output_directory)
        elif args.command == 'resync_dir_with_repo':
            command_function_map[args.command](args.settings_json)
    else:
        print(f'Unknown command: {args.command}')
        parser.print_help()

    settings.close_thread_system()
