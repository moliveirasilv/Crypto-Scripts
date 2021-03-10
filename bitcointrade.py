#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:33:04 2019

@author: math
"""

import pandas as pd
import requests
import json


pages = range(1,599)
dfs = []

for page in pages:
    try:
        url = 'https://api.bitcointrade.com.br/v2/public/BRLLTC/trades?start_time=2018-01-01T00:00:00-03:00&end_time=2020-01-31T23:59:59-03:00&page_size=249&current_page={}'.format(page)
        print(url) #progressbar
        payload = {}
        headers = {
          'Content-Type': 'application/json'
        }
        response = requests.request('GET', url, headers = headers, allow_redirects=False)
        
        text = json.loads(response.text)
        nested = pd.DataFrame(text)
        unesting = dict(nested['data'])
        data = pd.DataFrame(unesting['trades'])
        dfs.append(data)
#        break
    except:ValueError


#print(text)

dados = pd.concat(dfs)
dados.to_csv("brl_ltc_bitcointrade_2.csv")





    