import os
import logging
from datetime import datetime
from colorama import Fore, Style, init
import settings

init(autoreset=True)

logger = logging.getLogger(__name__)

theme_colors = {
    'Arg:': Fore.CYAN,
    'Args:': Fore.CYAN,
    'Function:': Fore.GREEN,
    'Routine Check:': Fore.YELLOW,
    'Script State:': Fore.MAGENTA,
    'Thread:': Fore.BLUE,
    'Process:': Fore.YELLOW,
    'Window:': Fore.LIGHTMAGENTA_EX,
    'Error:': Fore.RED + Style.BRIGHT,
    'Monitor:': Fore.LIGHTYELLOW_EX,
    'Progress Bar:': Fore.LIGHTCYAN_EX
}
default_color = Fore.LIGHTBLUE_EX

class ColorfulHandler(logging.StreamHandler):
    def format(self, record):
        log_entry = super().format(record)
        color = default_color

        for keyword, assigned_color in theme_colors.items():
            if keyword in log_entry:
                color = assigned_color
                break

        return f"{color}{log_entry}{Style.RESET_ALL}"

def configure_logging():
    log_dir = os.path.join(settings.SCRIPT_DIR, 'logs')
    timestamp = datetime.now().strftime('%m_%d_%Y_%H%M')
    log_file = os.path.join(log_dir, f'unreal_auto_mod_{timestamp}.log')
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

def log_message(message: str):
    logger.info(message)
    color = default_color
    for keyword, assigned_color in theme_colors.items():
        if keyword in message:
            color = assigned_color
            break
    print(f"{color}{message}{Style.RESET_ALL}")

configure_logging()