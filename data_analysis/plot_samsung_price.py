import pandas as pd
import matplotlib.pyplot as plt

# Read Data
data = {}
with open('price.csv', 'r') as file:
    columns = file.readline().rstrip().split(',')
    for column in columns:
        data[column] = []
    for line in file:
        items = line.rstrip().split(',')
        data['Date'].append(items[0])
        data['Samsung'].append(items[1])
        data['LG'].append(items[2])
print(data)

# Make pandas dataframe
df = pd.DataFrame(data, index=data['Date'])
print(df)

# Visualization
plt.figure(figsize=(5,5))
plt.plot(df.index, df['Samsung'], color='blue')
plt.plot(df.index, df['LG'], color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(['Samsung', 'LG'])
plt.show()

# pandas read csv
df2 = pd.read_csv('price.csv', index_col='Date')
print(df2)