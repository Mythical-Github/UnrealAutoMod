import os
import sys
import subprocess

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

scripts_to_run = [
    "cleanup.py",
    "build.py",
    "cleanup.py"
]

for script in scripts_to_run:
    script_path = os.path.join(SCRIPT_DIR, script)
    subprocess.run(["python", script_path])

exit()
