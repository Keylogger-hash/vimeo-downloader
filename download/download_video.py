import requests
import aiohttp
import asyncio
import aiofiles
from fake_useragent import UserAgent

#Асинхронно скачиваем все видео
async def download_file(id_video,url):
    # Инициализируем User-Agent
    ua = UserAgent()
    # Устанавливаем заголовки
    headers = {'User-Agent':str(ua.random)}
    # Разделяем имя файла
    filename = url.split('/')[-1]
    # Асинхронно шлем запрос на исходный файл
    async with aiohttp.request('get',url,headers=headers) as response:
        # Если статус ответа сервера 2000,то
        if response.status==200:
            #Асинхронно открываем файл
            async with aiofiles.open(f"video\\{id_video}_{filename}",mode="wb") as f:
                # Проходим итерацию по тем данным, которые нам выслал сервер
                async for data in response.content.iter_chunked(1024):
                    # Если chunk не пустой
                    if data:
                        # Асинхронно пишем данные в файл
                        await f.write(data)
    #Печатаем сообщение о том, что видео было скачано
    print(f"This file was download from vimeo.com:{id_video}_{filename}")
