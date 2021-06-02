import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# На вход подается ссылка на сайт с видео vimeo.com и путь до Chromedriver
def download_pagehtml(url_vimeo,executable_path):
    #инициализируется бразуер
    browser = webdriver.Chrome(executable_path=executable_path)
    #из ссылки извлекается имя файла
    filename = url_vimeo.split('/')[-1]
    #браузер переходит по ссылке
    browser.get(url_vimeo)
    #расширяет окно
    browser.maximize_window()
    #также наш запрос иницализируется cookies и создается сессия
    cookies = browser.get_cookies()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'],cookie['value'])
    #уходит в сон для того чтобы вся страница прогрузилась
    time.sleep(1)
    #ищет элемент с рекомендациями
    element = browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/main/div/aside/div/div")
    #кликает на него
    webdriver.ActionChains(browser).move_to_element(element).perform()
    #уходит в сон для того чтобы вся страница прогрузилась
    time.sleep(1)
    #извлекается html контент и пишется в файл
    page = browser.page_source
    with open(f"html\\{filename}.html","w",encoding="utf-8") as f:
        f.write(page)
    #браузер закрывается
    browser.close()
    #возвращается имя файла
    return f"{filename}.html"
