import sys
from pathlib import Path

from python_logging import log
from cli_py import cli


if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parent
else:
    script_dir = Path(__file__).resolve().parent


if __name__ == "__main__":
    
    try:
        log.set_colors_json_path(f'{script_dir}/json/log_colors.json')
        log.configure_logging()
        cli.set_json_location(f'{script_dir}/json/cli.json')
        cli.cli_logic()
    except Exception as error_message:
        log.log_message(str(error_message))     
