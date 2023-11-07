from pandas_datareader import data
import yfinance as yfin
import matplotlib.pyplot as plt
yfin.pdr_override()

df = data.get_data_yahoo('AAPL', start='2022-01-01', end='2022-12-31')

# plot(x, y)
plt.figure(figsize=(5,5))
plt.plot([1,2,3], [10,20,30], color='blue')
plt.xlabel('time')
plt.ylabel('growth')
plt.legend(["career"])
plt.show()

# example
plt.figure(figsize=(5,5))
plt.plot(df.index, df['Close'])
plt.xlabel('time')
plt.ylabel('price')
plt.legend('apple')
plt.show()

# multi line graph
plt.plot([1,2,3],[10,20,30])
plt.plot([4,5,6],[40,50,60])
plt.show()

# bar chart
plt.bar(['A','B','C'], [10,20,30])
plt.show()

# pie chart
plt.pie([10,20,30], labels=['a','b','c'])
plt.show()

# histogram
plt.hist([160,161,168,165,169,170,171,172,180])
plt.show()

# scatter
math = [5,8,23,5,67,34,34,23]
eng = [23,6,3,1,5,45,54,34]
plt.scatter(math,eng)
plt.show()

# stack chart
plt.stackplot(['A','B','C'], [10,20,30], [30,20,50], [10,20,30])
plt.show()