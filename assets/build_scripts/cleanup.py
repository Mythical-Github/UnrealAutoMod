import os
import sys
import shutil


# delete old zips
# delete old log dirs
# "C:\Users\Mythical\Documents\GitHub\UnrealAutoModDevWorkSpace\UnrealAutoMod\assets\base\UnrealAutoMod.zip"
# "C:\Users\Mythical\Documents\GitHub\UnrealAutoModDevWorkSpace\UnrealAutoMod\assets\base\logs"


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

BASE_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'base'))

build_scripts_dir = os.path.dirname(SCRIPT_DIR)

cleanup_list = {
f'{SCRIPT_DIR}/dist',
f'{SCRIPT_DIR}/build',
f'{SCRIPT_DIR}/__main__.spec',
f'{BASE_DIR}/UnrealAutoMod',
f'{BASE_DIR}/logs',
f'{BASE_DIR}/UnrealAutoMod.zip'
f''
}

for entry in cleanup_list:
    if os.path.isfile(entry):
        os.remove(entry)
    if os.path.isdir(entry):
        shutil.rmtree(entry)
