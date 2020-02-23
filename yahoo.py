import urllib.request
from bs4 import BeautifulSoup
import csv
import datetime

def yahoo():
    url = 'https://news.yahoo.co.jp'

    html = urllib.request.urlopen(url)

    # set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")

    mainNewsIndex = soup.find('ul', attrs={"class", "topicsList_main"})
    headlines = mainNewsIndex.find_all("li", attrs={"class", "topicsListItem"})



    for headline in headlines:
        print(headline.a.text)
        print(' → ' + headline.a.get('href'))

    return headlines, 'Yahoo'