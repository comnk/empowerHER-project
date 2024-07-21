import pandas as pd

# webscraping
import requests
import bs4
from bs4 import BeautifulSoup

# link: https://csrankings.org/#/index?all&us
def scrape_professors():
  # get contents of web page
  
  # url = "https://scholar.google.com/citations?hl=en&user=V5-wYX0AAAAJ&view_op=list_works&sortby=pubdate"
  # req = requests.get(url)
  # soup = BeautifulSoup(req.content, features='lxml')
  
  html_page = open("./profListings/scholar.html", "r")
  soup = BeautifulSoup(html_page, "lxml")
  
  # print(soup)
  
  # print(soup)
  
  all_papers = soup.find_all('a', class_='gsc_a_at')
  
  topPapers = all_papers[0:3]
  
  for paper in topPapers:
    print(paper.get_text())
  
  # print(prof_divs)
  # for div in prof_divs:
  #   content = div.get_text()
  #   print(content)

if __name__=="__main__": 
  scrape_professors()