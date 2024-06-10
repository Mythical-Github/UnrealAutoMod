import os
import shutil
import subprocess
import settings
import utilities
import unreal_pak
import script_states
from enums import PackingType, ScriptStateType, CompressionType, get_enum_from_val


install_queue_types = []
uninstall_queue_types = []


class PopulateQueueTypeCheckDicts():
    global install_queue_types
    global uninstall_queue_types
    for mod_name in settings.mod_names:
        print(mod_name)
    if settings.SCRIPT_ARG == 'test_mods':
        for packing_type in list(PackingType):
            for mod_info in settings.settings['mod_pak_info']:
                if mod_info['is_enabled'] and mod_info['mod_name'] in settings.mod_names:
                    install_queue_type = get_enum_from_val(PackingType, mod_info['packing_type'])
                    if not install_queue_type in install_queue_types:
                        install_queue_types.append(install_queue_type)
                if not mod_info['is_enabled'] and mod_info['mod_name'] in settings.mod_names:
                    uninstall_queue_type = get_enum_from_val(PackingType, mod_info['packing_type'])
                    if not uninstall_queue_type in uninstall_queue_types:
                        uninstall_queue_types.append(uninstall_queue_type)                
    else:
        for packing_type in list(PackingType):
            for mod_info in settings.settings['mod_pak_info']:
                if mod_info['is_enabled']:
                    install_queue_type = get_enum_from_val(PackingType, mod_info['packing_type'])
                    if not install_queue_type in install_queue_types:
                        install_queue_types.append(install_queue_type)
                else:
                    uninstall_queue_type = get_enum_from_val(PackingType, mod_info['packing_type'])
                    if not uninstall_queue_type in uninstall_queue_types:
                        uninstall_queue_types.append(uninstall_queue_type)                


def get_mod_packing_type(mod_name: str) -> PackingType:
    for mod_pak_info in utilities.get_mod_pak_info_list():
        if mod_name == mod_pak_info['mod_name']:
            return get_enum_from_val(PackingType, mod_pak_info['packing_type'])
    return None


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


def get_is_using_unversioned_cooked_content() -> bool:
    return settings.settings['engine_info']['use_unversioned_cooked_content']


def get_engine_pak_command() -> str:
    command = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{utilities.get_uproject_file()}" '
        f'-noP4 '
        f'-cook '
        f'-iterate '
        f'-stage '
        f'-pak '
        f'-compressed'
    )
    if get_is_using_unversioned_cooked_content():
        unversioned_arg = '-unversionedcookedcontent'
        command = f'{command} {unversioned_arg}'
    if utilities.get_always_build_project() or not utilities.has_build_target_been_built():
        build_arg = '-build'
        command = f'{command} {build_arg}'
    for arg in utilities.get_engine_cook_and_packaging_args():
        command = f'{command} {arg}'
    if utilities.get_is_game_iostore():
        command = f'{command} -iostore'
    return command


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
    if utilities.get_always_build_project() or not utilities.has_build_target_been_built():
        build_arg = '-build'
        command = f'{command} {build_arg}'
    for arg in utilities.get_engine_cook_and_packaging_args():
        command = f'{command} {arg}'
    return command


def cook_uproject():
    run_proj_command(get_cook_project_command())
 

def package_uproject():
    run_proj_command(get_engine_pak_command())   


def run_proj_command(command: str):
    print(command)
    subprocess.run(command, check=True, shell=True, cwd=utilities.get_unreal_engine_dir())


def handle_uninstall_logic(packing_type: PackingType):
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_MODS_UNINSTALL)
    if settings.SCRIPT_ARG == 'test_mods':
        for mod_pak_info in settings.settings['mod_pak_info']: 
            if not mod_pak_info['is_enabled'] and mod_pak_info['mod_name'] in settings.mod_names:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    uninstall_mod(packing_type, mod_pak_info['mod_name'])
    else:
        for mod_pak_info in settings.settings['mod_pak_info']: 
            if not mod_pak_info['is_enabled']:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    uninstall_mod(packing_type, mod_pak_info['mod_name'])
    script_states.ScriptState.set_script_state(ScriptStateType.POST_MODS_UNINSTALL)


