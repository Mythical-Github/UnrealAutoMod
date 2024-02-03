import os
import sys
import subprocess
import shutil
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

output_dir = f"{SCRIPT_DIR}/output"
destination_path = f"{output_dir}/Tempo"

main_py = "../../python_project/Tempo/main.py"
gui_py = "../../python_project/Tempo/gui.py"


files_to_delete = [
  f"{SCRIPT_DIR}/build",
  f"{SCRIPT_DIR}/main.spec",
  f"{SCRIPT_DIR}/gui.spec",
  f"{SCRIPT_DIR}/../../unreal_project/4_22_VictoryPlugin/Tools/Tempo",
  f"{SCRIPT_DIR}/../../unreal_project/4_23+/Tools/Tempo"
]

if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)

subprocess.run(f"pyinstaller --onefile --distpath {destination_path} {main_py}")

subprocess.run(f"pyinstaller --onefile --distpath {destination_path} {gui_py}")

before_exe = f"{destination_path}/gui.exe"
after_exe = f"{destination_path}/TempoGUI.exe"

shutil.move(before_exe, after_exe)

before_exe = f"{destination_path}/main.exe"
after_exe = f"{destination_path}/TempoCLI.exe"

shutil.move(before_exe, after_exe)

before_exe = "../../python_project/Tempo/run_tempo_cli.bat"
after_exe = f"{destination_path}/run_tempo_cli.bat"

shutil.copy(before_exe, after_exe)

before_presets = f"{SCRIPT_DIR}/../../assets/presets"
after_presets = f"{destination_path}/presets"

shutil.copytree(before_presets, after_presets)

before_settings_json = f"{SCRIPT_DIR}/../../assets/settings.json"
after_settings_json = f"{destination_path}/settings.json"

shutil.copy(before_settings_json, after_settings_json)

for file_to_delete in files_to_delete:
    if os.path.isdir(file_to_delete):
        shutil.rmtree(file_to_delete)
    if os.path.isfile(file_to_delete):
        os.remove(file_to_delete)

gui_exe = f"{destination_path}/TempoGUI.exe"

old_tempo_dir = f"{SCRIPT_DIR}/../../unreal_project/4_22_VictoryPlugin/Tools/Tempo"

shutil.copytree(destination_path, old_tempo_dir)

old_tempo_dir = f"{SCRIPT_DIR}/../../unreal_project/4_23+/Tools/Tempo"

shutil.copytree(destination_path, old_tempo_dir)

subprocess.Popen(gui_exe)

release_dir = f"{SCRIPT_DIR}/output/Tempo"

if not os.path.isdir(release_dir):
    os.mkdir(release_dir)

shutil.make_archive(destination_path, "zip", release_dir)

sys.exit()
