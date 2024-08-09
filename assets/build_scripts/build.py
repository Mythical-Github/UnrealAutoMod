import sys
import os
from pathlib import Path

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

src_dir = f'{os.path.dirname(os.path.dirname(SCRIPT_DIR))}/src/unreal_auto_mod'

base_path = Path(src_dir)
files_to_include = [
    base_path / "json/cli.json",
    base_path / "json/log_colors.json",
    base_path / "__init__.py",
    base_path / "engine.py",
    base_path / "enums.py",
    base_path / "game_runner.py",
    base_path / "mods.py",
    base_path / "packing.py",
    base_path / "repak_utilities.py",
    base_path / "script_states.py",
    base_path / "settings.py",
    base_path / "thread_constant.py",
    base_path / "thread_engine_monitor.py",
    base_path / "thread_game_monitor.py",
    base_path / "unreal_pak.py",
    base_path / "utilities.py"
]

pyinstaller_cmd = [
    'pyinstaller',
    '--collect-data grapheme',
    '--collect-submodules "psutil"',
    '--collect-submodules "python_window_management"',
    '--collect-submodules "unreal_engine_development_python_utilities"',
    '--collect-submodules "alive_progress"',
    '--collect-submodules "requests"',
    '--noconfirm',
    '--onefile',
    '--console',
    f"--icon={base_path.parent.parent / 'assets/images/UnrealAutoModIcon.ico'}"
]

for file_path in files_to_include:
    pyinstaller_cmd.append(f"--add-data={file_path};.")

command_string = " ".join(pyinstaller_cmd)

command = str(f'{src_dir}/__main__.py')

command_string = f'{command_string} "{command}"'

print(command_string)

os.system(command_string)
