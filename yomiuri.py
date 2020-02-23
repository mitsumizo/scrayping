import urllib.request
from bs4 import BeautifulSoup
import csv
import datetime

def yomiuri():
    # url
    url = "https://www.yomiuri.co.jp/"

    # get html
    html = urllib.request.urlopen(url)

    # set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # get headlines
    mainNewsIndex = soup.find("ul", attrs={"class", "p-category-latest-sec-list"})
    headlines = mainNewsIndex.find_all("h3", attrs={"class", "c-list-title"})



    # print headlines
    for headline in headlines:
        print(headline.a.text)
        print(' → ' + headline.a.get('href'))

    return headlines, 'yomiuri'