import feedparser
from bs4 import BeautifulSoup
import requests

d = feedparser.parse("https://www.financialreporter.co.uk/rss.asp?v=1")

for post in d.entries:
    print(post.link)
    print(post.title)
    req = requests.get(post.link)
    htmlParse = BeautifulSoup(req.text, "html.parser")
    for para in htmlParse.find_all("p"):
        print(para.get_text())
        print("**************")
    
