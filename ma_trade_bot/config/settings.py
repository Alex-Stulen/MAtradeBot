import os
import sys

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# add the project root directory to the sys.path variable so that the bot module can be imported
sys.path.append(BASE_DIR)

DOTENV_PATH = os.path.join(BASE_DIR, '.env')
if not os.path.exists(DOTENV_PATH):
    raise FileNotFoundError('Could not find required \'.env\' config file in project root folder')
load_dotenv(DOTENV_PATH)

# Telegram bot access token
BOT_TOKEN = os.getenv('BOT_TOKEN')

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
