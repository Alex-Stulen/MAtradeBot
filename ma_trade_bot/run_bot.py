from aiogram.utils import executor

from config import settings
from bot import dp, on_startup, on_shutdown


if __name__ == '__main__':
    try:
        if settings.USE_POLLING:
            executor.start_polling(
                dispatcher=dp,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
                skip_updates=settings.BOT_SKIP_UPDATES
            )
        elif settings.USE_WEBHOOK:
            executor.start_webhook(
                dispatcher=dp,
                webhook_path=settings.WEBHOOK_PATH,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
                skip_updates=settings.BOT_SKIP_UPDATES,
                host=settings.WEBAPP_HOST,
                port=settings.WEBAPP_PORT,
            )
    except Exception as exc:
        settings.LOGGER.log.critical(exc, exc_info=True)
