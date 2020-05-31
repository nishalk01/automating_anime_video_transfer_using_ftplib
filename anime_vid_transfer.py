import ftplib
import os
import time
from dateutil import parser
from datetime import datetime
path="storage/shared/UCDownloads/video"
save_downloads_="/home/nishal/ftp_through"
ftp=ftplib.FTP()
ftp.connect("192.168.43.1",1024)


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


for file_ in files:
    try:
      name="MDTM {}".format(file_)
      date_time=ftp.sendcmd(name)
      li=date_time.split(" ")
      my_date = datetime.strptime(li[1], "%Y%m%d%H%M%S")
      date_of_mfile_=datetime(my_date.year,my_date.month,my_date.day)
      date_to_check=datetime(2020,5,29)
      if(date_of_mfile_>date_to_check):
          file_size_in_mb=convert_bytes_to_mb(file_)
          print("downloading {} of size {} MB...".format(file_,file_size_in_mb))
          #download(ftp,file_,save_downloads_)


      #print(date_of_mfile_)
      
      
      
    except:
       print("passed {}".format(file_))
      

# # for verbose of process slows down download speed
# #ftp.set_debuglevel(1)
# #print(ftp.sendcmd("pwd"))
