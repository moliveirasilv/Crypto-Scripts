#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import requests
import os


def get_data(ticker):
    '''obtem dados do orderbook do mercadobitcoin dado ticker'''

    dfs = []

    url = 'https://www.mercadobitcoin.net/api/{}/trades/1514764800'.format(ticker)
    response = requests.get(url)
    start = pd.DataFrame(eval(response.text))
    dfs.append(start)


    n=1
    while n>0:
        n+=1
        urls = 'https://www.mercadobitcoin.net/api/{}/trades/{}'.format(ticker,start['date'][999])
        print(n,urls)
        responses = requests.get(urls)
        start = pd.DataFrame(eval(responses.text))
        dfs.append(start)
        if start.index.size < 1000:
            break
    return dfs


def format(data):
    '''formata os dados obtidos'''
    df = pd.concat(data)
    df.set_index('date',inplace=True)
    return df







