import os
import shutil
import subprocess

import packing
import script_states
import utilities
from enums import CompressionType, ScriptStateType


def get_pak_dir_to_pack(mod_name: str):
    return f'{utilities.get_working_dir()}/{mod_name}'


def get_unreal_pak_exe_path() -> str:
    return f'{utilities.get_unreal_engine_dir()}/Engine/Binaries/Win64/UnrealPak.exe'


def get_pak_dir_to_pack(mod_name: str) -> str:
    return f'{utilities.get_working_dir()}/{mod_name}'


def make_response_file(mod_name: str) -> str:
    file_list_path = os.path.join(utilities.get_working_dir(), "filelist.txt")
    if os.path.isfile(file_list_path):
        os.remove(file_list_path)

    dir_to_pack = get_pak_dir_to_pack(mod_name)
    print("Directory to pack:", dir_to_pack)

    with open(file_list_path, "w") as file:
        for root, _, files in os.walk(dir_to_pack):
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(root, dir_to_pack).replace("\\", "/")
                mount_point = f'../../../{relative_path}/'
                file.write(f'"{absolute_path}" "{mount_point}"\n')

    print("Created response file:", file_list_path)
    return file_list_path


def install_unreal_pak_mod(mod_name: str, compression_type: CompressionType):
    move_files_for_packing(mod_name)
    compression_str = CompressionType(compression_type).value
    output_pak_dir = f'{utilities.get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}'
    if not os.path.isdir(output_pak_dir):
        os.makedirs(output_pak_dir)
    exe_path = get_unreal_pak_exe_path()
    pak_path = f'{output_pak_dir}/{mod_name}.pak'
    response_file = make_response_file(mod_name)
    command = f'{exe_path} "{pak_path}" -Create="{response_file}"'
    if not compression_str == 'None':
        command = f'{command} -compress -compressionformat={compression_str}'
    packing.command_queue.append(command)


def move_files_for_packing(mod_name: str):
    mod_files_dict = packing.get_mod_file_paths_for_manually_made_pak_mods(mod_name)
    for before_file in mod_files_dict.keys():
        after_file = mod_files_dict[before_file]
        if os.path.exists(after_file):
            from utilities import get_do_files_have_same_hash
            if not get_do_files_have_same_hash(before_file, after_file):
                os.remove(after_file)
            else:
                return
        if not os.path.isdir(os.path.dirname(after_file)):
            os.makedirs(os.path.dirname(after_file))
        if os.path.isfile(before_file):
            shutil.copy2(before_file, after_file)
