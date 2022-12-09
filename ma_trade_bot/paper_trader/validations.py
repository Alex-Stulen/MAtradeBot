from aiogram import types

from .config import settings


def _validate_list(validation_list):
    for validation in validation_list:
        if not validation:
            return False

    return True


def is_valid_pair(pair: str):
    validation_list = [
        pair is not None,
        isinstance(pair, str),
        len(pair) > 0,
        not pair.startswith('/')
    ]

    return _validate_list(validation_list)


def is_valid_pair_message(message: types.Message):
    # We use == because both message.content_type and ContentType.TEXT return a string
    return message.content_type == types.ContentType.TEXT and is_valid_pair(message.text)


def is_valid_timeframe(timeframe: str):
    validation_list = [
        timeframe is not None,
        isinstance(timeframe, str),
        len(timeframe) > 0,
        timeframe in settings.ALLOWED_TIMEFRAMES
    ]

    return _validate_list(validation_list)


def is_valid_timeframe_message(message: types.Message):
    # We use == because both message.content_type and ContentType.TEXT return a string
    if message.content_type != types.ContentType.TEXT:
        return False

    return is_valid_timeframe(message.text)
