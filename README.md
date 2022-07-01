# FinMath_Project_01
In this small and fun project we scrape stock data from the RUSSELL3000 and SIX listed stocks, store it and analyse it.

Goal: Scrape for stock information and analyse stock data to filter out stocks worth analysing further.
Outline: 
1. Scrape PDF file (Russell3000.pdf) for the tickers of the stocks contained in the Russell 3000 index. Then scrape the scv file for all tickers of stocks on the swiss stock exchange.  
2. Using YahooFinance retrieve balance sheet, income statement, cash statement of the stocks we input. Store the company data in a dictionary and save it as a .txt file.
3. Read the .txt file literally and analyse the company information using non-cashflow and cashflow based methods. Select criteria to form a group of stocks to further analyse. 

Files: 
------.txt files of dictionaries that contain company information scraped using yahoofinance in the function file SaveStockData.
scrape_tickers.py is the function used to scrape ticker information from files to dataframes.
scrape_yahoofin.py is the function used to scrape yahoofinance, whereby multithreading is used to multiply in/out limited yahoo api.

Instructions: RUN AnalyzeStockData.py

Any comments and suggestions on code is welcome. 