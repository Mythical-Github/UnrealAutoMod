import os
import requests
import subprocess

import settings
import utilities
from log_py import log_py as log


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
        "5.4": "V11",
        "5.5": "V11"
    }
    return engine_version_to_repack_version[utilities.custom_get_unreal_engine_version(utilities.get_unreal_engine_dir())]


def get_repak_pak_version_str() -> str:
    if utilities.get_is_overriding_automatic_version_finding():
        repak_version_str = settings.settings['repak_info']['repak_version']
    elif utilities.get_should_ship_uproject_steps():
        repak_version_str = settings.settings['repak_info']['repak_version']
    else:
        repak_version_str = get_repak_version_str_from_engine_version()
    return repak_version_str


def get_latest_version_number(repository='trumank/repak'):
    api_url = f'https://api.github.com/repos/{repository}/releases/latest'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        release_data = response.json()
        version_number = release_data['tag_name'].lstrip('v')
        return version_number
    
    except requests.RequestException as e:
        log.log_message(f'Error: fetching release information: {e}')
        return None


def get_installed_version(executable_path):
    try:
        result = subprocess.run([executable_path, '--version'], capture_output=True, text=True, check=True)
        version_output = result.stdout.strip()
        version = version_output.split(' ')[-1]
        return version
    
    except subprocess.CalledProcessError as e:
        log.log_message(f'Error: retrieving installed version: {e}')
        return None
    except FileNotFoundError:
        log.log_message(f'Warning: Executable not found at {executable_path}')
        return None


def download_and_install_latest_version(repository='trumank/repak', install_path=None):
    latest_version = get_latest_version_number(repository)
    if not latest_version:
        log.log_message('Error: Could not retrieve the latest version number of Repak.')
        return
    
    if install_path is None:
        install_path = os.path.join(os.path.expanduser('~'), '.cargo', 'bin')
        
    installed_version = get_installed_version(os.path.join(install_path, 'repak.exe'))
    
    if installed_version == latest_version:
        log.log_message('The latest version of Repak is already installed.')
        return
    
    log.log_message(f'Updating Repak to the latest version {latest_version}...')
    log.log_message('Repak is from https://github.com/trumank/repak')
    log.log_message('and was worked on by https://github.com/trumank/repak/graphs/contributors')
    log.log_message('and is licensed here https://github.com/trumank/repak/blob/master/LICENSE-APACHE')
    log.log_message('and also licensed here https://github.com/trumank/repak/blob/master/LICENSE-MIT')


    api_url = f'https://api.github.com/repos/{repository}/releases/latest'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        release_data = response.json()
        asset = next((asset for asset in release_data['assets'] if asset['name'] == 'repak_cli-installer.ps1'), None)
        
        if asset is None:
            raise RuntimeError('Asset "repak_cli-installer.ps1" not found in the latest release.')
        
        asset_url = asset['browser_download_url']
        script_path = os.path.join(os.environ['TEMP'], 'repak_cli-installer.ps1')
        script_response = requests.get(asset_url)
        script_response.raise_for_status()
        
        with open(script_path, 'wb') as file:
            file.write(script_response.content)
        
        subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', script_path], check=True)
        
        log.log_message('Repak CLI installed successfully.')
    
    except requests.RequestException as e:
        log.log_message(f'Error fetching release information: {e}')
    except subprocess.CalledProcessError as e:
        log.log_message(f'Error executing the installer script: {e}')
    except RuntimeError as e:
        log.log_message(e)


def get_package_path():
    if utilities.get_is_using_repak_path_override():
        return utilities.get_repak_path_override()
    else:
        return os.path.join(os.path.expanduser('~'), '.cargo', 'bin', 'repak.exe')

if not utilities.get_is_using_repak_path_override():
    download_and_install_latest_version()
