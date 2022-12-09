import aiohttp


class PaperTradeRequest(object):
    """ Class for working with requests to the host https://paper-trader.frwd.one """
    HOST = 'https://paper-trader.frwd.one'

    @classmethod
    async def post(cls, data: dict):
        async with aiohttp.ClientSession() as session:
            return await session.post(url=cls.HOST, data=data)
