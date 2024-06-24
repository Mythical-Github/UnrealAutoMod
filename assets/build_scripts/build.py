import sys
import os
from pathlib import Path
import shutil

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
    "--collect-data grapheme",
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
