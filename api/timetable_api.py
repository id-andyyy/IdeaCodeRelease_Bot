import aiohttp
from config_data.config import load_config

config = load_config(r'.env')


async def search_group_timetable(group_number: str) -> int | None:
    url = f'{config.api.base_url}/timetable/search_group?query={group_number}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data and len(data) == 1:
                    return int(data[0]['id'])
            return None


async def get_today_timetable(group_id: int) -> list[dict] | None:
    url = f'{config.api.base_url}/timetable/group/{group_id}/today'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            return None


async def get_tomorrow_timetable(group_id: int) -> list[dict] | None:
    url = f'{config.api.base_url}/timetable/group/{group_id}/tomorrow'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            return None


async def get_week_timetable(group_id: int) -> list[dict] | None:
    url = f'{config.api.base_url}/timetable/group/{group_id}/schedule'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            return None
