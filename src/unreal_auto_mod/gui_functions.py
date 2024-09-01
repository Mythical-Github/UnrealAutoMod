import os
import enums
import shutil
import zipfile
import settings
import requests
import utilities
import game_runner


def unzip_zip(zip_path: str, output_location: str):
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_location)


def download_file(url: str, download_path: str):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


def open_dir_in_file_browser(input_directory: str):
    os.system(f'explorer {input_directory}')


def open_website(input_url: str):
    os.system(f'start {input_url}')


def get_uproject_dir():
    return os.path.dirname(utilities.get_uproject_file())


def get_uproject_unreal_auto_mod_dir():
    return f'{get_uproject_dir()}/Plugins/UnrealAutoMod'


def get_uproject_unreal_auto_mod_resources_dir():
    return f'{get_uproject_unreal_auto_mod_dir()}/Resources'


def open_file_in_default(file_path: str):
    os.system(f'start {file_path}')


def get_persistent_mods_dir() -> str:
    return f'{settings.settings_json_dir}/mod_packaging/persistent_files'


# -----------------------------------------------------------------


def get_fmodel_path() -> str:
    return f'{get_uproject_unreal_auto_mod_resources_dir()}/FModel/FModel.exe'


def install_fmodel():
    zip_path = f'{utilities.get_working_dir()}/FModel.zip'
    install_dir = f'{get_uproject_unreal_auto_mod_resources_dir()}/FModel'
    unzip_zip(zip_path, install_dir)


def download_fmodel():
    url = 'https://github.com/4sval/FModel/releases/latest/download/FModel.zip'
    download_path = f'{utilities.get_working_dir()}/FModel.zip'
    download_file(url, download_path)


def get_umodel_path() -> str:
    return f'{get_uproject_unreal_auto_mod_resources_dir()}/UModel/umodel_64.exe'


def install_umodel():
    zip_path = f'{utilities.get_working_dir()}/umodel_win32.zip'
    install_dir = f'{get_uproject_unreal_auto_mod_resources_dir()}/UModel'
    unzip_zip(zip_path, install_dir)


def download_umodel():
    url = 'https://www.gildor.org/down/47/umodel/umodel_win32.zip'
    download_path = f'{utilities.get_working_dir()}/umodel_win32.zip'
    download_file(url, download_path)


def get_kismet_analyzer_path() -> str:
    return f'{get_uproject_unreal_auto_mod_resources_dir()}/kismet-analyzer/kismet-analyzer.exe'


def install_kismet_analyzer():
    zip_path = f'{utilities.get_working_dir()}/kismet-analyzer-ba3dad5-win-x64.zip'
    install_dir = f'{get_uproject_unreal_auto_mod_resources_dir()}/kismet-analyzer'
    unzip_zip(zip_path, install_dir)


def download_kismet_analyzer():
    url = "https://github.com/trumank/kismet-analyzer/releases/download/latest/kismet-analyzer-ba3dad5-win-x64.zip"
    download_path = f'{utilities.get_working_dir()}/kismet-analyzer-ba3dad5-win-x64.zip'
    download_file(url, download_path)


def get_ide_path():
    return settings.settings['optionals']['ide_path']


def get_blender_path():
    return settings.settings['optionals']['blender_path']


def get_uasset_gui_path() -> str:
    return f'{get_uproject_unreal_auto_mod_resources_dir()}/UAssetGUI/UAssetGUI.exe'


def install_uasset_gui():
    exe_path = f'{utilities.get_working_dir()}/UAssetGUI.exe'
    install_dir = f'{get_uproject_unreal_auto_mod_resources_dir()}/UAssetGUI'
    os.makedirs(install_dir, exist_ok=True)
    shutil.move(exe_path, f'{install_dir}/UAssetGUI.exe')


def download_uasset_gui():
    url = "https://github.com/atenfyr/UAssetGUI/releases/latest/download/UAssetGUI.exe"
    download_path = f'{utilities.get_working_dir()}/UAssetGUI.exe'
    download_file(url, download_path)


def does_umodel_exist() -> bool:
    return os.path.isfile(get_umodel_path())


def does_fmodel_exist() -> bool:
    return os.path.isfile(get_fmodel_path())


def does_kismet_analyzer_exist() -> bool:
    return os.path.isfile(get_kismet_analyzer_path())


def does_uasset_gui_exist() -> bool:
    return os.path.isfile(f"{get_uproject_unreal_auto_mod_resources_dir()}/UAssetGUI/UAssetGUI.exe")


