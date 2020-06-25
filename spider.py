import urllib.request
from bs4 import BeautifulSoup
import requests

url = 'https://www.chinaielts.org/whats_new/ielts_news.shtml'
hrefurl = 'https://www.chinaielts.org'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

res = requests.get(url, headers=headers)
content = res.text

soup = BeautifulSoup(content, 'html.parser')
divs = soup.find_all(class_ = 'title')

for div in divs:

    title = div.a.text.split("发布时间：")[0]
    time = div.a.text.split("发布时间：")[1]
    href = hrefurl + div.a['href']

    print(time)    
    print(title)
    print(href)
    
    print("-----------------------------------")