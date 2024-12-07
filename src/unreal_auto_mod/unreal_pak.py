import os
import shutil

from rich.progress import Progress

from unreal_auto_mod import gen_py_utils as general_utils
from unreal_auto_mod import packing, utilities
from unreal_auto_mod import ue_dev_py_utils as unreal_dev_utils
from unreal_auto_mod.enums import CompressionType, PackagingDirType
from unreal_auto_mod.main import SCRIPT_DIR
from unreal_auto_mod import gen_py_utils


def get_pak_dir_to_pack(mod_name: str):
    return f'{utilities.get_working_dir()}/{mod_name}'


def get_pak_dir_to_pack(mod_name: str) -> str:
    return f'{utilities.get_working_dir()}/{mod_name}'


def make_response_file(mod_name: str) -> str:
    file_list_path = os.path.join(utilities.get_working_dir(), f'{mod_name}_filelist.txt')
    dir_to_pack = get_pak_dir_to_pack(mod_name)
    with open(file_list_path, "w") as file:
        for root, _, files in os.walk(dir_to_pack):
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                if not os.path.isfile:
                    raise FileNotFoundError(f'The following file could not be found "{absolute_path}"')
                relative_path = os.path.relpath(root, dir_to_pack).replace("\\", "/")
                mount_point = f'../../../{relative_path}/'
                # file.write(f'"{absolute_path}" "{mount_point}"\n')
                file.write(f'"{os.path.normpath(absolute_path)}" "{mount_point}"\n')
    return file_list_path


# def make_response_file(mod_name: str) -> str:
#     file_list_path = os.path.normpath(os.path.join(utilities.get_working_dir(), f'{mod_name}_filelist.txt'))
    
#     file_list_content = r'''
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Content\Mods\TestMod\DA_TestMod.uasset" "../../../RoboQuest/Content/Mods/TestMod/"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Content\Mods\TestMod\DA_TestMod.uexp" "../../../RoboQuest/Content/Mods/TestMod/"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Content\Mods\TestMod\ModActor.uasset" "../../../RoboQuest/Content/Mods/TestMod/"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Content\Mods\TestMod\ModActor.uexp" "../../../RoboQuest/Content/Mods/TestMod/"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Content\Mods\TestMod\ModRoot\BP_TestMod.uasset" "../../../RoboQuest/Content/Mods/TestMod/ModRoot/"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Content\Mods\TestMod\ModRoot\BP_TestMod.uexp" "../../../RoboQuest/Content/Mods/TestMod/ModRoot/"
# '''

#     os.makedirs(os.path.dirname(file_list_path), exist_ok=True)
#     with open(file_list_path, "w") as file:
#         file.write(file_list_content)

#     return file_list_path

    


def get_iostore_commands_file_contents(mod_name: str, final_pak_file: str) -> str:
    chunk_utoc_path = f'{os.path.dirname(final_pak_file)}/{mod_name}-WindowsNoEditor.utoc'  # this can be different depending on ue4/5 or not deal with this later
    container_name = mod_name
    response_file = make_response_file(mod_name)
    commands_file_content = f'''-Output={os.path.normpath(chunk_utoc_path)}-ContainerName={container_name} -ResponseFile="{os.path.normpath(response_file)}"'''
    print(commands_file_content)
    return commands_file_content



    # global_utoc_path = f'{SCRIPT_DIR}/assets/iostore_packaging/global.utoc'
    # cooked_content_dir = f'{utilities.get_working_dir()}/{mod_name}'
    # crypto_keys_json = f'{SCRIPT_DIR}/assets/iostore_packaging/Crypto.json'


def make_iostore_unreal_pak_mod_checks(
        cooked_content_dir: str, 
        global_utoc_path: str, 
        crypto_keys_json: str, 
        commands_txt_path: str
    ):
        gen_py_utils.check_directory_exists(cooked_content_dir)
        gen_py_utils.check_file_exists(global_utoc_path)
        gen_py_utils.check_file_exists(crypto_keys_json)
        gen_py_utils.check_file_exists(commands_txt_path)


# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest"
# "C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\global.utoc"


