"""
SaveStockData.py
Author: a-zagorulko
Date: 30.06.2022

This code saves balance sheet, income statement, cash statement data of a stock list into a dictionary
in a txt file.

Stock Lists:
Russell3000
SIX

"""

import pandas as pd
from scrape_tickers import scrape_tickers
from scrape_yahoofin import scrape_yahoofinance


# Get ticker names for RUssell3000 (5h) and SIX (30min)
Russell3000_stocks, swiss_stocks = scrape_tickers()
stocks1 = Russell3000_stocks['Symbol']

for symbol in swiss_stocks['Symbol']:
    swiss_stocks = swiss_stocks.replace([symbol], symbol + '.SW')
stocks2 = swiss_stocks['Symbol']

# Set names and thread count
name1 = 'Russell3000'
name2 = 'SIX'
threads = 4

#errors_SIX, time_SIX = scrape_yahoofinance(stocks2, name2, threads)
#print(errors_SIX, time_SIX)

errors_RUSSELL3000, time_RUSSELL3000 = scrape_yahoofinance(stocks1, name1, threads)



""" 
What info do I have in cash_statement_data?
1. investments
2. changeToLiabilities
3. totalCashflowsFromInvestingActivities
4. netBorrowings
5. totalCashFromFinancingActivities
6. changeToOperatingActivities
7. issuanceOfStock
8. netIncome
9. changeInCash
10. repurchaseOfStock
11. totalCashFromOperatingActivities
12. depreciation
13. otherCashflowsFromInvestingActivities
14. dividendsPaid
15. changeToInventory
16. changeToAccountReceivables
17. otherCashflowsFromFinancingActivities
18. changeToNetincome
19. capitalExpenditures
"""

