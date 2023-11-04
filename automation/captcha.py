import requests
from bs4 import BeautifulSoup

# Set header
header = {
    'User-Agent': ''
}
# Set Cooke
cookie = {
}
# Set URL
response = requests.get('URL', headers=header, cookies=cookie)

data = BeautifulSoup(response.content, 'html.parser')

# Set CSS Selector
item = data.select('')

# Get Data
print(item[0].text)
print(response.status_code)