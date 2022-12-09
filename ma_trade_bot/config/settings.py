import os
import sys
import logging
from logging import handlers

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# add the project root directory to the sys.path variable so that the ma_trade_bot module can be imported
sys.path.append(BASE_DIR)

DOTENV_PATH = os.path.join(BASE_DIR, '.env')
if not os.path.exists(DOTENV_PATH):
    raise FileNotFoundError('Could not find required \'.env\' config file in project root folder')
load_dotenv(DOTENV_PATH)

# Telegram ma_trade_bot access token
BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_SKIP_UPDATES = True if os.getenv('BOT_SKIP_UPDATES') == 'True' else False

# Polling has a higher priority.
# If you specify USE_POLLING = True and USE_WEBHOOK = True,
# then the bot will start according to the polling system
USE_POLLING = True if os.getenv('USE_POLLING') == 'True' else False
USE_WEBHOOK = True if os.getenv('USE_WEBHOOK') == 'True' else False

# Do not specify for WEBHOOK_HOST at the end of /
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = int(os.getenv('WEBAPP_PORT', 80))


# The maximum number of characters allowed in one message
MAX_MESSAGE_LEN = os.getenv('MAX_MESSAGE_LEN')
MAX_MESSAGE_LEN = int(MAX_MESSAGE_LEN) if MAX_MESSAGE_LEN and MAX_MESSAGE_LEN.isdigit() else 64

# Storage of media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

LOGGER_NAME = 'main'
LOG_FILENAME = LOGGER_NAME + '.log'

LOG_FILEPATH = os.path.join(LOGS_DIR, LOG_FILENAME)
if not os.path.exists(LOG_FILEPATH):
    open(LOG_FILEPATH, 'a').close()

# maxBytes = 5Mb
LOGGER_FILE_HANDLER = handlers.RotatingFileHandler(filename=LOG_FILEPATH, maxBytes=5 ** (1024 * 2), backupCount=1)

try:
    from ma_trade_bot.root_logging import logger
except ImportError as exc:
    raise exc

LOGGER = logger.Logger(name=LOGGER_NAME, level=logging.DEBUG, handler=LOGGER_FILE_HANDLER)
