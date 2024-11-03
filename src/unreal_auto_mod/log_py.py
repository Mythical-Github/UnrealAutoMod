import os
import logging
from datetime import datetime
from shutil import get_terminal_size
from colorama import Style, init

init(autoreset=True)

logger = logging.getLogger(__name__)

log_base_dir = f'{os.getcwd()}/src'

theme_colors = ''
default_color = ''
background_color = ''
log_prefix = ''


class FlushFileHandler(logging.FileHandler):
    """Custom FileHandler that flushes after every write."""
    def emit(self, record):
        super().emit(record)
        self.flush()  # Ensures log is written immediately


def module_setup():
    return


def set_log_base_dir(base_dir: str):
    global log_base_dir
    log_base_dir = base_dir


def configure_logging(colors_config):
    global theme_colors
    global default_color
    global background_color
    global log_prefix

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

    # Use FlushFileHandler to ensure immediate writes
    file_handler = FlushFileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(message)s'))

    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


def log_message(message: str):
    logger.info(message)
    color = default_color
    for keyword, assigned_color in theme_colors.items():
        if keyword in message:
            color = assigned_color
            break
    terminal_width = get_terminal_size().columns
    padded_message = (message[:terminal_width] if len(message) > terminal_width else message.ljust(terminal_width))
    print(f"{background_color}{color}{padded_message}{Style.RESET_ALL}")

    # Ensure file is flushed and available immediately
    if hasattr(logger.handlers[0], 'flush'):
        logger.handlers[0].flush()


def rename_latest_log(log_dir):
    latest_log_path = os.path.join(log_dir, 'latest.log')
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
    except IOError:
        return True