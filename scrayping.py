import urllib.request
from bs4 import BeautifulSoup
import csv
import datetime

import newsPicks
import yahoo
import yomiuri

def scraping():
    print("----------NewsPicks----------------")
    headlines, where = newsPicks.newspicks()
    copy_to_csv_newpics(headlines, 'newspicks')

    print("----------Yahoo!-------------------")
    headlines, where = yahoo.yahoo()
    copy_to_csv(headlines, where)

    print("----------読売!-------------------")
    headlines, where = yomiuri.yomiuri()
    copy_to_csv(headlines, where)


def copy_to_csv(datas, where):
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow([datetime.datetime.today(), where, data.a.text, data.a.get('href')])


def copy_to_csv_newpics(datas, where):
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow([datetime.datetime.today(), where, data.text, data.get('href')])

if __name__ == "__main__":
    scraping()
