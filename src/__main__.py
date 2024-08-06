import sys
from pathlib import Path

from cli_py import cli
from python_logging import log


if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parent
else:
    script_dir = Path(__file__).resolve().parent


if __name__ == "__main__":
    try:
        log.set_log_base_dir(script_dir)
        log.set_colors_json_path(f'{script_dir}/json/log_colors.json')
        cli.set_json_location(f'{script_dir}/json/cli.json')
        cli.cli_logic()
    except Exception as error_message:
        log.log_message(str(error_message))     
