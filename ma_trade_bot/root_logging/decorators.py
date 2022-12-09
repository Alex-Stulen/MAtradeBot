from functools import wraps

from ma_trade_bot.config import settings


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            settings.LOGGER.log.debug(f'Start processing "{func.__name__}"')
            response = func(*args, **kwargs)
            settings.LOGGER.log.debug(f'End of "{func.__name__}" processing. Successfully')
            return response

        except Exception as exc:
            settings.LOGGER.log.critical(exc, exc_info=True)

    return wrapper
