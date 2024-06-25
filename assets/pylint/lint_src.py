import os
import sys
import subprocess


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


def run_pylint_on_directory(directory):
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Running pylint on {file_path}")
                result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
                print(result.stdout)
                print(result.stderr)

src_directory = f'{os.path.dirname(os.path.dirname(SCRIPT_DIR))}/src'
run_pylint_on_directory(src_directory)
