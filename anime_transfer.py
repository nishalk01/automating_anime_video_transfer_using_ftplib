import ftplib
from tqdm import tqdm
import os
import time
from dateutil import parser
from datetime import datetime
# from latest_mtime import  check_the_list
path="UCDownloads/video"
save_downloads_=".anime/"

ftp=ftplib.FTP()
ftp.connect("192.168.43.1",1024)
ftp.login()
ftp.cwd(path)
ftp.pwd()
files=ftp.nlst(".")
ftp.voidcmd('TYPE I')

## for verbose of process slows down download speed
#ftp.set_debuglevel(1)  #u change value of levels for detailed verbose output

def check_the_list(): 
    path=".anime/"
    all_anime_vid=[]
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            all_anime_vid.append(os.path.basename(name))
    return all_anime_vid



def download(ftp,file, localdir): #downloads the file
    start=time.time()
    f = open(os.path.join(localdir, file),"wb")
    ftp.retrbinary("RETR " + file,f.write,blocksize=262144)
    f.close()
    end=time.time()
    print(end-start)

def convert_bytes_to_mb(file_): #converts given filename size to MB from bytes 
    return str(round(ftp.size(file_)/(1000*1000),2))


all_anime_dow=check_the_list()
for file_ in files:
    if(file_ not in all_anime_dow):
     try:
      if(file_.split(".")[1]=="mp4"):#downloads only mp4
          file_size_in_mb=convert_bytes_to_mb(file_)
          print("downloading {} of size {} MB...".format(file_,file_size_in_mb))
          download(ftp,file_,save_downloads_)
      
     except (ftplib.error_perm,IndexError):
           print("error")     


