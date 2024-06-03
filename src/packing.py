import os
import shutil
import utilities
from settings import settings
from script_states import ScriptState
from enums import PackingType, ScriptStateType, CompressionType, get_enum_from_val


class PopulateQueueTypeCheckDicts():
    global install_queue_types
    install_queue_types = []
    global uninstall_queue_types
    uninstall_queue_types = []
    
    from settings import SCRIPT_ARG
    if SCRIPT_ARG == 'test_mods':
        from settings import mod_names
        for packing_type in list(PackingType):
            for mod_pak_info in settings['mod_pak_info']:
                if mod_pak_info['is_enabled'] and mod_pak_info['mod_name'] in mod_names:
                    install_queue_type = get_enum_from_val(PackingType, mod_pak_info['packing_type'])
                    if not install_queue_type in install_queue_types:
                        install_queue_types.append(install_queue_type)
                if not mod_pak_info['is_enabled'] and mod_pak_info['mod_name'] in mod_names:
                    uninstall_queue_type = get_enum_from_val(PackingType, mod_pak_info['packing_type'])
                    if not uninstall_queue_type in uninstall_queue_types:
                        uninstall_queue_types.append(uninstall_queue_type)                
    else:
        for packing_type in list(PackingType):
            for mod_pak_info in settings['mod_pak_info']:
                if mod_pak_info['is_enabled']:
                    install_queue_type = get_enum_from_val(PackingType, mod_pak_info['packing_type'])
                    if not install_queue_type in install_queue_types:
                        install_queue_types.append(install_queue_type)
                else:
                    uninstall_queue_type = get_enum_from_val(PackingType, mod_pak_info['packing_type'])
                    if not uninstall_queue_type in uninstall_queue_types:
                        uninstall_queue_types.append(uninstall_queue_type)                


def get_mod_packing_type(mod_name: str) -> PackingType:
    for mod_pak_info in utilities.get_mod_pak_info_list():
        if mod_name == mod_pak_info['mod_name']:
            return get_enum_from_val(PackingType, mod_pak_info['packing_type'])


def get_is_mod_name_in_use(mod_name: str) -> bool:
    for mod_pak_info in utilities.get_mod_pak_info_list():
        if mod_name == mod_pak_info['mod_name']:
            return True
    return False


def get_mod_pak_entry(mod_name: str) -> dict:
    for info in utilities.get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return dict(info)
    return None


def get_is_mod_installed(mod_name: str) -> bool:
    for info in utilities.get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return True
    return False


def get_engine_pak_command() -> str:
    return (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{utilities.get_uproject_file()}" '
        f'-noP4 '
        f'-cook '
        f'-iterate '
        f'-stage '
        f'-pak '
        f'-compressed'
    )


def get_is_using_unversioned_cooked_content() -> bool:
    return settings['engine_info']['use_unversioned_cooked_content']


def get_cook_project_command() -> str:
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{utilities.get_uproject_file()}" '
        f'-noP4 '
        f'-cook '
        f'-iterate '
        f'-skipstage '
        f'-nocompileeditor '
        f'-nodebuginfo'
    )
    if get_is_using_unversioned_cooked_content():
        unversioned_arg = '-unversionedcookedcontent'
        command = f'{command} {unversioned_arg}'
    return command


def cook_uproject():
    run_proj_command(get_cook_project_command())
 

def package_uproject():
    run_proj_command(get_engine_pak_command())   


def run_proj_command(command: str):
    os.chdir(utilities.get_unreal_engine_dir())
    os.system(command)


def handle_uninstall_logic(packing_type: PackingType):
    ScriptState.set_script_state(ScriptStateType.PRE_MODS_UNINSTALL)
    from settings import SCRIPT_ARG
    if SCRIPT_ARG == 'test_mods':
        from settings import mod_names
        for mod_pak_info in settings['mod_pak_info']: 
            if not mod_pak_info['is_enabled'] and mod_pak_info['mod_name'] in mod_names:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    uninstall_mod(packing_type, mod_pak_info['mod_name'])
    else:
        for mod_pak_info in settings['mod_pak_info']: 
            if not mod_pak_info['is_enabled']:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    uninstall_mod(packing_type, mod_pak_info['mod_name'])
    ScriptState.set_script_state(ScriptStateType.POST_MODS_UNINSTALL)


