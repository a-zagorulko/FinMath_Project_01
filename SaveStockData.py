"""
SaveStockData.py
Author: a-zagorulko
Date: 30.06.2022

This code saves balance sheet, income statement, cash statement data of a stock list into a dictionary
in a txt file.

SET: threads to match max threads of your machine.s

Stock Lists:
Russell3000
SIX

"""

import pandas as pd
from scrape_tickers import scrape_tickers
from scrape_yahoofin import scrape_yahoofinance

def SaveStockData(name,threads):

    # Get ticker names for RUssell3000 (5h) and SIX (30min)
    Russell3000_stocks, swiss_stocks = scrape_tickers()
    stocks1 = Russell3000_stocks['Symbol']

    for symbol in swiss_stocks['Symbol']:
        swiss_stocks = swiss_stocks.replace([symbol], symbol + '.SW')
    stocks2 = swiss_stocks['Symbol']

    if name == 'Russell3000':
        errors_Russell3000, time_Russell3000 = scrape_yahoofinance(stocks2, name2, threads)
        print(errors_Russell3000,time_Russell3000)
    elif name == 'SIX':
        errors_SIX, time_SIX = scrape_yahoofinance(stocks2, name2, threads)
        print(errors_SIX, time_SIX)
    else:
        print('Error in StockListName')
    return 0
