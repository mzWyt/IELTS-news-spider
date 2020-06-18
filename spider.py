import requests

url = 'https://weibo.com/ieltscn/'

res = requests.get(url)
rslt = res.content.decode("utf8","ignore")
print(rslt)