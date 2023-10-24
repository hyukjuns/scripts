# Python Scripting

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

#### CSS Selector
```
soup.select('.class명')
soup.select('#id명')
soup.select('태그명') (HTML 태그명은 아무것도 안붙임)
soup.select('.class명1 .class명2') (띄어쓰기는 '~내부의' 라는 뜻)
```

#### Find all
```
# find_all ('태그', '속성')
val = soup.find_all("em", id="now_value")[0].text

# class로 찾을때 > class_
print(soup.find_all('td', class_="td"))
```