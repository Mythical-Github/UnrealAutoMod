import argparse
import os
import sys
from pathlib import Path

from rich_argparse import RichHelpFormatter

from unreal_auto_mod import log, main_logic

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


default_releases_dir = os.path.normpath(os.path.join(main_logic.settings_json_dir, 'mod_packaging', 'releases'))
default_output_releases_dir = os.path.normpath(os.path.join(SCRIPT_DIR, 'dist'))


def cli_logic():
    enable_vt100()
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

    package_parser = sub_parser.add_parser('package', help='package content for the uproject specified within the settings JSON', formatter_class=RichHelpFormatter)
    package_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_full_parser = sub_parser.add_parser('cleanup_full', help='Cleans up the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_full_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_cooked_parser = sub_parser.add_parser('cleanup_cooked', help='Cleans up the directories made from cooking of the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_cooked_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_build_parser = sub_parser.add_parser('cleanup_build', help='Cleans up the directories made from building of the github repo specified within the settings JSON', formatter_class=RichHelpFormatter)
    cleanup_build_parser.add_argument('settings_json', help='Path to the settings JSON file')

    cleanup_game_parser = sub_parser.add_parser('cleanup_game', help='Cleans up the specified directory, deleting all files not specified within the file list JSON, to generate one use the generate_file_list_json command', formatter_class=RichHelpFormatter)
    cleanup_game_parser.add_argument('settings_json', help='Path to the settings JSON file')

    generate_game_file_list_json_parser = sub_parser.add_parser('generate_game_file_list_json', help='Generates a JSON file containing all of the files in the game directory, from the game exe specified within the settings JSON', formatter_class=RichHelpFormatter)
    generate_game_file_list_json_parser.add_argument('settings_json', help='Path to the settings JSON file')

    # cleanup_game_parser = sub_parser.add_parser('cleanup_game', help='Cleans up the specified directory, deleting all files not specified within the provided, file list JSON', formatter_class=RichHelpFormatter)
    # cleanup_game_parser.add_argument('file_list_json', help='Path to the file list JSON file, usually created from the generate_file_list_json command')
    # cleanup_game_parser.add_argument('game_directory', help='Path to the game directory tree you want to cleanup')

    # generate_file_list_json_parser = sub_parser.add_parser('generate_file_list_json', help='Generates a JSON file containing all of the files in the specified directory tree, for use with other commands', formatter_class=RichHelpFormatter)
    # generate_file_list_json_parser.add_argument('directory', help='Path to the game directory tree you want to cleanup')
    # generate_file_list_json_parser.add_argument('output_json', help='Path to the output JSON file')

    upload_changes_to_repo_parser = sub_parser.add_parser('upload_changes_to_repo', help='Uploads latest changes of the git project to the github repo and branch specified within the settings JSON', formatter_class=RichHelpFormatter)
    upload_changes_to_repo_parser.add_argument('settings_json', help='Path to the settings JSON file')

    resync_dir_with_repo_parser = sub_parser.add_parser('resync_dir_with_repo', help='Cleans up and resyncs a git project to the github repo and branch specified within the settings JSON', formatter_class=RichHelpFormatter)
    resync_dir_with_repo_parser.add_argument('settings_json', help='Path to the settings JSON file')

    open_latest_log_parser = sub_parser.add_parser('open_latest_log', help='Open the latest log file', formatter_class=RichHelpFormatter)
    open_latest_log_parser.add_argument('settings_json', help='Path to the settings JSON file')

    enable_mods_parser = sub_parser.add_parser('enable_mods', help='Enable the given mod names in the provided settings JSON', formatter_class=RichHelpFormatter)
    enable_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    enable_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    disable_mods_parser = sub_parser.add_parser('disable_mods', help='Disable the given mod names in the provided settings JSON', formatter_class=RichHelpFormatter)
    disable_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    disable_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    add_mod_parser = sub_parser.add_parser('add_mod', help='Adds the given mod name in the provided settings JSON', formatter_class=RichHelpFormatter)
    add_mod_parser.add_argument('settings_json', help='Path to the settings JSON file', type=str)
    add_mod_parser.add_argument('mod_name', help='The name of the mod you want to add', type=str)
    add_mod_parser.add_argument('packing_type', help='', choices=['unreal_pak', 'repak', 'engine', 'loose'])
    add_mod_parser.add_argument('pak_dir_structure', help='', type=str)
    add_mod_parser.add_argument('--mod_name_dir_type', help='', type=str, default='Mods')
    add_mod_parser.add_argument('--use_mod_name_dir_name_override', help='', type=bool, default=False)
    add_mod_parser.add_argument('--mod_name_dir_name_override', help='', type=str, default=None)
    add_mod_parser.add_argument('--pak_chunk_num', help='', type=int, default=None)
    add_mod_parser.add_argument('--compression_type', help='', default='')
    add_mod_parser.add_argument('--is_enabled', help='', type=bool, default=True)
    add_mod_parser.add_argument('--asset_paths', help='', type=list, default=[])
    add_mod_parser.add_argument('--tree_paths', help='', type=list, default=[])

    remove_mods_parser = sub_parser.add_parser('remove_mods', help='Removes the given mod names in the provided settings JSON', formatter_class=RichHelpFormatter)
    remove_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    remove_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    run_game_parser = sub_parser.add_parser('run_game', help='Run the game', formatter_class=RichHelpFormatter)
    run_game_parser.add_argument('settings_json', help='Path to the settings JSON file')

    close_game_parser = sub_parser.add_parser('close_game', help='Close the game', formatter_class=RichHelpFormatter)
    close_game_parser.add_argument('settings_json', help='Path to the settings JSON file')

    run_engine_parser = sub_parser.add_parser('run_engine', help='Run the engine', formatter_class=RichHelpFormatter)
    run_engine_parser.add_argument('settings_json', help='Path to the settings JSON file')

    close_engine_parser = sub_parser.add_parser('close_engine', help='Close the engine', formatter_class=RichHelpFormatter)
    close_engine_parser.add_argument('settings_json', help='Path to the settings JSON file')

    test_mods_parser = sub_parser.add_parser('test_mods', help='Run tests for specific mods', formatter_class=RichHelpFormatter)
    test_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    test_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    test_mods_all_parser = sub_parser.add_parser('test_mods_all', help='Run tests for all mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    test_mods_all_parser.add_argument('settings_json', help='Path to the settings JSON file')

    generate_mods_parser = sub_parser.add_parser('generate_mods', help='Generates mods for the specified mod names', formatter_class=RichHelpFormatter)
    generate_mods_parser.add_argument('settings_json', help='Path to the settings JSON file')
    generate_mods_parser.add_argument('mod_names', nargs='+', help='List of mod names')

    generate_mods_all_parser = sub_parser.add_parser('generate_mods_all', help='Generates mods for all enabled mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    generate_mods_all_parser.add_argument('settings_json', help='Path to the settings JSON file')

    generate_mod_releases_parser = sub_parser.add_parser('generate_mod_releases', help='Generate one or more mod releases', formatter_class=RichHelpFormatter)
    generate_mod_releases_parser.add_argument('settings_json', help='Path to the settings JSON file')
    generate_mod_releases_parser.add_argument('mod_names', nargs='+', help='List of mod names')
    generate_mod_releases_parser.add_argument('--base_files_directory', help="Path to dir tree who's content to pack alongside the mod for release", default=default_releases_dir)
    generate_mod_releases_parser.add_argument('--output_directory', help='Path to the output directory', default=default_output_releases_dir)

    generate_mod_releases_all_parser = sub_parser.add_parser('generate_mod_releases_all', help='Generate mod releases for all mods within the specified settings JSON', formatter_class=RichHelpFormatter)
    generate_mod_releases_all_parser.add_argument('settings_json', help='Path to the settings JSON file')
    generate_mod_releases_all_parser.add_argument('--base_files_directory', help="Path to dir tree who's content to pack alongside the mod for release", default=default_releases_dir)
    generate_mod_releases_all_parser.add_argument('--output_directory', help='Path to the output directory', default=default_output_releases_dir)

    generate_uproject_parser = sub_parser.add_parser('generate_uproject', help='Generates a uproject file at the specified location, using the given information', formatter_class=RichHelpFormatter)
    generate_uproject_parser.add_argument('project_file', help='Path to generate the project file at')
    generate_uproject_parser.add_argument('--file_version', help='Uproject file specification. Defaults to 3.', default=3)
    generate_uproject_parser.add_argument('--engine_major_association', help='Major unreal engine version for the project. Example: the 4 in 4.27.', default=4)
    generate_uproject_parser.add_argument('--engine_minor_association', help='Minor unreal engine version for the project. Example: the 27 in 4.27.', default=27)
    generate_uproject_parser.add_argument('--category', help='Category for the uproject', default='Modding')
    generate_uproject_parser.add_argument('--description', help='Description for the uproject', default='Uproject for modding, generated with unreal_auto_mod.')
    generate_uproject_parser.add_argument('--ignore_safety_checks', help='wether or not to override the input checks for this command', default=False)

    resave_packages_and_fix_up_redirectors_parser = sub_parser.add_parser('resave_packages_and_fix_up_redirectors', help='Resaves packages and fixes up redirectors for the project', formatter_class=RichHelpFormatter)
    resave_packages_and_fix_up_redirectors_parser.add_argument('settings_json', help='Path to the settings JSON file')

    install_fmodel_parser = sub_parser.add_parser('install_fmodel', help='Install Fmodel', formatter_class=RichHelpFormatter)
    install_fmodel_parser.add_argument('output_directory', help='Path to the output directory')
    install_fmodel_parser.add_argument('--run_after_install', help='Should the installed program be ran after installation', default=False)

    install_umodel_parser = sub_parser.add_parser('install_umodel', help='Install Umodel', formatter_class=RichHelpFormatter)
    install_umodel_parser.add_argument('output_directory', help='Path to the output directory')
    install_umodel_parser.add_argument('--run_after_install', help='Should the installed program be ran after installation', default=False)

    install_stove_parser = sub_parser.add_parser('install_stove', help='Install Stove', formatter_class=RichHelpFormatter)
    install_stove_parser.add_argument('output_directory', help='Path to the output directory')
    install_stove_parser.add_argument('--run_after_install', help='Should the installed program be ran after installation', default=False)

    install_spaghetti_parser = sub_parser.add_parser('install_spaghetti', help='Install Spaghetti', formatter_class=RichHelpFormatter)
    install_spaghetti_parser.add_argument('output_directory', help='Path to the output directory')
    install_spaghetti_parser.add_argument('--run_after_install', help='Should the installed program be ran after installation', default=False)

    install_uasset_gui_parser = sub_parser.add_parser('install_uasset_gui', help='Install UAssetGUI', formatter_class=RichHelpFormatter)
    install_uasset_gui_parser.add_argument('output_directory', help='Path to the output directory')
    install_uasset_gui_parser.add_argument('--run_after_install', help='Should the installed program be ran after installation', default=False)

    install_kismet_analyzer_parser = sub_parser.add_parser('install_kismet_analyzer', help='Install Kismet Analyzer', formatter_class=RichHelpFormatter)
    install_kismet_analyzer_parser.add_argument('output_directory', help='Path to the output directory')
    install_kismet_analyzer_parser.add_argument('--run_after_install', help='Should the installed program be ran after installation', default=False)

    close_programs_parser = sub_parser.add_parser('close_programs', help='Closes all programs with the exe names provided', formatter_class=RichHelpFormatter)
    close_programs_parser.add_argument('exe_names', nargs='+', help='List of exe names')

    args = parser.parse_args()

    command_function_map = {
        'build': main_logic.build,
        'cook': main_logic.cook,
        'package': main_logic.package,
        'cleanup_full': main_logic.cleanup_full,
        'cleanup_cooked': main_logic.cleanup_cooked,
        'cleanup_build': main_logic.cleanup_build,
        'cleanup_game': main_logic.cleanup_game,
        'generate_game_file_list_json': main_logic.generate_game_file_list_json,
        'resync_dir_with_repo': main_logic.resync_dir_with_repo,
        'upload_changes_to_repo': main_logic.upload_changes_to_repo,
        'enable_mods': main_logic.enable_mods,
        'disable_mods': main_logic.disable_mods,
        'add_mod': main_logic.add_mod,
        'remove_mods': main_logic.remove_mods,
        'open_latest_log': main_logic.open_latest_log,
        'run_game': main_logic.run_game,
        'close_game': main_logic.close_game,
        'run_engine': main_logic.run_engine,
        'close_engine': main_logic.close_engine,
        'test_mods': main_logic.test_mods,
        'test_mods_all': main_logic.test_mods_all,
        'generate_mods': main_logic.generate_mods,
        'generate_mods_all': main_logic.generate_mods_all,
        'generate_mod_releases': main_logic.generate_mod_releases,
        'generate_mod_releases_all': main_logic.generate_mod_releases_all,
        'generate_uproject': main_logic.generate_uproject,
        'resave_packages_and_fix_up_redirectors': main_logic.resave_packages_and_fix_up_redirectors,
        'install_fmodel': main_logic.install_fmodel,
        'install_umodel': main_logic.install_umodel,
        'install_stove': main_logic.install_stove,
        'install_spaghetti': main_logic.install_spaghetti,
        'install_uasset_gui': main_logic.install_uasset_gui,
        'install_kismet_analyzer': main_logic.install_kismet_analyzer,
        'close_programs': main_logic.close_programs
    }

    main_logic.init_thread_system()

    if args.command in command_function_map:
        installer_commands = [
            'install_fmodel',
            'install_umodel',
            'install_uasset_gui',
            'install_kismet_analyzer',
            'install_stove',
            'install_spaghetti'
        ]
        settings_json_commands = [
            'build',
            'cook',
            'cleanup_full',
            'cleanup_cooked',
            'cleanup_build',
            'cleanup_game',
            'generate_game_file_list_json',
            'package',
            'run_engine',
            'close_engine',
            'upload_changes_to_repo',
            'open_latest_log',
            'run_game',
            'close_game',
            'resave_packages_and_fix_up_redirectors',
            'resync_dir_with_repo',
            'test_mods_all',
            'generate_mods_all'
        ]
        if args.command in settings_json_commands:
            command_function_map[args.command](args.settings_json)

        elif args.command == 'close_programs':
            command_function_map[args.command](args.exe_names)

        elif args.command in installer_commands:
            command_function_map[args.command](args.output_directory, args.run_after_install)

        elif args.command == 'enable_mods' or args.command == 'disable_mods' or (args.command == 'remove_mods' or args.command == 'test_mods') or args.command == 'generate_mods':
            command_function_map[args.command](args.settings_json, args.mod_names)

        elif args.command == 'add_mod':
            command_function_map[args.command](
                args.settings_json,
                args.mod_name,
                args.packing_type,
                args.pak_dir_structure,
                args.mod_name_dir_type,
                args.use_mod_name_dir_name_override,
                args.mod_name_dir_name_override,
                args.pak_chunk_num,
                args.compression_type,
                args.is_enabled,
                args.asset_paths,
                args.tree_paths
            )

        elif args.command == 'generate_mod_releases':
            command_function_map[args.command](
                args.settings_json,
                args.mod_names,
                args.base_files_directory,
                args.output_directory
                )

        elif args.command == 'generate_mod_releases_all':
            command_function_map[args.command](
                args.settings_json,
                args.base_files_directory,
                args.output_directory
                )

        elif args.command == 'generate_uproject':
            command_function_map[args.command](
                args.project_file,
                args.file_version,
                args.engine_major_association,
                args.engine_minor_association,
                args.category,
                args.description,
                args.ignore_safety_checks
                )
    else:
        print(f'Unknown command: {args.command}')
        parser.print_help()

    main_logic.close_thread_system()
    from unreal_auto_mod import utilities
    log.log_message(f'Timer: Time since script execution: {utilities.get_running_time()}')


def enable_vt100():
    """Enable VT100 escape codes in the Windows Command Prompt."""
    # Check if VT100 is already enabled
    query_command = 'reg query HKCU\\Console /v VirtualTerminalLevel 2>nul'
    result = os.popen(query_command).read()
    if "0x1" not in result:  # If not enabled, set the registry key
        os.system('reg add HKCU\\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul')
