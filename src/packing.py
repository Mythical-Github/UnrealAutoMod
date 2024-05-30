import os
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


def set_packing_type_true(packing_type_enum: PackingType):
    global queue_type_check_dict
    if packing_type_enum in queue_type_check_dict:
        queue_type_check_dict[packing_type_enum] = True
    else:
        raise ValueError(f'{packing_type_enum} is not a valid packing type')


def get_engine_pak_command() -> str:
    command_str = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{settings['engine_info']['unreal_project_file']}" '
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
        f'-project="{settings['engine_info']['unreal_project_file']}" '
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
    os.chdir(settings['engine_info']['unreal_engine_dir'])
    os.system(command)


def test_mods_all(mod_names: str):
    test_mods(mod_names)


def test_mods(mod_names):
    pass


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
    from utilities import is_game_ue4
    win_dir_type = 'Windows'
    if is_game_ue4():
        win_dir_type = f'{win_dir_type}NoEditor'
    uproject_file = settings['engine_info']['unreal_project_file']
    uproject_name = os.path.splitext(os.path.basename(uproject_file))[0]
    uproject_file_dir = os.path.dirname(uproject_file)

    for mod_pak_info in settings['mod_pak_info']:
        manually_specified_asset_paths = mod_pak_info['manually_specified_assets']['asset_paths']
        for asset in manually_specified_asset_paths:
            print(f'{uproject_file_dir}/Saved/Cooked/{win_dir_type}/{uproject_name}/{asset}')
        
        manually_specified_tree_paths = mod_pak_info['manually_specified_assets']['tree_paths']
        for tree in manually_specified_tree_paths:
            print(f'{uproject_file_dir}/Saved/Cooked/{win_dir_type}/{uproject_name}/{tree}')


def handle_alt_exe_logic():
    pass
        

def make_pak_repak():
    pass


def make_pak_unreal_pak():
    pass


def move_loose_file_mods():
    pass


def move_engine_made_paks():
    pass


def cleanup_disabled_mods():
    pass


def cleanup_output_dir():
    pass


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
