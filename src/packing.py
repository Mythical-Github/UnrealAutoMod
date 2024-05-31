import os
import shutil
import utilities
from settings import settings
from script_states import ScriptState
from enums import PackingType, ScriptStateType, CompressionType, get_enum_from_val


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


def get_is_mod_installed(mod_name: str) -> bool:
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


def handle_logic(packing_type: PackingType):
    for mod_pak_info in utilities.get_mod_pak_info_list():
            if not mod_pak_info['is_enabled']:
                uninstall_mod(packing_type, mod_pak_info['mod_name'])
    for mod_pak_info in settings['mod_pak_info']: 
        if mod_pak_info['is_enabled']:
            install_mod(packing_type, mod_pak_info['mod_name'], get_enum_from_val(CompressionType, mod_pak_info['compression_type']))


def make_mods():
    pre_packaging()
    pre_pak_creation()
    
    global queue_types
    for queue_type in queue_types:
        handle_logic(queue_type)


def uninstall_loose_mod(mod_name: str):
    mod_files = utilities.get_mod_files(mod_name)
    dict_keys = mod_files.keys()
    for key in dict_keys:
        file_to_remove = mod_files[key]
        if os.path.isfile(file_to_remove):
            os.remove(file_to_remove)

    for folder in set(os.path.dirname(file) for file in mod_files.values()):
         if os.path.exists(folder) and not os.listdir(folder):
             os.removedirs(folder)


def uninstall_pak_mod(mod_name: str):
    extensions = ['pak']
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


def install_engine_mod(mod_name: str, compression_type: CompressionType):
    pass


def install_repak_mod(mod_name: str, compression_type: CompressionType):
    pass


def install_unreal_pak_mod(mod_name: str, compression_type: CompressionType):
    pass


def install_mod(packing_type: PackingType, mod_name: str, compression_type: CompressionType):
    if packing_type == PackingType.LOOSE:
        install_loose_mod(mod_name)
    if packing_type == PackingType.ENGINE:
        install_engine_mod(mod_name, compression_type)
    if packing_type == PackingType.REPAK:
        install_repak_mod(mod_name, compression_type)
    if packing_type == PackingType.UNREAL_PAK:
        install_unreal_pak_mod(mod_name, compression_type)


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