def handle_install_logic(packing_type: PackingType):
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_MODS_INSTALL)
    if settings.SCRIPT_ARG == 'test_mods':
        for mod_pak_info in settings.settings['mod_pak_info']: 
            if mod_pak_info['is_enabled'] and mod_pak_info['mod_name'] in settings.mod_names:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    install_mod(packing_type, mod_pak_info['mod_name'], get_enum_from_val(CompressionType, mod_pak_info['compression_type']))
    else:
        for mod_pak_info in settings.settings['mod_pak_info']: 
            if mod_pak_info['is_enabled']:
                if get_enum_from_val(PackingType, mod_pak_info['packing_type']) == packing_type:
                    install_mod(packing_type, mod_pak_info['mod_name'], get_enum_from_val(CompressionType, mod_pak_info['compression_type']))
    script_states.ScriptState.set_script_state(ScriptStateType.POST_MODS_INSTALL)


def make_mods():
    if utilities.get_clear_uproject_saved_cooked_dir_before_tests():
        cooked_dir = f'{utilities.get_uproject_dir()}/Saved/Cooked'
        if os.path.isdir(cooked_dir):
            shutil.rmtree(cooked_dir)
    cooking()
    
    global uninstall_queue_types
    for uninstall_queue_type in uninstall_queue_types:
        handle_uninstall_logic(uninstall_queue_type)

    global install_queue_types
    for install_queue_type in install_queue_types:
        handle_install_logic(install_queue_type)


def uninstall_loose_mod(mod_name: str):
    mod_files = get_mod_paths_for_loose_mods(mod_name)
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
    mod_files = get_mod_paths_for_loose_mods(mod_name)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        before_file = key
        after_file = mod_files[key]
        _dir = os.path.dirname(after_file)
        if not os.path.isdir(_dir):
            os.makedirs(_dir)
        if os.path.exists(after_file):
            if not utilities.get_do_files_have_same_hash(before_file, after_file):
                shutil.copyfile(before_file, after_file)
        else:
            shutil.copyfile(before_file, after_file)


def install_engine_mod(mod_name: str):
    mod_files = []
    info = utilities.get_mod_pak_info(mod_name)
    pak_chunk_num = info['pak_chunk_num']
    prefix = f'{utilities.get_uproject_dir()}/Saved/StagedBuilds/{utilities.get_win_dir_str()}/{utilities.get_uproject_name()}/Content/Paks/pakchunk{pak_chunk_num}-{utilities.get_win_dir_str()}.'
    mod_files.append(prefix)
    for file in mod_files:
        for suffix in utilities.get_mod_extensions():
            before_file = f'{file}{suffix}'
            dir_engine_mod = f'{utilities.get_game_dir()}/Content/Paks/{utilities.get_pak_dir_structure(mod_name)}'
            if not os.path.isdir(dir_engine_mod):
                os.makedirs(dir_engine_mod)
            after_file = f'{dir_engine_mod}/{mod_name}.{suffix}'
            if os.path.exists(after_file):
                if not utilities.get_do_files_have_same_hash(before_file, after_file):
                    shutil.copy2(before_file, after_file)
            else:
                shutil.copy2(before_file, after_file)


def make_pak_repak(mod_name: str):
    pak_dir = f'{utilities.get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}'
    if not os.path.isdir(pak_dir):
        os.makedirs(pak_dir)
    os.chdir(pak_dir)

    compression_type_str = utilities.get_mod_pak_info(mod_name)['compression_type']
    before_symlinked_dir = f'{utilities.get_working_dir()}/{mod_name}'
    

    command = f'{utilities.get_repak_exe_path()} pack {before_symlinked_dir} {pak_dir}/{mod_name}.pak'
    if not compression_type_str == 'None':
        command = f'{command} --compression {compression_type_str} --version {utilities.get_repak_pak_version_str()}'
    if os.path.isfile(f'{pak_dir}/{mod_name}.pak'):
        os.remove(f'{pak_dir}/{mod_name}.pak')
    print(command)
    subprocess.run(command)


