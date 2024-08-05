import os
import sys
import json
import subprocess


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(sys.executable)
else:
    SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))

SETTINGS_JSON = f'{SCRIPT_DIR}/main_machine_settings.json'


def load_settings(settings_file):
    with open(settings_file, 'r') as file:
        settings = json.load(file)
    return settings


SETTINGS = load_settings(SETTINGS_JSON)


def get_mods_dir():
    return SETTINGS['mods_dir']


def get_client():
    return f'{SCRIPT_DIR}/main_machine.py'


def get_files_in_tree_dir_alt(root_dir):
    files_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files_list.append(file_path)
    return files_list


def send_command():
    executable = get_client()
    args = get_files_in_tree_dir_alt(get_mods_dir())
    command = ["python", executable] + args
    subprocess.run(command)


def send_mods():
    send_command()


if __name__ == "__main__":
    send_mods()
