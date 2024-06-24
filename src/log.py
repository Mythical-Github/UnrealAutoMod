import os
import logging
from datetime import datetime

import settings

logger = logging.getLogger(__name__)

def configure_logging():
    log_dir = os.path.join(settings.SCRIPT_DIR, 'logs')
    timestamp = datetime.now().strftime('%m_%d_%Y_%H%M')
    log_file = os.path.join(log_dir, f'unreal_auto_mod_{timestamp}.log')
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_message(message: str):
    logger.info(message)
    print(message)

configure_logging()
