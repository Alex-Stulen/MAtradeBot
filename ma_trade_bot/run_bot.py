from aiogram.utils import executor

from config import settings
from bot import dp, on_startup, on_shutdown


if __name__ == '__main__':
    try:
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    except Exception as exc:
        settings.LOGGER.log.critical(exc, exc_info=True)