def install_repak_mod(mod_name: str):
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_PAK_DIR_SETUP)
    mod_files_dict = get_mod_file_paths_for_manually_made_pak_mods(mod_name)
    for before_file in mod_files_dict.keys():
        after_file = mod_files_dict[before_file]
        if os.path.exists(after_file):
            if not utilities.get_do_files_have_same_hash(before_file, after_file):
                os.remove(after_file)
            else:
                return
        if not os.path.isdir(os.path.dirname(after_file)):
            os.makedirs(os.path.dirname(after_file))
        if os.path.isfile(before_file):
            print(before_file)
            print(after_file)
            shutil.copy2(before_file, after_file)
    script_states.ScriptState.set_script_state(ScriptStateType.POST_PAK_DIR_SETUP)
    make_pak_repak(mod_name)


def install_mod(packing_type: PackingType, mod_name: str, compression_type: CompressionType):
    if packing_type == PackingType.LOOSE:
        install_loose_mod(mod_name)
    if packing_type == PackingType.ENGINE:
        install_engine_mod(mod_name)
    if packing_type == PackingType.REPAK:
        install_repak_mod(mod_name)
    if packing_type == PackingType.UNREAL_PAK:
        unreal_pak.install_unreal_pak_mod(mod_name, compression_type)


def cooking():
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_COOKING)
    if PackingType.ENGINE not in install_queue_types:
        cook_uproject()
    else:
        package_uproject()
    script_states.ScriptState.set_script_state(ScriptStateType.POST_COOKING)


def get_mod_files_asset_paths_for_loose_mods(mod_name: str) -> dict:
    file_dict = {}
    cooked_uproject_dir = utilities.get_cooked_uproject_dir()
    mod_pak_info = get_mod_pak_entry(mod_name)
    for asset in mod_pak_info['manually_specified_assets']['asset_paths']:
        base_path = f'{cooked_uproject_dir}/{asset}'
        for extension in utilities.get_file_extensions(base_path):
            before_path = f'{base_path}{extension}'
            after_path = f'{utilities.get_game_dir()}/{asset}{extension}'
            file_dict[before_path] = after_path
    return file_dict


def get_mod_files_tree_paths_for_loose_mods(mod_name: str) -> dict:
    file_dict = {}
    cooked_uproject_dir = utilities.get_cooked_uproject_dir()
    mod_pak_info = get_mod_pak_entry(mod_name)
    for tree in mod_pak_info['manually_specified_assets']['tree_paths']:
        tree_path = f'{cooked_uproject_dir}/{tree}'
        for entry in utilities.get_files_in_tree(tree_path):
            if os.path.isfile(entry):
                base_entry = os.path.splitext(entry)[0]
                for extension in utilities.get_file_extensions(entry):
                    before_path = f'{base_entry}{extension}'
                    relative_path = os.path.relpath(base_entry, cooked_uproject_dir)
                    after_path = f'{utilities.get_game_dir()}/{relative_path}{extension}'
                    file_dict[before_path] = after_path
    return file_dict


def get_mod_files_persistant_paths_for_loose_mods(mod_name: str) -> dict:
    file_dict = {}
    persistant_mod_dir = utilities.get_persistant_mod_dir(mod_name)

    for root, _, files in os.walk(persistant_mod_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, persistant_mod_dir)
            game_dir = utilities.get_game_dir()
            game_dir = os.path.dirname(game_dir)
            game_dir_path = os.path.join(game_dir, relative_path)
            file_dict[file_path] = game_dir_path
    return file_dict


def get_mod_files_mod_name_dir_paths_for_loose_mods(mod_name: str) -> dict:
    file_dict = {}
    cooked_game_name_mod_dir = f'{utilities.get_cooked_uproject_dir()}/Content/{utilities.get_unreal_mod_tree_type_str(mod_name)}/{utilities.get_mod_name_dir_name(mod_name)}'
    for file in utilities.get_files_in_tree(cooked_game_name_mod_dir):
        relative_file_path = os.path.relpath(file, cooked_game_name_mod_dir)
        before_path = f'{cooked_game_name_mod_dir}/{relative_file_path}'
        after_path = f'{os.path.dirname(utilities.get_game_dir())}/Content/{utilities.get_unreal_mod_tree_type_str(mod_name)}/{utilities.get_mod_name_dir_name(mod_name)}/{relative_file_path}'
        file_dict[before_path] = after_path
    return file_dict


