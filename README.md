## Web Crawler, Find HTML element
### CSS Selector
```
soup.select('.class명')
soup.select('#id명')
soup.select('태그명') (HTML 태그명은 아무것도 안붙임)
soup.select('.class명1 .class명2') (띄어쓰기는 '~내부의' 라는 뜻)
```

### Find all
```
# find_all ('태그', '속성')
val = soup.find_all("em", id="now_value")[0].text

# class로 찾을때 > class_
print(soup.find_all('td', class_="td"))
```