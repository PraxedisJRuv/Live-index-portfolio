import pandas as pd

def full_dataframe_extraction(tickers,start, end):
    flag=True
    for ticker in tickers:
        url=f"https://stooq.com/q/d/l/?s={ticker}&d1={start:%Y%m%d}&d2={end:%Y%m%d}&i=d"
        df_temp=(pd.read_csv(url,parse_dates=["Date"])
            .set_index("Date")
            .sort_index())
        df_temp.columns = [f"{ticker} Open", f"{ticker} High", f"{ticker} Low", f"{ticker} Close", f"{ticker} Volume"]
        if flag:
            data=df_temp
            flag =False
        else:
            data=data.join(df_temp)
    return data