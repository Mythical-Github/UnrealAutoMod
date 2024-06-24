import sys
import os
from pathlib import Path
import shutil
import zipfile

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

src_dir = f'{os.path.dirname(os.path.dirname(SCRIPT_DIR))}/src'

base_path = Path(src_dir)
files_to_include = [
    base_path / "__main__.py",
    base_path / "cli.json",
    base_path / "cli.py",
    base_path / "engine.py",
    base_path / "enums.py",
    base_path / "epic.py",
    base_path / "game_runner.py",
    base_path / "packing.py",
    base_path / "script_states.py",
    base_path / "settings.py",
    base_path / "steam.py",
    base_path / "thread_constant.py",
    base_path / "thread_engine_monitor.py",
    base_path / "thread_game_monitor.py",
    base_path / "unreal_pak.py",
    base_path / "utilities.py",
    base_path / "windows.py"
]

pyinstaller_cmd = [
    "pyinstaller",
    "--noconfirm",
    "--onefile",
    "--console",
    f"--icon={base_path.parent / 'assets/images/UnrealAutoModIcon.ico'}"
]

for file_path in files_to_include:
    pyinstaller_cmd.append(f"--add-data={file_path};.")

command_string = " ".join(pyinstaller_cmd)

command = str(f'{src_dir}/__main__.py')

command_string = f'{command_string} "{command}"'

print(command_string)

os.system(command_string)

new_exe = f'{SCRIPT_DIR}/dist/__main__.exe'
assets_dir = os.path.dirname(SCRIPT_DIR)
old_exe = f'{assets_dir}/base/UnrealAutoModCLI.exe'
if os.path.isfile(old_exe):
    os.remove(old_exe)
if os.path.isfile(new_exe):
    shutil.copy(new_exe, old_exe)

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

import subprocess
subprocess.run(f'{SCRIPT_DIR}/cleanup.py')
