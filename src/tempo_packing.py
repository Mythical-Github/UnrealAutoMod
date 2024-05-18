import os
from tempo_enums import PackingType
from tempo_settings import settings


def get_base_command():
    output_dir = settings['general_info']['output_dir']
    uproject = settings['engine_info']['unreal_project_file']
    command_str = (
        f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun '
        f'-project="{uproject}" '
        f'-noP4 '
        f'-platform=Win64 '
        f'-clientconfig=Development '
        f'-serverconfig=Development '
        f'-cook '
        f'-allmaps '
        f'-stage '
        f'-archive '
        f'-archivedirectory="{output_dir}"'
    )
    return command_str


def cook_uproject():
    command = get_base_command()
    run_proj_command(command)
 

def package_uproject():
    command = f'{get_base_command()} -pak'
    run_proj_command(command)   


def run_proj_command(command):
    engine_dir = settings['engine_info']['unreal_engine_dir']
    os.chdir(engine_dir)
    os.system(command)


def test_mods_all(mod_names):
    test_mods(mod_names)


def test_mods(mod_names):
    pass


def make_mod(packing_type_enum):
    if packing_type_enum == PackingType.ENGINE:
        handle_engine_logic()
    elif packing_type_enum == PackingType.UNREAL_PAK:
        handle_unreal_pak_logic()
    elif packing_type_enum == PackingType.REPAK:
        handle_repak_logic()
    elif packing_type_enum == PackingType.LOOSE:
        handle_loose_logic()
    elif packing_type_enum == PackingType.ALT_EXE:
        handle_alt_exe_logic()
    else:
        raise ValueError('Unsupported packing_type specified in the settings.json')


def handle_engine_logic():
    pass


def handle_unreal_pak_logic():
    pass


def handle_repak_logic():
    pass


def handle_loose_logic():
    pass


def handle_alt_exe_logic():
    pass
        

def make_pak_repak():
    pass


def make_pak_unreal_pak():
    pass


def move_paks_repak():
    pass


def move_paks_unreal_pak():
    pass


def move_loose_file_mods():
    pass


def move_engine_made_paks():
    pass


def cleanup_disabled_mods():
    pass


def cleanup_output_dir():
    pass
