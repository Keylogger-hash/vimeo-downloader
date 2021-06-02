import requests
from fake_useragent import UserAgent

#Извлекает исходные ссылки для скачивания video
def get_source_urls(ids):
    #Создаем пустой массив для исходных ссылок
    source_urls = []
    # Проходимся циклом по всем id, которые мы нашли на html-странице
    for id in ids:
        #создаем фейковый User-Agent
        ua = UserAgent()
        #Создаем ссылку для извлечения конфигурации видео
        link_config = f"https://player.vimeo.com/video/{id}/config"
        # Устанавливаем заголовки
        header = {'User-Agent':str(ua.random)}
        # Шлем get-запрос для получения ответа
        r = requests.get(link_config,headers=header)
        # Если сервер принял запрос
        if r.status_code==200:
            # Преобразуем ответ сервера в формат json
            json_file = r.json()
            # Если видео, которое мы ищем ограничено настройками приватности, то пропускаем его
            if json_file.get("message") is not None:
                continue
            else:
                # Иначе извлекаем исходный url адресс.
                source_url = json_file["request"]["files"]["progressive"][0]["url"]
                # Добавляем данный адрес в наш массив для исходных ссылок
                source_urls.append((id,source_url))
        else:
            continue
    #Возвращаем массив с исходными url
    return source_urls
