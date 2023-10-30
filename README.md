# Python Scripting
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