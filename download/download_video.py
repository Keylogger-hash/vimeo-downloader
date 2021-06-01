import requests
import aiohttp
import asyncio
import aiofiles
from fake_useragent import UserAgent

async def download_file(id_video,url):
    ua = UserAgent()
    headers = {'User-Agent':str(ua.random)}
    filename = url.split('/')[-1]
    async with aiohttp.request('get',url,headers=headers) as response:
        if response.status==200:
            async with aiofiles.open(f"video\\{id_video}_{filename}",mode="wb") as f:
                async for data in response.content.iter_chunked(1024):
                    if data:
                        await f.write(data)
    print(f"This file was download from vimeo.com:{id_video}_{filename}")
