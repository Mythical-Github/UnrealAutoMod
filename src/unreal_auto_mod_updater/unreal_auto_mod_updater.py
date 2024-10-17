import os
import sys
import shutil
import zipfile
import requests
from pathlib import Path


script_name = os.path.basename(sys.executable) if getattr(sys, 'frozen', False) else os.path.basename(__file__)


if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parent
else:
    script_dir = Path(__file__).resolve().parent

BACKUP_DIR = os.path.join(script_dir, 'backup')
UPDATE_URL = 'https://github.com/Mythical-Github/UnrealAutoMod/releases/latest/download/UnrealAutoMod.zip'


def backup_files():

    backup_bak_dir = f'{BACKUP_DIR}.bak'
    
    if os.path.exists(BACKUP_DIR):
        os.rename(BACKUP_DIR, backup_bak_dir)


    os.makedirs(BACKUP_DIR)
    if os.path.exists(backup_bak_dir):
        shutil.move(backup_bak_dir, BACKUP_DIR)


    for item in os.listdir(script_dir):
        item_path = os.path.join(script_dir, item)
        
        if item != script_name and item != 'backup.bak':
            shutil.move(item_path, BACKUP_DIR)


def download_and_install():
    print(f'Downloading {UPDATE_URL}')
    response = requests.get(UPDATE_URL, stream=True)
    zip_path = os.path.join(script_dir, 'UnrealAutoMod.zip')
    with open(zip_path, 'wb') as f:
        f.write(response.content)


    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(script_dir)
    os.remove(zip_path)
    print(f'Installed new version in {script_dir}')


def main():
    backup_files()
    download_and_install()

if __name__ == '__main__':
    main()
