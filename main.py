"""
main.py
Author: a-zagorulko
Date: 11.07.2022

This is the main file that executes functions scrape_tickers, scrape_yahoo, SaveStockData and AnalyzeStockData.

Inputs: Select Russell3000 or Six listed stocks, number of cores for multithreading

"""

from SaveStockData import SaveStockData

# Names of Stocklists
name1 = 'Russell3000'
name2 = 'SIX'
threads = 8

def main(name2, threads):
    SaveStockData(name1, threads)
    return 0
