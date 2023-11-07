from pandas_datareader import data
import yfinance as yfin
import matplotlib.pyplot as plt
yfin.pdr_override()

# bit coin price between 2020.01~12 
df = data.get_data_yahoo('BTC-USD', start='2020-01-01', end='2020-12-31')
print(df)

# Volume > mean(Volume)
mean_volume = df['Volume'].mean()
result = df.query(f"Volume > {mean_volume}")['Close']
print(result.index)

# Draw Bar Graph by plt
plt.figure(figsize=(5,5))
plt.bar(result.index, result)
plt.show()

