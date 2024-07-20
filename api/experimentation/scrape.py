import pandas as pd

# webscraping
import requests
import bs4
from bs4 import BeautifulSoup

# link: https://csrankings.org/#/index?all&us
def scrape_professors():
  # get contents of web page
  # url = "https://csrankings.org/#/index?all&us"
  # req = requests.get(url)
  
  # soup = BeautifulSoup(req.content, features='lxml')
  
  html_page = open("./profListings/home.html", "r")
  soup = BeautifulSoup(html_page, "lxml")
  
  # print(soup)
  
  prof_divs = soup.find_all('div', class_='csr-chart')
  
  print(f"{len(prof_divs)} found")
  # print(prof_divs)
  # for div in prof_divs:
  #   content = div.get_text()
  #   print(content)

if __name__=="__main__": 
  scrape_professors()