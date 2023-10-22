import csv
import requests
from bs4 import BeautifulSoup

def ranking_news(category):
    data = requests.get(f"https://sports.naver.com/{category}/index")
    soup = BeautifulSoup(data.content, 'html.parser')
    rankings = soup.select('ol.news_list li')

    news = dict()
    for rank in rankings:
        number = rank.select('span.number')[0].text
        title = rank.select('a')[0].text
        news_url = f"https://sports.naver.com{rank.select('a')[0].get('href')}"
        news[number] = (title, news_url)
    
    return news

if __name__ == "__main__":

    # 스포츠 종목 입력
    user_input = int(input("스포츠 종목을 입력하세요.\n1: 야구\n2: 해외야구\n3: 축구\n4: 해외축구\n5: 농구\n6: 배구\n7: 골프\n8: 일반\n>> "))
    sports_keywords = {1: "kbaseball",
              2: "wbaseball",
              3: "kfootball",
              4: "wfootball",
              5: "basketball",
              6: "volleyball",
              7: "golf",
              8: "general"}
    if user_input in sports_keywords.keys():
        category = sports_keywords.get(user_input)
    else:
        category = sports_keywords.get(8)

    # 실시간 순의 뉴스 검색 (1~10위)
    rankings = ranking_news(category)

    # 파일에 쓰고 종료
    targets = list(rankings.items())
    with open('news.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',escapechar='"')
        writer.writerow(["number", "title", "url"])
        for target in targets: 
            strings = f"{target[0]};{target[1][0]};{target[1][1]}"
            writer.writerow(strings.split(';'))
