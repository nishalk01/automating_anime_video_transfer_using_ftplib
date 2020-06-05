import ftplib
import os
import time
from datetime import datetime
from get_list import check_the_list

path="storage/shared/UCDownloads/video"
save_downloads_="./anime" #make where your'e saving is inside the folder your checking the list with 
ftp=ftplib.FTP()
ftp.connect("192.168.43.1",1024)

## for verbose of process slows down download speed
#ftp.set_debuglevel(1)  #u change value of levels for detailed verbose output

ftp.cwd(path)
files=ftp.nlst(".")

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
      if(file_.split(".")[1]=="mp4"):
          file_size_in_mb=convert_bytes_to_mb(file_)
          print("downloading {} of size {} MB...".format(file_,file_size_in_mb))
          download(ftp,file_,save_downloads_)
      
     except (ftplib.error_perm,IndexError):
           print("error")     


