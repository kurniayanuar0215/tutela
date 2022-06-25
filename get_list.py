import ftplib
from operator import index
import os
import mysql.connector
import pandas as pd

#CHECK IN FTP
path = '/tutela_border_merger_mm/'

ftp = ftplib.FTP("10.54.18.250") 
ftp.login("tutela_border", "Nov2020@border") 

files = []

try:
    ftp.cwd(path)
    files = ftp.nlst()
except ftplib.error_perm as resp:
    if str(resp) == "550 No files found":
        print ("No files in this directory")
    else:
        raise
x = list()
for f in files:
    namefile = f.split('_')
    x.append(namefile[3])

x = list(map(int, x))
last_tutela = str(max(x))

#CHECK IN DB
mydb  = mysql.connector.connect(
    host="10.3.193.202",
    user="dbjabar",
    password="Telkomsel#1",
    database="performance"
)
cursor = mydb.cursor()

cursor.execute('''SELECT MAX(`yearweek`) lastweek FROM `tutela_border_merger_mm`''')
result = cursor.fetchall()

for i in result:
    lastweek = str(i[0])[0:6]

try:
    if last_tutela == lastweek:
        update.message.reply_text("Last Tutela in FTP area : "+last_tutela+"\n"+"Last Tutela in DB SQA : "+lastweek+"\n"+"Status is Updated")
    else:
        update.message.reply_text("Last Tutela in FTP area : "+last_tutela+"\n"+"Last Tutela in DB SQA : "+lastweek+"\n"+"type '/updatetutela "+str(last_tutela)+"' for update")
except:
    os.environ["https_proxy"] = "https://10.59.66.1:8080"
    os.system("telegram-send "+str(last_tutela))