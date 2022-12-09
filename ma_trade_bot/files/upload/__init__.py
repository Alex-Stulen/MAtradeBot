import aiohttp


async def get_file_from_url(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception('Response is not 200 code')

            return await response.read()
