"""
AnalyzeStockData.py
Author: a-zagorulko
Date: 30.06.2022

Here we read and analyze the income, balance and cash data on stocks to define a group of stocks to further
investigate. We use following measures to value a company:

Non-Cash-Flow based methods
------------------------------------
ROE Growth
EPS Growth
------------------------------------
------------------------------------
Cash-Flow-Discounting based methods
------------------------------------


------------------------------------

"""
import ast
import pandas as pd

# READ data from files
with open('balanceSheet_Russell3000.txt', 'r') as input:
    balanceSheet = ast.literal_eval(input.read())

with open('incomeStatement_Russell3000.txt', 'r') as input:
    incomeStatement = ast.literal_eval(input.read())

with open('cashStatement_Russell3000.txt', 'r') as input:
    cashStatement = ast.literal_eval(input.read())

############### ROE and EPSG GROWTH ###############
roe_dict, epsg_dict = {}, {}
count_missing, count_cond, count_eps_0 = 0, 0, 0
for (keyB, valB), (keyI, valI) in zip(balanceSheet.items(), incomeStatement.items()):
    try:
        if keyB == keyI:
            yearsI = [k for year in valI for k, v in year.items()]
            yearsB = [k for year in valB for k, v in year.items()]
            if yearsI == yearsB:
                count_cond += 1
                equity = [v['totalStockholderEquity'] for year in valB for k, v in year.items()]
                commonStock = [v['commonStock'] for year in valB for k, v in year.items()]
                profit = [v['grossProfit'] for year in valI for k, v in year.items()]
                revenue = [v['totalRevenue'] for year in valI for k, v in year.items()]
                netIncome = [v['netIncome'] for year in valI for k, v in year.items()]
                roe = [round(netin/equity*100,2) for netin, equity in zip(netIncome, equity)]
                roe_dict[keyB] = (round(sum(roe)/len(roe),2), roe)
                eps = [round(earn/stono,2) for earn, stono in zip(profit, commonStock)]

                try:
                    epsg = []
                    for ep in range(len(eps)):
                        if ep == 0:
                            continue
                        elif ep == 1:
                            epsg.append(round(100*((eps[ep-1]/eps[ep])-1),2))
                        elif ep == 2:
                            epsg.append(round(100*((eps[ep-2]/eps[ep])**(1/2)-1),2))
                            epsg.append(round(100*((eps[ep-1]/eps[ep])-1),2))
                        elif ep == 3:
                            epsg.append(round(100*((eps[ep-3]/eps[ep])**(1/3)-1),2))
                            epsg.append(round(100*((eps[ep-1]/eps[ep])-1),2))
                        else:
                            print('More than 4 years of FY data')

                    epsg_dict[keyB] = (round(sum(epsg)/len(epsg),2), epsg)
                except:
                    #                     print(keyB, 'eps contains 0')
                    count_eps_0 += 1
                    epsg_dict[keyB] = (0, eps)
    except:
        #         print(keyB, 'data missing')
        count_missing += 1
print('Yearly data avail',count_cond, 'out of', len(balanceSheet))
print('Some key data missing', count_missing, 'out of', len(balanceSheet))
print('EPS Growth NaN', count_eps_0, 'out of', len(balanceSheet))

# Set ROE and ESPG growth requirement
ROE_req = 10
EPSG_req = 10
print('-'*50, 'RETURN ON EQUITY','-'*50)
roe_crit = {k:v for (k,v) in roe_dict.items() if v[0] >= ROE_req and sum(n < 0 for n in v[1])==0}
print(roe_crit)
print('-'*50, 'EARNINGS PER SHARE GROWTH','-'*50)
eps_crit = {k:v for (k,v) in epsg_dict.items() if v[0] >= EPSG_req and sum(n < 0 for n in v[1])==0}
print(eps_crit)
print('-'*50, 'ROE & EPS Growth Critera','-'*50)
both = [key1 for key1 in roe_crit.keys() for key2 in eps_crit.keys() if key2==key1]
print(both)


################## Cash-Flow-Depreciation Methods ##################




