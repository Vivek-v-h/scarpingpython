import requests
import time
from fake_useragent import UserAgent
url="https://www.ft.com/content/4bf40350-ea4f-4b24-b8a1-c85d9277e6cc"
session=requests.Session()

headers={
    'User-Agent':UserAgent().random,
    'Accept-Language':'en-Us,en;q=0.9',
    'Accept-Encoding':'gzip,deflate,br',
    'Connection':'keep-alive',
    'Referer':'https://www.google.com'
}

r=session.get(url)
#print(r.text)

with open("file.html","w", encoding="utf-8") as f:
    f.write(r.text)