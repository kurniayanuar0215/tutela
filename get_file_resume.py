import os
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine

try:
    week = weeks
    year = years
except:
    date = datetime.today() - timedelta(days=7)
    week = 'date.strftime("%W")'
    year = date.strftime("%Y")

# PROCESS FILE TO A2
fields = ['period', 'yearweek', 'date_start', 'date_end', 'level', 'region', 'location', 'location_id', 'node', 'operator',
          'sample', 'device_share', 'good_quality', 'game_parameter', 'good_coverage', 'coverage_share', 'video_score_netflix']

df = pd.read_csv(
    'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/'+year+'/TUTELA_BORDER_MERGER_MM_W'+week+'.csv', usecols=fields)

reg1 = df["region"] == "JABAR"
level = df["level"] == "kabupaten"
node = df["node"] == "4G"

mask = reg1 & level & node
df_filtered = df.loc[mask]

df_filtered.to_csv(
    'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/'+year+'/RESUME/TUTELA_BORDER_MERGER_MM_W'+week+'.csv', index=False)

try:
    update.message.bot.sendDocument(update.message.chat.id, open(
        'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/'+year+'/RESUME/TUTELA_BORDER_MERGER_MM_W'+week+'.csv', 'rb'))
except:
    os.environ["https_proxy"] = "https://10.59.66.1:8080"
    os.system('telegram-send --file F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/' +
              year+'/RESUME/TUTELA_BORDER_MERGER_MM_W'+week+'.csv')
