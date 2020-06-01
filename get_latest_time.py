import os
import datetime
import time
import random 

def get_time(file_name):
    p=time.ctime(os.path.getmtime(file_name))
    date_striped=datetime.datetime.strptime(p,"%a %b %d %H:%M:%S %Y") #Sat Mar 28 06:36:31 2020. is in this format
    date_of_file=datetime.datetime(date_striped.year,date_striped.month,date_striped.day,date_striped.hour,date_striped.minute,date_striped.second)
    return date_of_file
      #date_to_check=datetime(2020,5,29)
      # datetime.datetime(2019, 7, 2,23,15,9)


def run_(): 
    path=".anime/"
    all_anime_vid=[]
    animes =os.listdir(path)
    for anime in animes:
        path2anime_vid=os.path.join(path,anime)
        anime_episodes=os.listdir(path2anime_vid)
        for i,anime_episode in enumerate(anime_episodes):
            path2anime=os.path.join(path2anime_vid,anime_episode)
            if(os.path.isdir(path2anime)):
                folder_in_folder=os.listdir(path2anime)
                for animes in folder_in_folder:
                    folder_in_folder_vid=os.path.join(path2anime,animes)
                    if(os.path.isfile(folder_in_folder_vid)):
                        all_anime_vid.append(folder_in_folder_vid)
                        
            elif(os.path.isfile(path2anime)):
             all_anime_vid.append(path2anime)

    time_of_all=[]
    for name in all_anime_vid:
     time_of_all.append(get_time(name))

    #find latest time
    latest_time_=time_of_all[0]
    for i in range(len(time_of_all)):
        if(i<len(time_of_all)-1):
         if(latest_time_<time_of_all[i]):
           latest_time_=time_of_all[i]

    ind_t=time_of_all.index(latest_time_) 
    path_of_anime_ep=all_anime_vid[ind_t]
    name=os.path.basename(path_of_anime_ep)
    return name,latest_time_
# t=latest_time_
# ind_t=time_of_all.index(t)
# path_of_anime_ep=all_anime_vid[ind_t]
# name=os.path.basename(path_of_anime_ep)

# print(run_())


#al=time_of_all[11]
#print(val)
#print(time_of_all.index(val))
