import os
import logging
from datetime import datetime
from shutil import get_terminal_size
from colorama import Fore, Style, init
import settings

init(autoreset=True)

logger = logging.getLogger(__name__)

theme_colors = {
    'Error': Fore.RED + Style.BRIGHT,  # Red
    'Warning': Fore.YELLOW + Style.BRIGHT,  # Yellow
    'Arg:': '\033[38;2;255;105;180m',  # Hot Pink
    'Args:': '\033[38;2;181;92;9m',    # Orange
    'Function:': '\033[38;2;0;255;0m',  # Lime
    'Routine Check:': '\033[38;2;138;43;226m',  # Blue Violet
    'Script State:': '\033[38;2;0;206;209m',  # Dark Turquoise
    'Thread:': '\033[38;2;255;140;0m', # Dark Orange
    'Process:': '\033[38;2;255;20;147m',  # Deep Pink
    'Window:': '\033[38;2;255;165;0m',  # Light Orange
    'Monitor:': '\033[38;2;173;216;230m',  # Light Blue
    'Progress Bar:': '\033[38;2;144;238;144m',  # Light Green
    'Packed': '\033[38;2;218;112;214m',  # Orchid
    'Command:': '\033[38;2;255;182;193m',  # Light Pink
    'FGlobal': '\033[38;2;32;178;170m',  # Light Sea Green
    'LogTemp:': '\033[38;2;255;228;181m',  # Moccasin
    'LogCook: Display:': '\033[38;2;123;104;238m',  # Medium Slate Blue
    'LogCookCommandlet: Display:': '\033[38;2;135;206;250m',  # Light Sky Blue
    'LogInit': '\033[38;2;238;130;238m'  # Violet
}

default_color = Fore.LIGHTBLUE_EX

background_color = '\033[48;2;40;42;54m'


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
    terminal_width = get_terminal_size().columns
    padded_message = (message[:terminal_width] if len(message) > terminal_width else message.ljust(terminal_width))
    print(f"{background_color}{color}{padded_message}{Style.RESET_ALL}")


configure_logging()
