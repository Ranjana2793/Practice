from flask import Flask
import feedparser
from bs4 import BeautifulSoup
import requests



app = Flask(__name__)

@app.route("/articles/<string:title>/")
def getArticles(title):
    d = feedparser.parse("https://www.financialreporter.co.uk/rss.asp?v=1")
    titlename=""
    for post in d.entries:
        print(post.title)
        if title in post.title:
            titlename=post.title
    return titlename

if __name__ == "__main__":
    app.run()

