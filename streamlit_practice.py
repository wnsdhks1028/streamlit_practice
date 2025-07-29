import streamlit as st
import pandas as pd
import yfinance as yf
import pandas as pd
from datetime import datetime

st.title("📊 간단한 Streamlit 대시보드")


ticker = ['GOOG','MSFT','PLTR','TSM','U','TSLA'] #

today_date = datetime.today().strftime('%Y-%m-%d')

data = pd.DataFrame()

for value in ticker:

    info = yf.Ticker(f"{value}").info
    info_df = pd.DataFrame(info)

    desired_columns = ['symbol','shortName','industry','industryKey','industryDisp','sector','sectorKey','sectorDisp',
                'previousClose','fiftyTwoWeekLow','fiftyTwoWeekHigh','fiftyDayAverage','twoHundredDayAverage','currentPrice','targetHighPrice','targetLowPrice','targetMeanPrice','targetMedianPrice',
                'trailingPE','forwardPE','priceToSalesTrailing12Months','priceToBook','bookValue','pegRatio','trailingPegRatio',
                'trailingEps','forwardEps','profitMargins','earningsQuarterlyGrowth','enterpriseToRevenue','enterpriseToEbitda',
                'returnOnEquity','freeCashflow','operatingCashflow','earningsGrowth','revenueGrowth','grossMargins','ebitdaMargins','operatingMargins']
    
    data_list = info_df.reindex(columns=desired_columns)

    data_list.drop_duplicates(inplace=True)
    data_list['date'] = today_date
    data = pd.concat([data, data_list], ignore_index=True)

st.dataframe(data)