import re

#проверяет соответсвует ли ссылка на сайт vimeo.com шабдону
def url_validator(url):
    regexp = re.compile(r"^https://vimeo.com/[0-9]{8,9}$")
    return re.search(regexp,url)
