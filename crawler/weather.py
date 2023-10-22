import csv
import requests
from bs4 import BeautifulSoup

def weather_info():
    data = requests.get("https://weather.naver.com/")
    soup = BeautifulSoup(data.content, 'html.parser')

    weather = dict()
    for i in range(1,3):
        # date
        date = soup.select(f"#weekly > ul > li:nth-child({i}) > div > div.cell_date")[0].text.strip()

        # weather
        day_weather = soup.select(f"#weekly > ul > li:nth-child({i}) > div > div.cell_weather")[0]
        day_morning = day_weather.select(".timeslot")[0].text.strip()
        day_morning_rainfall = day_weather.select(".rainfall")[0].text.strip()
        day_afternoon = day_weather.select(".timeslot")[1].text.strip()
        day_afternoon_rainfall = day_weather.select(".rainfall")[1].text.strip()

        # temperature
        day_temperature_lowest = soup.select(f"#weekly > ul > li:nth-child({i}) > div > div.cell_temperature .lowest")[0].text.strip()
        day_temperature_highest = soup.select(f"#weekly > ul > li:nth-child({i}) > div > div.cell_temperature .highest")[0].text.strip()

        weather[date] = [(day_morning, day_morning_rainfall), (day_afternoon, day_afternoon_rainfall), (day_temperature_lowest, day_temperature_highest)]
    
    return weather

def save_to_csv(info):

    with open('weather_info.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date","morning rainfall","afternoon rainfall","temperature lowest", "temperature highest"])
        for data in info.items():
            weather = f"{data[0]};{data[1][0][0]} {data[1][0][1]};{data[1][1][0]} {data[1][1][1]};{data[1][2][0]};{data[1][2][1]}"
            writer.writerow(weather.split(';'))

if __name__ == "__main__":
    result = weather_info()
    save_to_csv(result)
    print(result)