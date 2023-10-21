import requests
from bs4 import BeautifulSoup

# find_all ('태그', '속성')
# val = soup.find_all("em", id="now_value")[0].text

# class로 찾을때 > class_
# print(soup.find_all('td', class_="td"))

# css select: class > . | id > #
# print(soup.select('#chart_1')[0].text)

def kospi(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    # id
    val = soup.find_all("em", id="now_value")[0].text
    # class
    print(soup.find_all('td', class_="td"))
    return val

if __name__=="__main__":
    url = 'https://finance.naver.com/sise/sise_index.naver?code=KOSPI'
    kospi_nowvalue = kospi(url)
    f = open("kospi_nowvalue.txt", 'w')
    f.write(kospi_nowvalue)
    f.close
