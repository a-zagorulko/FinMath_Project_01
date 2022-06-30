"""
scrape_yahoofin.py
Author: a-zagorulko
Date: 22.06.2022

Function that gets data from YahooFinance for given stock
Input: tickerlist
Output:

For yahoofinancials function see: https://pypi.org/project/yahoofinancials/
For multithreading with concurrent.futures see: https://docs.python.org/3/library/concurrent.futures.html
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import concurrent.futures as cf
import time


def scrape_yahoofinance(stocks, name, threads):
    """ Function that creates txt files of dictionaries of balance, income and cash statements
    :param stocks: list, array, or df of stock tickers
    :param name: name to append to file name
    :param threads: int indicating number of threads for multithreading
    :return: array of tickers with errors, time for operation
    """

    # Create empty dictionaries for storing financial data
    balanceSheet = {}
    incomeStatement = {}
    cashStatement = {}
    errors = []

    def getFinancialData(stock):
        try:
            x = YahooFinancials(stock)
            # GET data
            balance_sheet_data = x.get_financial_stmts('annual', 'balance')
            income_statement_data = x.get_financial_stmts('annual', 'income')
            cash_statement_data = x.get_financial_stmts('annual', 'cash')

            # PUT data in dictionaries
            balanceSheet[stock] = balance_sheet_data['balanceSheetHistory'][stock]
            incomeStatement[stock] = income_statement_data['incomeStatementHistory'][stock]
            cashStatement[stock] = cash_statement_data['cashflowStatementHistory'][stock]
        except:
            print('ERROR with retrieving stock data')
            errors.append(stock)

    """
    Multithreading: we send multiple requests, limited by number of computer threads to the api, 
    as the api is input output limited. This way we can speed up the process of getting data for multiple stocks.
    """

    start = time.time()
    executor = cf.ThreadPoolExecutor(threads)  # make executor that says how many threads to execute
    futures = [executor.submit(getFinancialData, stock) for stock in stocks]  # make a list of executor submissions and which function you submit
    cf.wait(futures)  # wait for execution of all items in futures
    end = time.time()

    # WRITE data to files
    with open('balanceSheet_' + name + '.txt', 'w') as output:
        output.write(str(balanceSheet))
    with open('incomeStatement_' + name + '.txt', 'w') as output:
        output.write(str(incomeStatement))
    with open('cashStatement_' + name + '.txt', 'w') as output:
        output.write(str(cashStatement))

    return errors, end - start


