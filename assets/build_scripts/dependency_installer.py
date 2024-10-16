import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}: {e.cmd}", file=sys.stderr)
        print(e.output, file=sys.stderr)
        print(e.stderr, file=sys.stderr)


def main():
    commands = [
        "pip uninstall log_py -y",
        "pip uninstall cli_py -y",
        "pip uninstall ue_dev_py_utils -y",
        "pip uninstall win_man_py -y",
        "pip uninstall gen_py_utils -y",
        "pip uninstall pyjson5 -y",
        "pip uninstall alive_progress -y",
        "pip uninstall pyinstaller -y"
        "pip install alive_progress",
        "pip install pyjson5",
        "pip install pyinstaller",
        "pip install git+https://github.com/Mythical-Github/log_py.git",
        "pip install git+https://github.com/Mythical-Github/cli_py.git",
        "pip install git+https://github.com/Mythical-Github/ue_dev_py_utils.git",
        "pip install git+https://github.com/Mythical-Github/win_man_py.git",
        "pip install git+https://github.com/Mythical-Github/gen_py_utils.git"
    ]

    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()
