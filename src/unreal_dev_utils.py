import os
import json


import general_utils
from unreal_dev_enums import PackagingDirType


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


def get_game_paks_dir(uproject_file_path: str, game_dir: str) -> str:
    return f'{os.path.dirname(game_dir)}/{get_uproject_name(uproject_file_path)}/Content/Paks'


def get_is_game_iostore(uproject_file_path: str, game_dir: str) -> bool:
    _game_dir = game_dir
    _uproject_file_path = uproject_file_path
    is_game_iostore = False
    file_extensions = general_utils.get_file_extensions(get_game_paks_dir(_uproject_file_path, _game_dir))
    for file_extension in file_extensions:
        if file_extension == '.ucas':
            is_game_iostore = True
        elif file_extension == '.utoc':
            is_game_iostore = True
    return is_game_iostore


def get_game_dir(game_exe_path: str):
    return os.path.dirname(os.path.dirname(os.path.dirname(game_exe_path)))


def get_game_content_dir(game_dir: str):
    return f'{game_dir}/Content'


def get_game_pak_folder_archives() -> list:
    if general_utils.get_is_game_iostore():
        return [
            'pak',
            'utoc',
            'ucas'
        ]
    else:
        return ['pak']


def get_win_dir_type(unreal_engine_dir: str) -> PackagingDirType:
    if get_unreal_engine_version(unreal_engine_dir).startswith('5'):
        return PackagingDirType.WINDOWS
    else:
        return PackagingDirType.WINDOWS_NO_EDITOR


def is_game_ue5(unreal_engine_dir: str) -> bool:
    return get_win_dir_type(unreal_engine_dir) == PackagingDirType.WINDOWS


def is_game_ue4(unreal_engine_dir: str) -> bool:
    return get_win_dir_type(unreal_engine_dir) == PackagingDirType.WINDOWS_NO_EDITOR


def get_unreal_editor_exe_path(unreal_engine_dir: str) -> str:
    if get_win_dir_type(unreal_engine_dir) == PackagingDirType.WINDOWS_NO_EDITOR:
        engine_path_suffix = 'UE4Editor.exe'
    else:
        engine_path_suffix = 'UnrealEditor.exe'
    return f'{unreal_engine_dir}/Engine/Binaries/Win64/{engine_path_suffix}'


def get_win_dir_str(unreal_engine_dir: str) -> str:
    win_dir_type = 'Windows'
    if is_game_ue4(unreal_engine_dir):
        win_dir_type = f'{win_dir_type}NoEditor'
    return win_dir_type


def get_cooked_uproject_dir(uproject_file_path: str, unreal_engine_dir: str) -> str:
    return f'{get_uproject_dir(uproject_file_path)}/Saved/Cooked/{get_win_dir_str(unreal_engine_dir)}/{get_uproject_name(uproject_file_path)}'


def get_uproject_name(uproject_file_path: str) -> str:
    return os.path.splitext(os.path.basename(uproject_file_path))[0]


def get_uproject_dir(uproject_file_path: str) -> str:
    return os.path.dirname(uproject_file_path)


def get_saved_cooked_dir(uproject_file_path: str) -> str:
    return f'{get_uproject_dir(uproject_file_path)}/Saved/Cooked'


def get_engine_window_title(uproject_file_path: str) -> str:
    return f'{general_utils.get_process_name(uproject_file_path)[:-9]} - {'Unreal Editor'}'


def get_engine_process_name() -> str:
    return general_utils.get_process_name(get_unreal_editor_exe_path())


def get_build_target_file_path(uproject_file_path: str) -> str:
    return f'{get_uproject_dir(uproject_file_path)}/Binaries/Win64/{get_uproject_name(uproject_file_path)}.target'


def has_build_target_been_built(uproject_file_path: str) -> bool:
    return os.path.exists(get_build_target_file_path(uproject_file_path))
