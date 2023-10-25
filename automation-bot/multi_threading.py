import requests
import json
import time
from multiprocessing.dummy import Pool as ThreadPool

url = [
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000",
  "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000"
]

def get_data(url):
    data = requests.get(url)
    data_dict = json.loads(data.content)
    return data_dict['data'][0]['Close']

# 단순반복문 시간 측정
start = time.time()
for i in url:
    get_data(i)
end = time.time()
print(end-start)

# 쓰레드 4개 사용 시간 측정
start = time.time()
pool = ThreadPool(4)
result = map(get_data, url) # map(함수, 리스트)
pool.close()
pool.join()
end = time.time()
print(end-start)

print(list(result))

