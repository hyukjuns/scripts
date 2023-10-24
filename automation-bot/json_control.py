import json
import requests
import time


data = requests.get('<URL>')
# print(data.content)

# json.loads -> json to dictionary
json_data = json.loads(data.content)
for i in range(0,200):
    # epoch to localtime
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json_data['body']['candles'][i]['dt']/1000))
    print(date)
    print(json_data['body']['candles'][i]['close'])