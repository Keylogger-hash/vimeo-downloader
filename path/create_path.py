import os

def create_video_html_dirs():
    current_dir = os.getcwd()
    video_path = f"{current_dir}\\video"
    html_path = f"{current_dir}\\html"
    if os.path.exists(video_path)!=True:
        os.mkdir("video")
    if os.path.exists(html_path)!=True:
        os.mkdir("html")