def download_spaghetti():
    url = 'https://github.com/bananaturtlesandwich/spaghetti/releases/latest/download/spaghetti.exe'
    download_path = f"{utilities.get_working_dir()}/spaghetti.exe"
    download_file(url, download_path)


def download_stove():
    url = 'https://github.com/bananaturtlesandwich/stove/releases/latest/download/stove.exe'
    download_path = f"{utilities.get_working_dir()}/stove.exe"
    download_file(url, download_path)


def get_spaghetti_path() -> str:
    return f"{get_uproject_unreal_auto_mod_resources_dir()}/spaghetti/spaghetti.exe"


def does_spaghetti_exist() -> bool:
    return os.path.isfile(get_spaghetti_path())


def get_stove_path() -> str:
    return f"{get_uproject_unreal_auto_mod_resources_dir()}/stove/stove.exe"


def does_stove_exist() -> bool:
    return os.path.isfile(get_stove_path())


def install_stove():
    exe_path = f'{utilities.get_working_dir()}/stove.exe'
    install_dir = f'{get_uproject_unreal_auto_mod_resources_dir()}/stove'
    os.makedirs(install_dir, exist_ok=True)
    shutil.move(exe_path, f'{install_dir}/stove.exe')


def install_spaghetti():
    exe_path = f'{utilities.get_working_dir()}/spaghetti.exe'
    install_dir = f'{get_uproject_unreal_auto_mod_resources_dir()}/spaghetti'
    os.makedirs(install_dir, exist_ok=True)
    shutil.move(exe_path, f'{install_dir}/spaghetti.exe')


# =======================================


def open_stove():
    if not os.path.isfile(get_stove_path()):
        install_stove()
    utilities.run_app(get_stove_path(), enums.ExecutionMode.ASYNC)


def open_spaghetti():
    if not os.path.isfile(get_spaghetti_path()):
        install_spaghetti()
    utilities.run_app(get_spaghetti_path(), enums.ExecutionMode.ASYNC)


def open_kismet_analyzer():
    # add shell stuff to run app later or something
    if not os.path.isfile(get_kismet_analyzer_path()):
        install_kismet_analyzer()
    import subprocess
    subprocess.run([get_kismet_analyzer_path(), '-h'], shell=True)


def open_ide():
    open_file_in_default(get_ide_path())


def open_blender():
    open_file_in_default(get_blender_path())


def open_uasset_gui():
    if not os.path.isfile(get_uasset_gui_path()):
        install_uasset_gui()
    utilities.run_app(get_uasset_gui_path(), enums.ExecutionMode.ASYNC)


def open_latest_log():
    file_to_open = f'{get_uproject_unreal_auto_mod_resources_dir()}/UnrealAutoMod/logs/latest.log'
    open_file_in_default(file_to_open)


def open_settings_json():
    open_file_in_default(settings.settings_json)


def run_game():
    game_runner.run_game()


def open_downloads_dir():
    downloads_dir = f"{os.path.expanduser('~')}/Downloads"
    open_dir_in_file_browser(downloads_dir)


def open_unreal_auto_mod_dir():
    open_dir_in_file_browser(get_uproject_unreal_auto_mod_dir())


def open_game_dir():
    open_dir_in_file_browser(utilities.custom_get_game_dir())


def open_game_binaries_dir():
    open_dir_in_file_browser(os.path.dirname(utilities.get_game_exe_path()))


def open_game_paks_dir():
    open_dir_in_file_browser(utilities.custom_get_game_paks_dir())


def open_uproject_dir():
    open_dir_in_file_browser(get_uproject_dir())


def open_umodel():
    if not os.path.isfile(get_umodel_path()):
        install_umodel()
    utilities.run_app(get_umodel_path(), exec_mode=enums.ExecutionMode.ASYNC)


def open_unreal_docs_website():
    open_website('https://dev.epicgames.com/documentation/en-us/unreal-engine/')


def open_google_website():
    open_website('https://www.google.com/')


def open_youtube_website():
    open_website('https://www.youtube.com/')


def open_github_website():
    open_website('https://github.com/')


def open_persistent_mods_dir():
    open_dir_in_file_browser(get_persistent_mods_dir())


def open_fmodel():
    if not os.path.isfile(get_fmodel_path()):
        install_fmodel()
    utilities.run_app(get_fmodel_path(), exec_mode=enums.ExecutionMode.ASYNC)
