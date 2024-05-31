import os
import psutil
import shutil
import utilities
from settings import settings
from script_states import ScriptState
from enums import PackingType, ScriptStateType, get_enum_from_val


class PopulateQueueTypeCheckDict():
    global queue_types
    queue_types = []

    for packing_type in list(PackingType):
        for mod_pak_info in settings['mod_pak_info']: 
            queue_type = get_enum_from_val(PackingType, mod_pak_info['packing_type'])
            if not queue_type in queue_types:
                queue_types.append(queue_type)


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


def get_is_mod_enabled(mod_name: str) -> bool:
    for info in utilities.get_mod_pak_info_list():
        if info['mod_name'] == mod_name:
            return True
    return False


def get_engine_pak_command() -> str:
    command_str = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{utilities.get_uproject_file()}" '
        f'-noP4 '
        f'-cook '
        f'-iterate '
        f'-stage '
        f'-pak '
    )
    return command_str


def get_cook_project_command() -> str:
    command_str = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{utilities.get_uproject_file()}" '
        f'-noP4 '
        f'-cook '
        f'-iterate '
        f'-skipstage '
        f'-nocompileeditor '
        f'-nodebuginfo'
    )
    return command_str


def cook_uproject():
    run_proj_command(get_cook_project_command())
 

def package_uproject():
    run_proj_command(get_engine_pak_command())   


def run_proj_command(command: str):
    os.chdir(utilities.get_unreal_engine_dir())
    os.system(command)


def make_mods():
    pre_packaging()
    pre_pak_creation()
    
    global queue_types

    if PackingType.ENGINE in queue_types:
        handle_engine_logic()
    if PackingType.UNREAL_PAK in queue_types:
        handle_unreal_pak_logic()
    if PackingType.REPAK in queue_types:
        handle_repak_logic()
    if PackingType.LOOSE in queue_types:
        handle_loose_logic()


def handle_engine_logic():
    pass


def handle_unreal_pak_logic():
    pass


def handle_repak_logic():
    pass


def handle_loose_logic():
    for mod_pak_info in utilities.get_mod_pak_info_list():
        if not mod_pak_info['is_enabled']:
            disable_mod(PackingType.LOOSE, mod_pak_info['mod_name'])
    for mod_pak_info in settings['mod_pak_info']: 
        if mod_pak_info['is_enabled']:
            enable_mod(PackingType.LOOSE, mod_pak_info['mod_name'])


def disable_loose_mod(mod_name: str):
    mod_files = utilities.get_mod_files(mod_name)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        file_to_remove = mod_files[key]
        if os.path.isfile(file_to_remove):
            os.remove(file_to_remove)

    for folder in set(os.path.dirname(file) for file in mod_files.values()):
         if os.path.exists(folder) and not os.listdir(folder):
             os.removedirs(folder)


def disable_engine_mod(mod_name: str):
    pass


def disable_repak_mod(mod_name: str):
    pass


def disable_unreal_pak_mod(mod_name: str):
    pass


def disable_mod(packing_type: PackingType, mod_name: str):
    if packing_type == PackingType.LOOSE:
        disable_loose_mod(mod_name)
    if packing_type == PackingType.ENGINE:
        disable_engine_mod(mod_name)
    if packing_type == PackingType.REPAK:
        disable_repak_mod(mod_name)
    if packing_type == PackingType.UNREAL_PAK:
        disable_unreal_pak_mod(mod_name)


def enable_loose_mod(mod_name: str):
    mod_files = utilities.get_mod_files(mod_name)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        before_file = key
        after_file = mod_files[key]
        dir = os.path.dirname(after_file)
        if not os.path.isdir(dir):
            os.makedirs(dir)
        print(f'before file: {before_file}')
        print(f'after file: {after_file}')
        shutil.copyfile(before_file, after_file)


def enable_engine_mod(mod_name: str):
    pass

def enable_repak_mod(mod_name: str):
    pass

def enable_unreal_pak_mod(mod_name: str):
    pass


def enable_mod(packing_type: PackingType, mod_name: str):
    if packing_type == PackingType.LOOSE:
        enable_loose_mod(mod_name)
    if packing_type == PackingType.ENGINE:
        enable_engine_mod(mod_name)
    if packing_type == PackingType.REPAK:
        enable_repak_mod(mod_name)
    if packing_type == PackingType.UNREAL_PAK:
        enable_unreal_pak_mod(mod_name)


def pre_packaging():
    ScriptState.set_script_state(ScriptStateType.PRE_PACKAGING)
    if not PackingType.ENGINE in queue_types:
        cook_uproject()
    post_packaging()


def post_packaging():
    ScriptState.set_script_state(ScriptStateType.POST_PACKAGING)


def pre_pak_creation():
    ScriptState.set_script_state(ScriptStateType.PRE_PAK_CREATION)
    if PackingType.ENGINE in queue_types:
        package_uproject()
    post_pak_creation()


def post_pak_creation():
    ScriptState.set_script_state(ScriptStateType.POST_PAK_CREATION)


def test_mods_all(mod_names: str):
    test_mods(mod_names)


def test_mods(mod_names):
    pass
