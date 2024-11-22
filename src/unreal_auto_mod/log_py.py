import os
from datetime import datetime
from shutil import get_terminal_size

from unreal_auto_mod.console import console
from unreal_auto_mod.log_info import LOG_INFO

log_base_dir = f'{os.getcwd()}/src'
log_prefix = ''


def set_log_base_dir(base_dir: str):
    global log_base_dir
    log_base_dir = base_dir


def configure_logging(colors_config):
    global log_prefix

    log_prefix = colors_config['log_name_prefix']

    log_dir = os.path.join(log_base_dir, 'logs')
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    rename_latest_log(log_dir)


def rename_latest_log(log_dir):
    latest_log_path = os.path.join(log_dir, f'{log_prefix}latest.log')
    if os.path.isfile(latest_log_path):
        try:
            timestamp = datetime.now().strftime('%m_%d_%Y_%H%M_%S')
            new_name = f'{log_prefix}{timestamp}.log'
            new_log_path = os.path.join(log_dir, new_name)

            counter = 1
            while os.path.isfile(new_log_path) or is_file_in_use(latest_log_path):
                new_name = f'{log_prefix}{timestamp}_({counter}).log'
                new_log_path = os.path.join(log_dir, new_name)
                counter += 1

            os.rename(latest_log_path, new_log_path)

        except PermissionError as e:
            log_message(f"Error renaming log file: {e}")
            return


def is_file_in_use(file_path):
    try:
        with open(file_path, 'a'):
            return False
    except OSError:
        return True


def log_message(message: str):
    color_options = LOG_INFO.get('theme_colors')
    default_background_color = LOG_INFO.get('background_color')
    default_background_color = f"rgb({default_background_color[0]},{default_background_color[1]},{default_background_color[2]})"

    default_text_color = LOG_INFO.get('default_color')
    default_text_color = f"rgb({default_text_color[0]},{default_text_color[1]},{default_text_color[2]})"
    terminal_width = get_terminal_size().columns
    padded_message = (message[:terminal_width] if len(message) > terminal_width else message.ljust(terminal_width))

    for keyword, color in color_options.items():
        if keyword in padded_message:
            rgb_color = f"rgb({color[0]},{color[1]},{color[2]})"
            console.print(padded_message, style=f'{rgb_color} on {default_background_color}')
            break
    else:
        console.print(padded_message, style=f'{default_text_color} on {default_background_color}')

    log_dir = os.path.join(log_base_dir, 'logs')
    log_path = os.path.join(log_dir, f'{log_prefix}latest.log')

    if os.path.isfile(log_path):
        with open(log_path, 'a') as log_file:
            log_file.write(f"{padded_message}\n")
