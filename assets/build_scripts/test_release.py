import os
import sys

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

assets_dir = os.path.dirname(SCRIPT_DIR)
help_bat_file = f'{assets_dir}/base/help.bat'
if os.path.isfile(help_bat_file):
    os.system(help_bat_file)