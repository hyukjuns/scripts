import pandas as pd

df = pd.read_csv('credit.csv')

# Correlation > corr()
# 0에 수렴: 상관없음, 1에 수렴: 정비례, -1에 수렴: 반비례
corr = df[['사용금액', '사용횟수']].corr()
print(corr)

# Filter - simple
print(df[df['나이'] > 50])
print(df[df['사용금액'] < 1000])
# Filter - query
print(df.query("성별 == 'M' and 기혼 == 'Married'").describe())

# Raw data to dataframe
raw_data = {
    'Goal': [10,8,9],
    'Assist': [10,10,15],
    'Save': [4,7,1]
}
data = pd.DataFrame(raw_data)
print(data)

