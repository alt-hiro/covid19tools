# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:22:13 2020

@author: Takano
"""

import datetime
import requests
import pandas as pd

filename = 'daily_positive_detail'
url = 'https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/development/data/daily_positive_detail.json'
exectime = datetime.datetime.now().strftime('%Y%m%d%H%M')

## 東京都のCOVID-9 のデータを取得
res = requests.get(url)

## dictからdataframeに変換
d = res.json()
df = pd.DataFrame.from_dict(d['data'])

## 累計合計を取得
df['missing_count_cumsum'] = df['missing_count'].transform(pd.Series.cumsum) 
df['reported_count'] = df['reported_count'].transform(pd.Series.cumsum) 

## CSV ファイルに書き出し
df.to_csv(filename + exectime + '.csv')