def handle_install_logic(packing_type: PackingType):
    ScriptState.set_script_state(ScriptStateType.PRE_MODS_INSTALL)
    from settings import SCRIPT_ARG
    if SCRIPT_ARG == 'test_mods':
        from settings import mod_names
        for mod_pak_info in settings['mod_pak_info']: 
            if mod_pak_info['is_enabled'] and mod_pak_info['mod_name'] in mod_names:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    install_mod(packing_type, mod_pak_info['mod_name'], get_enum_from_val(CompressionType, mod_pak_info['compression_type']))
    else:
        for mod_pak_info in settings['mod_pak_info']: 
            if mod_pak_info['is_enabled']:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    install_mod(packing_type, mod_pak_info['mod_name'], get_enum_from_val(CompressionType, mod_pak_info['compression_type']))
    ScriptState.set_script_state(ScriptStateType.POST_MODS_INSTALL)


def make_mods():
    if utilities.get_clear_uproject_saved_cooked_dir_before_tests:
        shutil.rmtree(f'{utilities.get_uproject_dir()}/Saved/Cooked')
    cooking()
    
    global uninstall_queue_types
    for uninstall_queue_type in uninstall_queue_types:
        handle_uninstall_logic(uninstall_queue_type)

    global install_queue_types
    for install_queue_type in install_queue_types:
        handle_install_logic(install_queue_type)


def uninstall_loose_mod(mod_name: str):
    mod_files = utilities.get_mod_paths_for_loose_mods(mod_name)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        file_to_remove = mod_files[key]
        if os.path.isfile(file_to_remove):
            os.remove(file_to_remove)

    for folder in set(os.path.dirname(file) for file in mod_files.values()):
         if os.path.exists(folder) and not os.listdir(folder):
             os.removedirs(folder)


def uninstall_pak_mod(mod_name: str):
    extensions = utilities.get_mod_extensions()
    if utilities.is_game_ue5():
        extensions.extend(['ucas', 'utoc'])
    for extension in extensions:
        file_path = f'{utilities.get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.{extension}'
        if os.path.isfile(file_path):
            os.remove(file_path) 


def uninstall_mod(packing_type: PackingType, mod_name: str):
    if packing_type == PackingType.LOOSE:
        uninstall_loose_mod(mod_name)
    else:
        if packing_type in list(PackingType):
            uninstall_pak_mod(mod_name)


def install_loose_mod(mod_name: str):
    mod_files = utilities.get_mod_paths_for_loose_mods(mod_name)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        before_file = key
        after_file = mod_files[key]
        dir = os.path.dirname(after_file)
        if not os.path.isdir(dir):
            os.makedirs(dir)
        if os.path.exists(after_file):
            if not utilities.get_do_files_have_same_hash(before_file, after_file):
                shutil.copyfile(before_file, after_file)
        else:
            shutil.copyfile(before_file, after_file)


def install_engine_mod(mod_name: str):
    info_list = utilities.get_mod_pak_info_list()
    for info in info_list:
        mod_files = []
        if info['mod_name'] == mod_name:
            pak_chunk_num = info['pak_chunk_num']
            prefix = f'{utilities.get_uproject_dir()}/Saved/StagedBuilds/{utilities.get_win_dir_str()}/{utilities.get_uproject_name()}/Content/Paks/pakchunk{pak_chunk_num}-{utilities.get_win_dir_str()}.'
            mod_files.append(prefix)
            for file in mod_files:
                for suffix in utilities.get_mod_extensions():
                    before_file = f'{file}{suffix}'
                    dir = f'{utilities.get_game_dir()}/Content/Paks/{utilities.get_pak_dir_structure(mod_name)}'
                    if not os.path.isdir(dir):
                        os.makedirs(dir)
                    after_file = f'{dir}/{mod_name}.{suffix}'
                    if os.path.exists(after_file):
                        if not utilities.get_do_files_have_same_hash(before_file, after_file):
                            shutil.copy2(before_file, after_file)
                    else:
                        shutil.copy2(before_file, after_file)


def install_mod(packing_type: PackingType, mod_name: str, compression_type: CompressionType):
    if packing_type == PackingType.LOOSE:
        install_loose_mod(mod_name)
    if packing_type == PackingType.ENGINE:
        install_engine_mod(mod_name)
    if packing_type == PackingType.REPAK:
        from repak import install_repak_mod
        install_repak_mod(mod_name)
    if packing_type == PackingType.UNREAL_PAK:
        from unreal_pak import install_unreal_pak_mod
        install_unreal_pak_mod(mod_name, compression_type)


def cooking():
    ScriptState.set_script_state(ScriptStateType.PRE_COOKING)
    if not PackingType.ENGINE in install_queue_types:
        cook_uproject()
    else:
        package_uproject()
    ScriptState.set_script_state(ScriptStateType.POST_COOKING)
