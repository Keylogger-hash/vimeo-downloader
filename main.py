from concurrent.futures import ThreadPoolExecutor
# импорт функции скачивающей страницу
from download.download_page import download_pagehtml
# импорт функции асинхронно скачивающую файлы
from download.download_video import download_file
# импорт функции создающую папку с video и html
from path.create_path import create_video_html_dirs
# импорт функции для проверки ссылки на сайт
from validators.check_link import url_validator
# импорт функции для проверки chromedriver для Selenium-а
from validators.check_chromedriver import check
# импорт функции для парсинга файла извлечения из него всех id видео
from parse.scrapy import parse_file
# импорт функции для извлечения исходных ссылок на видео
from parse.source import get_source_urls
# импорт библиотеки datetime и time для того, чтобы посчитать время программы
from datetime import timedelta
import time
# импорт библиотеки asyncio для асинхронного выполнения скачивания многих файлов
import asyncio
# импорт библиотеки для работы с файлами
import os

if __name__=="__main__":
    # переменная start_time для отсчета момента запуска программы
    start_time = time.time()
    # создание папок video и html
    create_video_html_dirs()
    # ввод пользователем драйвера пути до драйвера chrome Selenium
    executable_path = str(input("Введите путь chromedriver.exe для Selenium-а:"))
    # проверка данного адреса
    chromedriver = check(executable_path)
    # если проверка удалась,то
    if chromedriver==1:
        # Запускаем бесконечный цикл для ввода ссылки
        while(True):
            # Пользователь вводит ссылку на видео
            link_vimeo_for_download = str(input("Введите ссылку для скачивания видео с портала vimeo:"))
            # Проверяем что ссылка введена правильно
            if url_validator(link_vimeo_for_download) is not None:
                # скачиваем файл с нужной страницей
                filename = download_pagehtml(link_vimeo_for_download,executable_path)
                # Извлекаем id видео, которое мы хотели скачать и всех рекомендованных
                urls_for_config = parse_file(filename)
                # Извлекаем исходные ссылки на видео
                source_urls = get_source_urls(urls_for_config)
                # Если массив ссылок не пустой, то скачиваем, иначе видео защищено настройками приватности
                if source_urls==[]:
                    print("Нам жаль, но видео защищено настройками приватности!\nМы ничего не можем сделать(")
                else:
                    # Запускаем event-loop
                    loop = asyncio.get_event_loop()
                    # Устанавливаем максимальное число потоков - 5
                    executor = ThreadPoolExecutor(5)
                    loop.set_default_executor(executor)
                    # Создаем задачи для параллельного асинхронного скачивания
                    tasks = [loop.create_task(download_file(id_video,url)) for id_video,url in source_urls]
                    try:
                        # Ждем пока event-loop сделает всю работу
                        loop.run_until_complete(asyncio.wait(tasks))
                    finally:
                        # Замеряем время работы
                        elapsed_time = timedelta(seconds=round(time.time()-start_time))
                        # Печатаем результат
                        print(f"Видео скачались за {elapsed_time}. Программа закрывается")
                        # Закрываем event-loop
                        executor.shutdown(wait=True)
                        loop.close()
                break
            #Если ссылка введена не корректно показываем пользователю правильный пример
            else:
                print("Попробуйте снова ссылка не корректно введена:пример(https://vimeo.com/111111111)\n")
    # Если неправильный путь 
    else:
        print("Неправильный путь до chromedriver.exe")
