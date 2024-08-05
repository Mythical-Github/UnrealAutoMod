import os
import json

import general_utils


def get_game_process_name(input_game_exe_path: str) -> str:
    return general_utils.get_process_name(input_game_exe_path)


def get_unreal_engine_version(engine_path: str) -> str:
    version_file_path = f'{engine_path}/Engine/Build/Build.version'
    general_utils.check_file_exists(version_file_path)
    with open(version_file_path, 'r') as f:
        version_info = json.load(f)
        unreal_engine_major_version = version_info.get('MajorVersion', 0)
        unreal_engine_minor_version = version_info.get('MinorVersion', 0)
        return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'


def get_is_game_iostore() -> bool:
    is_game_iostore = False
    file_extensions = get_file_extensions(get_game_paks_dir())
    for file_extension in file_extensions:
        if file_extension == '.ucas':
            is_game_iostore = True
        elif file_extension == '.utoc':
            is_game_iostore = True
    return is_game_iostore


def get_game_dir(game_exe_path: str):
    return os.path.dirname(os.path.dirname(os.path.dirname(game_exe_path)))
