#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import requests

"""Script para obter e salvar os dados do orderbook da brazillex"""


def get_data(ticker):
    dfs = []

    url = 'https://braziliex.com/api/v1/public/tradehistory/timestamp/{}/1'.format(ticker)
    response = requests.get(url)
    start = pd.DataFrame(eval(response.text))
    dfs.append(start)


    n=1
    while n>0:
        n+=1
        print(n)
        urls = 'https://braziliex.com/api/v1/public/tradehistory/timestamp/{}/{}'.format(ticker,start['timestamp'][9999])
        responses = requests.get(urls)
        start = pd.DataFrame(eval(responses.text))
        dfs.append(start)
        if start.index.size < 10000:
            break
    return dfs

def save_data(name):
    df = get_data(name)
    data = pd.concat(df)
    data.set_index('date_exec',inplace=True)
    data.to_csv('brazillex_{}.csv'.format(name))


save_data('bch_brl')




