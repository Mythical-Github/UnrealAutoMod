import os
import sys
import json
import logging
from datetime import datetime
from shutil import get_terminal_size
from colorama import Fore, Style, init

init(autoreset=True)

logger = logging.getLogger(__name__)


log_base_dir = f'{os.getcwd()}/src'

colors_json_path = f'{log_base_dir}/log_colors.json'

colors_config = ''
theme_colors = ''
default_color = ''
background_color = ''
log_prefix = ''


has_configured_logging = False


def module_setup():
    return


def set_log_base_dir(base_dir: str):
    global log_base_dir
    log_base_dir = base_dir


def set_colors_json_path(json_path: str):
    global colors_json_path
    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        json_filename = os.path.basename(json_path)
        colors_json_path = os.path.join(base_path, json_filename)
    else:
        colors_json_path = json_path


def load_theme_colors():
    if not os.path.isfile(colors_json_path):
        raise FileNotFoundError(f"Theme colors file not found: {colors_json_path}")
    with open(colors_json_path, 'r') as f:
        return json.load(f)


def configure_logging():

    global colors_config
    global theme_colors
    global default_color
    global background_color
    global log_prefix

    colors_config = load_theme_colors()
    theme_colors = colors_config.get('theme_colors', {})
    default_color = colors_config['default_color']
    background_color = colors_config['background_color']
    log_prefix = colors_config['log_name_prefix']

    log_dir = os.path.join(log_base_dir, 'logs')
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    rename_latest_log(log_dir)

    original_path = os.path.join(log_dir, 'latest.log')

    global inter_log
    inter_log = original_path

    log_file = inter_log

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(message)s'))

    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


def log_message(message: str):
    global has_configured_logging
    if not has_configured_logging:
        configure_logging()
        has_configured_logging = True
    logger.info(message)
    color = default_color
    for keyword, assigned_color in theme_colors.items():
        if keyword in message:
            color = assigned_color
            break
    terminal_width = get_terminal_size().columns
    padded_message = (message[:terminal_width] if len(message) > terminal_width else message.ljust(terminal_width))
    print(f"{background_color}{color}{padded_message}{Style.RESET_ALL}")



def rename_latest_log(log_dir):
    latest_log_path = os.path.join(log_dir, 'latest.log')
    if os.path.isfile(latest_log_path):
        try:
            timestamp = datetime.now().strftime('%m_%d_%Y_%H%M_%S')
            new_name = f'{log_prefix}{timestamp}.log'
            new_log_path = os.path.join(log_dir, new_name)
            os.rename(latest_log_path, new_log_path)
        except PermissionError as e:
            log_message(f"Error renaming log file: {e}")
            return