def get_mod_paths_for_loose_mods(mod_name: str) -> dict:
    file_dict = {}
    file_dict.update(get_mod_files_asset_paths_for_loose_mods(mod_name))
    file_dict.update(get_mod_files_tree_paths_for_loose_mods(mod_name))
    file_dict.update(get_mod_files_persistant_paths_for_loose_mods(mod_name))
    file_dict.update(get_mod_files_mod_name_dir_paths_for_loose_mods(mod_name))

    return file_dict

def get_cooked_mod_file_paths(mod_name: str) -> list:
    return list((get_mod_paths_for_loose_mods(mod_name)).keys())


def get_game_mod_file_paths(mod_name: str) -> list:
    return list((get_mod_paths_for_loose_mods(mod_name)).values())


def get_mod_file_paths_for_manually_made_pak_mods_asset_paths(mod_name: str) -> dict:
    file_dict = {}
    cooked_uproject_dir = utilities.get_cooked_uproject_dir()
    mod_pak_info = get_mod_pak_entry(mod_name)
    for asset in mod_pak_info['manually_specified_assets']['asset_paths']:
        base_path = f'{cooked_uproject_dir}/{asset}'
        for extension in utilities.get_file_extensions(base_path):
            before_path = f'{base_path}{extension}'
            after_path = f'{utilities.get_working_dir()}/{mod_name}/{utilities.get_uproject_name()}/{asset}{extension}'
            file_dict[before_path] = after_path
    return file_dict


def get_mod_file_paths_for_manually_made_pak_mods_tree_paths(mod_name: str) -> dict:
    file_dict = {}
    cooked_uproject_dir = utilities.get_cooked_uproject_dir()
    mod_pak_info = get_mod_pak_entry(mod_name)
    for tree in mod_pak_info['manually_specified_assets']['tree_paths']:
        tree_path = f'{cooked_uproject_dir}/{tree}'
        for entry in utilities.get_files_in_tree(tree_path):
            if os.path.isfile(entry):
                base_entry = os.path.splitext(entry)[0]
                for extension in utilities.get_file_extensions(entry):
                    before_path = f'{base_entry}{extension}'
                    relative_path = os.path.relpath(base_entry, cooked_uproject_dir)
                    after_path = f'{utilities.get_working_dir()}/{mod_name}/{utilities.get_uproject_name()}/{relative_path}{extension}'
                    file_dict[before_path] = after_path
    return file_dict


def get_mod_file_paths_for_manually_made_pak_mods_persistent_paths(mod_name: str) -> dict:
    file_dict = {}
    persistant_mod_dir = utilities.get_persistant_mod_dir(mod_name)

    for root, _, files in os.walk(persistant_mod_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, persistant_mod_dir)
            game_dir = utilities.get_working_dir()
            game_dir = os.path.dirname(game_dir)
            game_dir_path = f'{utilities.get_working_dir()}/{mod_name}/{relative_path}'
            file_dict[file_path] = game_dir_path
    return file_dict


def get_mod_file_paths_for_manually_made_pak_mods_mod_name_dir_paths(mod_name: str) -> dict:
    file_dict = {}
    cooked_game_name_mod_dir = f'{utilities.get_cooked_uproject_dir()}/Content/{utilities.get_unreal_mod_tree_type_str(mod_name)}/{utilities.get_mod_name_dir_name(mod_name)}'
    for file in utilities.get_files_in_tree(cooked_game_name_mod_dir):
        relative_file_path = os.path.relpath(file, cooked_game_name_mod_dir)
        before_path = f'{cooked_game_name_mod_dir}/{relative_file_path}'
        after_path = f'{utilities.get_working_dir()}/{mod_name}/{utilities.get_uproject_name()}/Content/{utilities.get_unreal_mod_tree_type_str(mod_name)}/{utilities.get_mod_name_dir_name(mod_name)}/{relative_file_path}'
        file_dict[before_path] = after_path
    return file_dict


def get_mod_file_paths_for_manually_made_pak_mods(mod_name: str) -> dict:
    file_dict = {}
    file_dict.update(get_mod_file_paths_for_manually_made_pak_mods_asset_paths(mod_name))
    file_dict.update(get_mod_file_paths_for_manually_made_pak_mods_tree_paths(mod_name))
    file_dict.update(get_mod_file_paths_for_manually_made_pak_mods_persistent_paths(mod_name))
    file_dict.update(get_mod_file_paths_for_manually_made_pak_mods_mod_name_dir_paths(mod_name))

    return file_dict
