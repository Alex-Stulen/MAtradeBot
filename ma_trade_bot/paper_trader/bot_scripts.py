from aiogram import types, Bot

from ma_trade_bot.parser.html.images import get_all_images
from ma_trade_bot.urls.core import build_absolute_url
from ma_trade_bot.files.upload import get_file_from_url
from ma_trade_bot.paper_trader.request import PaperTradeRequest
from ma_trade_bot.paper_trader.dataclasses import PostDataHandle
from ma_trade_bot.root_logging.decorators import log


@log
async def process_pair_info(bot: Bot, message: types.Message, data: dict):
    """ scenario for processing data pairs and sending messages by a bot """

    # Creation and validation post data to paper trader
    post_data_handler = PostDataHandle(**data)
    if not post_data_handler.is_valid():
        errors_as_text = post_data_handler.errors_as_text(sep='\n')
        return await bot.send_message(
            message.chat.id,
            f'You have entered incorrect data. Errors: {errors_as_text}'
        )

    data_as_text = post_data_handler.as_text(sep='\n')
    await bot.send_message(
        message.chat.id,
        f'Your data has been accepted.'
        f'\nData:\n{data_as_text}'
    )
    await bot.send_message(message.chat.id, 'Wait, please. Loading data...')

    response = await PaperTradeRequest.post(post_data_handler.as_dict())
    response_text = await response.text()

    if response.status != 200:
        return await bot.send_message(message.chat.id, 'Failed to load data. Try again later')

    all_images = get_all_images(response_text)

    # process response errors
    if 'error' in response_text or len(all_images) == 0:
        return await bot.send_message(message.chat.id, 'Failed to load data or data is missing 😢'
                                                       '\nTry changing the input or try again later.')

    # get image from url as file bytes and send diagram to user
    for image in all_images:
        image_src = image.get('src')
        if image_src is None:
            continue

        image_absolute_url = build_absolute_url(PaperTradeRequest.HOST, image_src)
        try:
            file_bytes = await get_file_from_url(image_absolute_url)
            await bot.send_message(message.chat.id, '📈 Diagram:')
            await bot.send_photo(message.chat.id, file_bytes)
        except Exception as e:
            await bot.send_message(message.chat.id, 'Some data could not be loaded 😢')
