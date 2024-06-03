import os
import shutil
import utilities
import script_states
from enums import ScriptStateType


def get_repak_version_str_from_engine_version() -> str:
    engine_version_to_repack_version = {
        "4.0": "V1",
        "4.1": "V1",
        "4.2": "V1",
        "4.3": "V3",
        "4.4": "V3",
        "4.5": "V3",
        "4.6": "V3",
        "4.7": "V3",
        "4.8": "V3",
        "4.9": "V3",
        "4.10": "V3",
        "4.11": "V3",
        "4.12": "V3",
        "4.13": "V3",
        "4.14": "V3",
        "4.15": "V3",
        "4.16": "V4",
        "4.17": "V4",
        "4.18": "V4",
        "4.19": "V4",
        "4.20": "V5",
        "4.21": "V7",
        "4.22": "V8A",
        "4.23": "V8B",
        "4.24": "V8B",
        "4.25": "V9",
        "4.26": "V11",
        "4.27": "V11",
        "4.28": "V11",
        "5.0": "V11",
        "5.1": "V11",
        "5.2": "V11",
        "5.3": "V11",
        "5.4": "V11"
    }
    return engine_version_to_repack_version[utilities.get_unreal_engine_version(utilities.get_unreal_engine_dir())]


def get_is_overriding_automatic_version_finding() -> bool:
    from settings import settings
    return settings['repak_info']['override_automatic_version_finding']


def get_repak_pak_version_str() -> str:
    if get_is_overriding_automatic_version_finding():
        from settings import settings
        repak_version_str = settings['repak_info']['repak_version']
    else:
        repak_version_str = get_repak_version_str_from_engine_version()
    return repak_version_str


def get_repak_exe_path() -> str:
    from settings import settings
    return settings['repak_info']['repak_path']


def make_pak_repak(mod_name: str):
    pak_dir = f'{utilities.get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}'
    if not os.path.isdir(pak_dir):
        os.makedirs(pak_dir)
    os.chdir(pak_dir)

    compression_type_str = utilities.get_mod_pak_info(mod_name)['compression_type']
    before_symlinked_dir = f'{utilities.get_working_dir()}/{mod_name}'
    

    command = f'{get_repak_exe_path()} pack {before_symlinked_dir} {pak_dir}/{mod_name}.pak'
    if not compression_type_str == 'None':
        command = f'{command} --compression {compression_type_str} --version {get_repak_pak_version_str()}'
    from subprocess import run
    if os.path.isfile(f'{pak_dir}/{mod_name}.pak'):
        os.remove(f'{pak_dir}/{mod_name}.pak')
    print(command)
    run(command)


def install_repak_mod(mod_name: str):
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_PAK_DIR_SETUP)
    mod_files_dict = utilities.get_mod_file_paths_for_manually_made_pak_mods(mod_name)
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
        shutil.copy2(before_file, after_file)
    script_states.ScriptState.set_script_state(ScriptStateType.POST_PAK_DIR_SETUP)
    make_pak_repak(mod_name)
