#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:14:30 2019

@author: math
"""


import requests
import json
import pandas as pd


def get_data(ticker):
    dfs = []

    url= 'https://www.buda.com/api/v2/markets/{}/trades.json?timestamp=1577836800000&limit=100'.format(ticker)
    response = requests.get(url)
    data = json.loads(response.text)
    headers= ['timestamp','amount','price','type_order','tid']
    start = pd.DataFrame(data['trades']['entries'],columns=headers)    
    dfs.append(start)
    
    
    n=1
    while n>0:
        n+=1
        print(n)
        urls = 'https://www.buda.com/api/v2/markets/{}/trades.json?timestamp={}&limit=100'.format(ticker, data['trades']['last_timestamp'])
        response = requests.get(urls)
        data = json.loads(response.text)
        start = pd.DataFrame(data['trades']['entries'],columns=headers)    
        dfs.append(start)

#        if n>10:
#            break
        if start.index.size < 100:
            break
    return dfs


def format_and_save(ticker):
    df = get_data(ticker)
    buda = pd.concat(df)
    buda.set_index('timestamp',inplace=True)
    buda.to_csv('buda_{}.csv'.format(ticker))



format_and_save('btc-clp')



