import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def download_pagehtml(url_vimeo,executable_path):
    browser = webdriver.Chrome(executable_path=executable_path)
    filename = url_vimeo.split('/')[-1]
    browser.get(url_vimeo)
    browser.maximize_window()
    cookies = browser.get_cookies()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'],cookie['value'])
    time.sleep(1)
    element = browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/main/div/aside/div/div")
    webdriver.ActionChains(browser).move_to_element(element).perform()
    time.sleep(1)
    page = browser.page_source
    with open(f"html\\{filename}.html","w",encoding="utf-8") as f:
        f.write(page)
    browser.close()
    return f"{filename}.html"
