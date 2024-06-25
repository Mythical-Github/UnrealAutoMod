import sys
import os
import shutil
import zipfile

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

BASE_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'base'))

new_exe = os.path.join(SCRIPT_DIR, 'dist', '__main__.exe')
unreal_auto_mod_dir = os.path.join(BASE_DIR, 'UnrealAutoMod')
unreal_auto_mod_zip = os.path.join(BASE_DIR, 'UnrealAutoMod.zip')

os.makedirs(unreal_auto_mod_dir, exist_ok=True)

for item in os.listdir(BASE_DIR):
    if item != 'UnrealAutoMod':
        item_path = os.path.join(BASE_DIR, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, unreal_auto_mod_dir)
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(unreal_auto_mod_dir, item))

with zipfile.ZipFile(unreal_auto_mod_zip, 'w') as zipf:
    for root, _, files in os.walk(unreal_auto_mod_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), unreal_auto_mod_dir))
