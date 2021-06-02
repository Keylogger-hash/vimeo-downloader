import os

#проверяет существует ли данный путь и есть ли доступ к этому файлу
def check(path):
    if os.path.exists(path) and os.access(path,os.F_OK):
        return 1
    else:
        return 0
