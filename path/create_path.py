import os

#Создает папки video и html для того, чтобы сохранять туда mp4-файлы и html-страницы соответсвенно
def create_video_html_dirs():
    current_dir = os.getcwd()
    video_path = f"{current_dir}\\video"
    html_path = f"{current_dir}\\html"
    if os.path.exists(video_path)!=True:
        os.mkdir("video")
    if os.path.exists(html_path)!=True:
        os.mkdir("html")
