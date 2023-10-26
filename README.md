# Python Scripting
### Selinium
```
# 요소찾기
driver.find_element_by_css_selector('.class명')
driver.find_element_by_css_selector('#id명')
driver.find_element_by_css_selector('태그명[속성이름="속성명"]')
driver.find_element(By.CSS_SELECTOR,'.class명')
driver.find_element(By.CSS_SELECTOR,'#id명')

# 복수 요소
driver.find_elements_by_css_selector('.class명')[X]
driver.find_elements(By.CSS_SELECTOR, '.class명')[X] #위 문법이 안될 경우
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