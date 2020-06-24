import urllib.request
from bs4 import BeautifulSoup
import requests

url = 'https://ielts.neea.edu.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

res = requests.get(url, headers=headers)
content = res.text
soup = BeautifulSoup(content, 'html.parser')

print(soup)

# divs = soup.find_all(class_ = 'margin-top: -.2em;')
# print(divs)