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

# UPDATE THIS LATER

def main():
    commands = [
        "pip uninstall python_logging -y",
        "pip uninstall cli_py -y",
        "pip uninstall unreal_engine_development_python_utilities -y",
        "pip uninstall python_window_management -y",
        "pip uninstall general_python_utilities -y",
        "pip install git+https://github.com/Mythical-Github/python_logging.git",
        "pip install git+https://github.com/Mythical-Github/cli_py.git",
        "pip install git+https://github.com/Mythical-Github/unreal_engine_development_python_utilities.git",
        "pip install git+https://github.com/Mythical-Github/python_window_management.git",
        "pip install git+https://github.com/Mythical-Github/general_python_utilities.git"
    ]

    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()
