import os

def check(path):
    if os.path.exists(path) and os.access(path,os.F_OK):
        return 1
    else:
        return 0
