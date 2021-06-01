from bs4 import BeautifulSoup

def parse_file(filename):
    ids_for_config = []
    with open(f"html//{filename}","r",encoding="utf-8") as f:
        html = f.read()
        soup = BeautifulSoup(html,'html.parser')
        for link in soup.find_all('a',{'class':'contextclip-img-thumb'}):
            href = link.get('href').split('/')[-1]
            ids_for_config.append(href)
    return ids_for_config
