import os
import sys
import shutil

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

new_exe = f'{SCRIPT_DIR}/dist/__main__.exe'
assets_dir = os.path.dirname(SCRIPT_DIR)
old_exe = f'{assets_dir}/base/UnrealAutoModCLI.exe'
if os.path.isfile(old_exe):
    os.remove(old_exe)
if os.path.isfile(new_exe):
    shutil.copy(new_exe, old_exe)
