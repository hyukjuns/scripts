import pandas as pd

df = pd.read_csv('credit.csv')

# data = df.groupby('소득')
# print(data.describe())

df = df.replace('$120K +', 120)
df = df.replace('$40K - $60K', 50)
df = df.replace('$60K - $80K', 70)
df = df.replace('$80K - $120K', 100)
df = df.replace('Less than $40K', 40)
df = df.replace('Unknown', 40)

data = df[['소득', '사용금액']].corr()
print(data)

