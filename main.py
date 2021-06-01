from concurrent.futures import ThreadPoolExecutor
from download.download_page import download_pagehtml
from download.download_video import download_file
from path.create_path import create_video_html_dirs
from validators.check_link import url_validator
from validators.check_chromedriver import check
from parse.scrapy import parse_file
from parse.source import get_source_urls
from datetime import timedelta
import time
import asyncio
import os

if __name__=="__main__":
    start_time = time.time()
    create_video_html_dirs()
    executable_path = str(input("Введите путь chromedriver.exe для Selenium-а:"))
    chromedriver = check(executable_path)
    if chromedriver==1:
        while(True):
            link_vimeo_for_download = str(input("Введите ссылку для скачивания видео с портала vimeo:"))
            if url_validator(link_vimeo_for_download) is not None:
                filename = download_pagehtml(link_vimeo_for_download,executable_path)
                urls_for_config = parse_file(filename)
                source_urls = get_source_urls(urls_for_config)
                if source_urls==[]:
                    print("Нам жаль, но видео защищено настройками приватности!\nМы ничего не можем сделать(")
                else:
                    loop = asyncio.get_event_loop()
                    executor = ThreadPoolExecutor(5)
                    loop.set_default_executor(executor)
                    tasks = [loop.create_task(download_file(id_video,url)) for id_video,url in source_urls]
                    try:
                        loop.run_until_complete(asyncio.wait(tasks))
                    finally:
                        elapsed_time = timedelta(seconds=round(time.time()-start_time))
                        print(f"Видео скачались за {elapsed_time}. Программа закрывается")
                        executor.shutdown(wait=True)
                        loop.close()
                break
            else:
                print("Попробуйте снова ссылка не корректно введена:пример(https://vimeo.com/111111111)\n")
    else:
        print("Неправильный путь до chromedriver.exe")
