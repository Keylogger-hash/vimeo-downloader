from bs4 import BeautifulSoup

#Парсим скачанный файл html, для поиска id-видео
def parse_file(filename):
    # Создаем пустой массив для id-видео
    ids_for_config = []
    # Открываем файл в формате utf-8
    with open(f"html//{filename}","r",encoding="utf-8") as f:
        #Прочитаем файл
        html = f.read()
        #Преобразем его в формат удобный для парсинга
        soup = BeautifulSoup(html,'html.parser')
        #Пройдемся по всем ссылкам, где класс contextclib-img-thumb
        for link in soup.find_all('a',{'class':'contextclip-img-thumb'}):
            #Отделим символ '/' от id
            href = link.get('href').split('/')[-1]
            #Добавляем id в массив
            ids_for_config.append(href)
    # Возвращаем массив id
    return ids_for_config
