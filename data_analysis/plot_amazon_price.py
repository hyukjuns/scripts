from pandas_datareader import data
import yfinance as yfin
import matplotlib.pyplot as plt
yfin.pdr_override()

df = data.get_data_yahoo('AMZN', start='2020-01-01', end='2020-12-31')

# Make data (rolling = window slice)
df['rolling20'] = df['Close'].rolling(20).mean()
df['rolling60'] = df['Close'].rolling(60).mean()

# Draw plot graph
plt.figure(figsize=(5,5))
plt.xlabel('date')
plt.ylabel('price')
plt.plot(df.index, df['rolling20'])
plt.plot(df.index, df['rolling60'])
plt.legend(["rolling20", "rolling60"])
plt.show()