def make_iostore_unreal_pak_mod(mod_name: str, final_pak_file: str):
        
        exe = unreal_dev_utils.get_editor_cmd_path(utilities.get_unreal_engine_dir())
        global_utoc_path = f'{utilities.get_uproject_dir()}/Saved/Cooked/WindowsNoEditor/RoboQuest/Content/Paks/global.utoc'
        cooked_content_dir = f'{utilities.get_uproject_dir()}/Saved/Cooked/WindowsNoEditor'
        
        commands_txt_content = get_iostore_commands_file_contents(mod_name, final_pak_file)
        commands_txt_path = f'{utilities.get_working_dir()}/iostore_packaging/{mod_name}_commands_list.txt'
        os.makedirs(os.path.dirname(commands_txt_path), exist_ok=True)
        with open(commands_txt_path, 'w') as file:
            file.write(commands_txt_content)
        crypto_keys_json = f'{utilities.get_uproject_dir()}/Saved/StagedBuilds/WindowsNoEditor/RoboQuest/Metadata/Crypto.json'

        make_iostore_unreal_pak_mod_checks(cooked_content_dir, global_utoc_path, crypto_keys_json, commands_txt_path)

        platform_string = unreal_dev_utils.get_win_dir_str(utilities.get_unreal_engine_dir())
        iostore_txt_location = f'{utilities.get_working_dir()}/iostore_packaging/{mod_name}_iostore.txt'
        default_engine_patch_padding_alignment = 2048
        args = [
            utilities.get_uproject_file(),
            '-run=IoStore',
            f'-CreateGlobalContainer={global_utoc_path}',
            f'-CookedDirectory={cooked_content_dir}',
            f'-Commands="{os.path.normpath(commands_txt_path)}"',
            f'-patchpaddingalign={default_engine_patch_padding_alignment}',
            f'-cryptokeys={crypto_keys_json}',
            f'-TargetPlatform={platform_string}',
            f'-abslog="{iostore_txt_location}"',
            f'-stdout',
            f'-CrashForUAT',
            f'-unattended',
            f'-NoLogTimes',
            f'-UTF8Output'
        ]
        utilities.run_app(exe_path=exe, args=args)


def make_non_iostore_unreal_pak_mod(
        exe_path: str, 
        intermediate_pak_file: str, 
        mod_name: str,
        compression_str: str,
        final_pak_file: str
    ):
    command = f'{exe_path} "{intermediate_pak_file}" -Create="{make_response_file(mod_name)}"'
    if compression_str != 'None':
        command = f'{command} -compress -compressionformat={compression_str}'
    utilities.run_app(command)
    if os.path.islink(final_pak_file):
        os.unlink(final_pak_file)
    if os.path.isfile(final_pak_file):
        os.remove(final_pak_file)
    os.symlink(intermediate_pak_file, final_pak_file)


def install_unreal_pak_mod(mod_name: str, compression_type: CompressionType):
    move_files_for_packing(mod_name)
    compression_str = CompressionType(compression_type).value
    from unreal_auto_mod import utilities
    output_pak_dir = f'{utilities.get_working_dir()}/{utilities.get_pak_dir_structure(mod_name)}'
    intermediate_pak_file = f'{utilities.get_working_dir()}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.pak'
    final_pak_file = f'{utilities.custom_get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}/{mod_name}.pak'
    os.makedirs(output_pak_dir, exist_ok=True)
    os.makedirs(f'{utilities.custom_get_game_paks_dir()}/{utilities.get_pak_dir_structure(mod_name)}', exist_ok=True)
    exe_path = unreal_dev_utils.get_unreal_pak_exe_path(utilities.get_unreal_engine_dir())
    from unreal_auto_mod import ue_dev_py_utils
    is_game_iostore = ue_dev_py_utils.get_is_game_iostore(utilities.get_uproject_file(), utilities.custom_get_game_dir())

    if is_game_iostore:
        make_iostore_unreal_pak_mod(mod_name, final_pak_file)
    else:
        make_non_iostore_unreal_pak_mod(
            exe_path, 
            intermediate_pak_file, 
            mod_name, 
            compression_str, 
            final_pak_file
        )



def move_files_for_packing(mod_name: str):
    mod_files_dict = packing.get_mod_file_paths_for_manually_made_pak_mods(mod_name)
    mod_files_dict = utilities.filter_file_paths(mod_files_dict)

    with Progress() as progress:
        task = progress.add_task(f"[green]Copying files for {mod_name} mod...", total=len(mod_files_dict))

        for before_file, after_file in mod_files_dict.items():
            if os.path.exists(after_file):
                if not general_utils.get_do_files_have_same_hash(before_file, after_file):
                    os.remove(after_file)
            elif not os.path.isdir(os.path.dirname(after_file)):
                os.makedirs(os.path.dirname(after_file))

            if os.path.isfile(before_file):
                shutil.copy2(before_file, after_file)

            progress.update(task, advance=1)
