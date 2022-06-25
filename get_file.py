import ftplib
import os
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine

try:
    week = weeks
    year = years
except:
    date = datetime.today() - timedelta(days=7)
    week = date.strftime("%W")
    year = date.strftime("%Y")

# DOWNLOAD FILE
path = '/tutela_border_merger_mm/'
filename = 'tutela_border_mm_'+year+week+'_isat3.csv'
store_path = 'F:/KY/tutela/download/'

ftp = ftplib.FTP("10.54.18.250")
ftp.login("tutela_border", "Nov2020@border")

try:
    ftp.cwd(path)
    ftp.retrbinary("RETR " + filename, open(store_path+filename, 'wb').write)
    ftp.quit()

    # PROCESS FILE TO A2
    df = pd.read_csv(
        'F:/KY/tutela/download/tutela_border_mm_'+year+week+'_isat3.csv')

    reg1 = df["region"] == "JABAR"
    reg2 = df["region"] == "WESTERN JABOTABEK"
    reg3 = df["region"] == "EASTERN JABOTABEK"
    reg4 = df["region"] == "CENTRAL JABOTABEK"

    mask = reg1 | reg2 | reg3 | reg4
    mask_jabar = reg1

    df_filtered = df.loc[mask]

    df_filtered.to_csv(
        'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/2022/TUTELA_BORDER_MERGER_MM_W'+week+'.csv', index=False)

    df_filtered = df.loc[mask_jabar]

    df_filtered.to_csv(
        'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/2022/JABAR/TUTELA_BORDER_MERGER_MM_W'+week+'_JABAR.csv', index=False)

    dir = 'F:/KY/tutela/download/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    engine = create_engine(
        'mysql://dbjabar:Telkomsel#1@10.3.193.202/performance')

    name_file = 'TUTELA_BORDER_MERGER_MM_W'+week+'.csv'
    df = pd.read_csv("F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/" +
                     year+"/"+name_file, sep=',', quotechar='\'', encoding='utf8')
    df.to_sql('tutela_border_merger_mm', con=engine,
              index=False, if_exists='append')

    try:
        update.message.reply_text(
            "Update "+name_file+" to FTP & DB SQA is Done")
    except:
        os.environ["https_proxy"] = "https://10.59.66.1:8080"
        os.system("telegram-send Update_tutela_W"+week+"_Done")
except:
    name_file = 'TUTELA_BORDER_MERGER_MM_W'+week+'.csv'
    try:
        update.message.reply_text(name_file+" is missing")
    except:
        os.environ["https_proxy"] = "https://10.59.66.1:8080"
        os.system("telegram-send Tutela_W"+week+"_is_missing")
