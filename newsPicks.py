import urllib.request
from bs4 import BeautifulSoup

def newspicks():
    # url
    url = "https://newspicks.com/"

    # get html
    html = urllib.request.urlopen(url)

    # set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # get headlines
    mainNewsIndex = soup.find("div", attrs={"class", "latest-news"})
    headlines = mainNewsIndex.find_all("a", attrs={"class", "news-title-list"})


    # print headlines
    for headline in headlines:
        print(headline.text)
        print(' → ' + url[:-1] + headline.get('href'))

    return headlines, 'newsPicks'