from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import settings

from paper_trader.bot_scripts import process_pair_info
from paper_trader.config import settings as paper_settings
from paper_trader.validations import is_valid_pair_message, is_valid_timeframe_message

import states

bot = Bot(token=settings.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp_: Dispatcher):
    if settings.USE_WEBHOOK and not settings.USE_POLLING:
        await bot.set_webhook(settings.WEBHOOK_URL)

    settings.LOGGER.log.debug('Bot started working')
    print('Bot started working')


async def on_shutdown(dp_: Dispatcher):
    if settings.USE_WEBHOOK and not settings.USE_POLLING:
        await bot.delete_webhook()

    # Close DB connection
    await dp_.storage.close()
    await dp_.storage.wait_closed()
    settings.LOGGER.log.debug('The bot has finished')
    print('The bot has finished')


@dp.message_handler(commands=['start', ])
async def cmd_start(message: types.Message):
    await states.PairState.pair.set()
    await message.reply('Pick the trading pair (for example: BTCUSDT):')


@dp.message_handler(commands=['help', ])
async def cmd_help(message: types.Message):
    await bot.send_message(message.chat.id, settings.CMD_HELP_TEXT)


@dp.message_handler(lambda message: len(message.text) > settings.MAX_MESSAGE_LEN, state='*')
async def process_many_symbols(message: types.Message, state: FSMContext):
    await state.reset_state()
    return await message.reply(text='Too many symbols!')


# pair validation
@dp.message_handler(lambda message: not is_valid_pair_message(message), state=states.PairState.pair)
async def process_pair_invalid(message: types.Message):
    """ If pair is not valid. Allowed only text message type. """
    return await message.reply('You have entered an invalid pair. Pair can only be text')


@dp.message_handler(lambda message: is_valid_pair_message(message), state=states.PairState.pair)
async def process_pair(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pair'] = message.text

    await states.PairState.next()
    await message.reply(f'Set up the timeframe (pick from {paper_settings.ALLOWED_TIMEFRAMES_STRING}:')


# timeframe validation
@dp.message_handler(lambda message: not is_valid_timeframe_message(message), state=states.PairState.timeframe)
async def process_timeframe_invalid(message: types.Message):
    """
    If timeframe is not allowed.
    Allowed only text message type and allowed only from the list of available timeframes.
    """
    return await message.reply(f'You have entered an unavailable timeframe.'
                               f'\nAvailable timeframes: {paper_settings.ALLOWED_TIMEFRAMES_STRING}.'
                               f'\nTry entering timeframe again')


@dp.message_handler(lambda message: is_valid_timeframe_message(message), state=states.PairState.timeframe)
async def process_timeframe(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['timeframe'] = message.text
        await state.finish()

        await process_pair_info(bot, message, data)


@dp.message_handler()
async def unknown_message(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Sorry, I don\'t understand what you wrote. Please use only available features.')
