## Python Scripts
### python setup
```
# Setting venv
python3 -m venv .venv
source .venv/bin/activate
python -V
which python

# Setting vscode interpreter

# Disable venv
deactivate
```

### pandas_datareader, matplotlib
- pandas_datareader: Get Data from external
- matplotlib: Draw plot, bar, pie, scatter, stackplot
```
# pandas_datareader
from pandas_datareader import data

# 이동평균선 (rolling = window slice)
df.rolling(NUMBER).mean() # NUMBER 간격으로 평균 구하기

# matplotlib
import matplotlib.pyplot as plt

# plot(x, y)
plt.figure(figsize=(5,5))
plt.plot([1,2,3], [10,20,30], color='blue')
plt.xlabel('time')
plt.ylabel('growth')
plt.legend(["career"])
plt.show()

```

### regex
```
# re.search > return obejct
# re.findall > return list

# re.sub > replace, return list
# Ex: 2023-10-10 to 2023.10.10
re.sub('target', 'change', 'string')

# ^시작문자, 끝문자$, \특수문자
# [abc]: a or b or c, [a-zA-Z]
^: start
$: end
\: escape

# [^abc] : Not, a or b or c가 아닌것
# \d: digit, 모든숫자, 2자리: \d\d, 3자리: \d{3}, 숫자가아님: \D, 스페이스바검색: \s, 스페이스가 아닌것 \S(모든문자)
# a+ : a 라는 숫자 반복해서 찾음
# case insensitive: re.findall('kw','string', re.IGNORECASE)
[]: or
[^]: Not
+: iter
re.IGNORECASE: case insensitive
```

### Pandas
```
# Package
import pandas as pd

# Dataframe(as df) = Matrix
# Series = List

# Group by
df.groupby('컬럼')

# Correlation, 상관관계
# 0에 수렴: 상관없음, 1에 수렴: 정비례, -1에 수렴: 반비례
df[['컬럼1','컬럼2']].corr()
df[['사용금액','사용횟수']].corr()

# Filter(Condition), query
df[ CONDITION ]
df.query("QUERY")

# Excel (.xlsx)
import openpyxl

# apply: df['컬럼'].apply(함수)
def include_tax(data):
    return data * 1.1

raw_data['부가세포함'] = raw_data['판매가'].apply(include_tax)

# regex
import re
re.search('Keyword', 'Sentence') # return Object or None
```
### Send Mail
```
# Package
import smtplib
from email.mime.text import MIMEText

# Login > ID, Application PW (MFA 우회)
```
### mssql connect
[Prerequisites](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver16&tabs=linux#install-the-odbc-driver)
```
# Required Driver & Package
- driver: Microsoft ODBC 17 [18]
- pakage: pyodbc
```
### Azure Connect
```
# Required Package
azure-mgmt-resource>=18.0.0
azure-identity>=1.5.0
```

### requests - header, cookie
```
import requests
header = {
    'User-Agent': '<USER_AGENT>'
}
cookie = {
    <COOKIE>
}
response = requests.get('URL', headers=header, cookies=cookie)
```

### Installing pip
```
# Install
python3 -m pip install --user --upgrade pip
python3 -m pip --version

# Upgrade
python -m pip install --upgrade pip

```
### venv
```
# 가상환경 셋업 (파이썬 내장모듈 > venv 사용)
# python -m venv <디렉터리>
python -m venv .venv

# enable venv
. .venv/bin/activate
# 혹은
source .venv/bin/activate

# disable venv
deactivate

# check venv alright (python should be in .venv path)
which python
> /Users/hyukjun/github/python-scripts/automation-bot/.venv/bin/python3

# installing packages
python -m pip install <LIBRARARY> ['<LIBRARARY==VERSION>']

# Freezing and Re-Installing packages
# Freeze pacakge and save to requirements.txt
python -m pip freeze > requirements.txt

# Re-Installing packages
python -m pip install -r requirements.txt

# Uninstall package
python -m pip uninstall <PACKAGENAME> [--all]
```
### Selinium
웹개발시 로그인기능/글발행기능 등을 자동화하여 테스트 하기 위한 라이브러리로서 탄생, 현재 데이터수집에 활용
```
# chromedriver 준비
https://chromedriver.chromium.org/downloads

# 패키지설치
python -m pip install selenium==4.11.2

# 기본 사용법
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://kubernetes.io/docs/home/')

# 요소찾기
driver.find_element_by_css_selector('태그명[속성이름="속성명"]')
driver.find_element(By.CSS_SELECTOR,'.class명')
driver.find_element(By.CSS_SELECTOR,'#id명')
driver.find_element(By.CSS_SELECTOR,'태그명[속성이름="속성명"]')

# 복수 요소
driver.find_elements(By.CSS_SELECTOR, '.class명')[X]

# 클릭/입력
driver.find_element(By.CSS_SELECTOR,'.class명').click()
driver.find_element(By.CSS_SELECTOR,'.class명').send_keys('codingapple_test')
driver.find_element(By.CSS_SELECTOR,'.class명').send_keys(Keys.ENTER)  #엔터키입력

# 강제 클릭
e = driver.find_element(By.CSS_SELECTOR,'클릭하고싶은요소')
driver.execute_script('arguments[0].click();', e)

```
### MultiThread
```
# Multi Processing vs Multi Threading
- Multi Processing

    파이썬 프로세스를 병렬로 실행

- Multi Threading

    CPU를 병렬로 사용

- 주의점

    하나의 변수를 처리할 경우, lock 현상으로 인해 큰 효과를 거두지 못할 수 있음

```
### map
```
# 리스트 각 요소에 반복 연산이 필요할 경우
# map(리스트 각 요소에 적용할 함수, 리스트)
result = map(add, target)
```

### json
```
# get json data
data = requests.get(<URL>)

# json to dictionary
json_data = json.loads(data.content)
```

### Time
```
import time
import datetime

# epoch time
time_data = time.time()
print(time_data)

# epoch to localtime
time_data = time.ctime()
print(time_data)

# easy time
time_data = datetime.datetime.now()
print(time_data)
```

### HTML Parsing - selector
```
soup.select('.class명')
soup.select('#id명')
soup.select('태그명') (HTML 태그명은 아무것도 안붙임)
soup.select('.class명1 .class명2') (띄어쓰기는 '~내부의' 라는 뜻)
```

### HTML Parsing - find_all
```
# find_all ('태그', '속성')
val = soup.find_all("em", id="now_value")[0].text

# class로 찾을때 > class_
print(soup.find_all('td', class_="td"))
```

## Ref.
[selenium docs](https://selenium-python.readthedocs.io/)

[Webdriver API](https://selenium-python.readthedocs.io/api.html)

[chromedriver](https://chromedriver.chromium.org/downloads)

[Python Packaging User Guide](https://packaging.python.org/en/latest/)

[VENV and PIP](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)