import asyncio

import aiohttp

from .schema import create_pydantic


async def get_data(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_all(session, articles):
    base_url = 'https://card.wb.ru/cards/detail?nm='
    tasks = []
    for article in articles:
        url = base_url + str(article)
        task = asyncio.create_task(get_data(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def main(articles):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, articles)
        result = create_pydantic(data)
        return result
