import os
import datetime
import time
import random 

def get_time(file_name):
    p=time.ctime(os.path.getmtime(file_name))
    date_striped=datetime.datetime.strptime(p,"%a %b %d %H:%M:%S %Y") #Sat Mar 28 06:36:31 2020. is in this format
    date_of_file=datetime.datetime(date_striped.year,date_striped.month,date_striped.day,date_striped.hour,date_striped.minute,date_striped.second)
    return date_of_file

def run():
    path=".anime/"
    all_anime_vid=[]
    for root, dirs, files in os.walk(path, topdown=True):
     for name in files:
       file_=os.path.join(root, name)
       if os.path.isfile(file_):
        all_anime_vid.append(file_)
    time_of_all=[]
    for name_of_vid in all_anime_vid:
        time_of_all.append(get_time(name_of_vid))
    
    latest_time_=time_of_all[0]
    for i in range(len(time_of_all)):
        if(i<len(time_of_all)-1):
         if(latest_time_<time_of_all[i]):
           latest_time_=time_of_all[i]
    ind_t=time_of_all.index(latest_time_) 
    path_of_anime_ep=all_anime_vid[ind_t]
    name=os.path.basename(path_of_anime_ep)
    return name,latest_time_
