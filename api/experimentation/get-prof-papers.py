import csv
import pandas as pd
import requests, bs4
from bs4 import BeautifulSoup
from scholarly import scholarly, ProxyGenerator

source_df = pd.read_csv("./csrankings/csrankings.csv")

# all google scholar ids needing to be scraped
profs_df = {}
for index, row in source_df.iterrows():
    profs_df[row['name']] = {}
    if row['scholarid'] != 'NOSCHOLARPAGE':
        profs_df[row['name']]['gs-url'] = "https://scholar.google.com/citations?user=" + row['scholarid'] + "&hl=en&oi=ao"
        profs_df[row['name']]['scholar-id'] = row['scholarid']

# get 1. all abstract text, 2. most recent papers, 3. best papers by citation
count = 0
# pg = ProxyGenerator() # set up proxy for google scholar
# pg.FreeProxies()
# scholarly.use_proxy(pg)
for name in profs_df.keys():
    if 'scholar-id' in profs_df[name]: # has google scholar link
        print(profs_df[name]['scholar-id'])
        author = scholarly.search_author_id(profs_df[name]['scholar-id'])
        scholarly.pprint(author)
        # print(author.fill())
        # print("!")
        print(author.publications)
        # url = profs_df[name]['gs-url']
        # req = requests.get(url)
        # soup = BeautifulSoup(req.content, features='lxml')
        # print(soup)
        # paper_divs = soup.find_all('div', class_='gsc_a_t')
        # for paper in paper_divs:
        #     print(paper)
    # profs_df[name]['abstracts'] = ":3"

    count += 1 # stop after X profs
    if count >= 1:
        break
