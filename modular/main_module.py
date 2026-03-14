import pandas as pd
from datetime import datetime, timedelta
from extraction import full_dataframe_extraction
import benchmarks as bm
import portfolio as port
tickers = ["AAPL.US","MSFT.US"]
end=datetime.today()
start=end-timedelta(days=2*365)
df=full_dataframe_extraction(tickers, start, end)
period=pd.Timedelta("2W")
#ew=bm.calc_EW(tickers,period)
#print(ew)
vola=bm.calc_vola(df,tickers,period)
print(vola)
portafolio=port.portfolio_value(vola,df,period,tickers)
print(portafolio)
