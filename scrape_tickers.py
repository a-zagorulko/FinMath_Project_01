"""
scrape_tickers.py
Author: a-zagorulko
Date: 21.06.2022

Function to scrape stock index data of the RUSSELL 3000 and the SIX Group
Input: -
Output: df_russell, df_swiss (Dataframes with Col: Company, Ticker)

"""

import datetime as dt
import pandas as pd
import numpy as np
import urllib.request
from tabula.io import read_pdf
import os

def scrape_tickers():

    ### RUSSELL 3000 Dataframe
    # Download Russell 3000 PDF List
    russell3000_link = 'https://content.ftserussell.com/sites/default/files/ru3000_membershiplist_20210628.pdf'


    def download_file(download_url, filename):
        response = urllib.request.urlopen(download_url)
        file = open(filename + ".pdf", 'wb')
        file.write(response.read())
        file.close()


    f_name = 'Russell3000'
    download_file(russell3000_link, f_name)

    # Parse PDF into list
    PDF_data = read_pdf(f_name + '.pdf', pages='all')
    df_russell = pd.DataFrame(columns=['Company', 'Ticker'])

    # Convert list into dataframe
    # Col: Company, Ticker
    for i in range(len(PDF_data)):
        df_name1 = PDF_data[i]['Company']
        df_ticker1 = PDF_data[i]['Ticker']
        df_name2 = PDF_data[i]['Ticker.1']
        df_ticker2 = PDF_data[i]['Unnamed: 0']
        df_new1 = pd.concat([df_name1, df_ticker1], axis=1)  # Table 1 on page i
        df_new2 = pd.concat([df_name2, df_ticker2], axis=1)  # Table 2 on page i
        df_new2.rename(columns={'Ticker.1': 'Company', 'Unnamed: 0': 'Ticker'}, inplace=True)

        df_new = pd.concat([df_new1, df_new2], axis=0)  # Page i

        df_russell = pd.concat([df_russell, df_new], axis=0)

    df_russell = df_russell.reset_index(drop=True)
    df_russell.rename(columns={'Ticker':'Symbol'}, inplace=True)
    df_russell.dropna(subset=['Company'], inplace=True)

    # SIX Dataframe
    path = os.path.abspath('SIX_equity_issuers.csv')
    print(path)
    df_six_data = pd.read_csv(path, sep=';',
                              encoding='latin-1')
    df_swiss1 = df_six_data.Company
    df_swiss2 = df_six_data.Symbol
    df_swiss = pd.concat([df_swiss1,df_swiss2], axis=1)

    # TODO: CHECK FOR DUPLICATES IF COMBINE RUSSELLL AND SIX

    return df_russell, df_swiss

