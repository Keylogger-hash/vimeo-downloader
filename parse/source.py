import requests
from fake_useragent import UserAgent
ua = UserAgent()

def get_source_urls(ids):
    source_urls = []
    for id in ids:
        link_config = f"https://player.vimeo.com/video/{id}/config"
        header = {'User-Agent':str(ua.random)}
        r = requests.get(link_config,headers=header)
        if r.status_code==200:
            json_file = r.json()
            if json_file.get("message") is not None:
                continue
            else:
                source_url = json_file["request"]["files"]["progressive"][0]["url"]
                source_urls.append((id,source_url))
        else:
            continue
    return source_urls
