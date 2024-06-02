from subprocess import run
from os import makedirs, path
from enums import CompressionType
from utilities import get_unreal_engine_dir, get_pak_dir_structure, get_game_paks_dir


def get_unreal_pak_exe_path() -> str:
    return f'{get_unreal_engine_dir()}/Engine/Binaries/Win64/UnrealPak.exe'


def install_unreal_pak_mod(mod_name: str, compression_type: CompressionType):
    compression_str = CompressionType(compression_type)
    output_pak_dir = f'{get_game_paks_dir()}/{get_pak_dir_structure(mod_name)}'
    if not path.isdir(output_pak_dir):
        makedirs(output_pak_dir)
    exe_path = get_unreal_pak_exe_path()
    pak_path = f'{output_pak_dir}/{mod_name}.pak'
    response_file = f''
    command = f'{exe_path} "{pak_path}" -Create={response_file}'
    if not compression_str == 'None':
        command = f'{command} -compress -compressionformat={compression_str}'
    run(command)
