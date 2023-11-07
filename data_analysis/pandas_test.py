import pandas as pd

# df = dataframe
df = pd.read_csv('credit.csv')

print(df)
print(df['나이'].mean())
print(df['학력'].mode())
print(df['사용금액'].max())
print(df['사용금액'].min())
print(df[['사용금액','사용횟수']].describe())
print(df.groupby('성별').max())

print(df['사용금액'].plot())