import os
import datetime
import time

def check_the_list(): #v1.2.0
    path=".anime/"
    all_anime_vid=[]
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            all_anime_vid.append(os.path.basename(name))
    return all_anime_vid
