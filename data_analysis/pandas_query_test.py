import pandas as pd

df = pd.read_csv('credit.csv')

married_spend = df.query(" 기혼 == 'Married' and 성별 == 'M' ")['사용금액']
print(married_spend.mean())

un_married_sped = df.query(" (기혼 == 'Single' or 기혼 == 'Unknown') and 성별 == 'M' ")['사용금액']
print(un_married_sped.mean())
