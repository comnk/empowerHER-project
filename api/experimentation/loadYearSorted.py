from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from requests.exceptions import ConnectionError
from selenium import webdriver
import chromedriver_autoinstaller



# link: https://csrankings.org/#/index?all&us
def scrape_professors():
  # Automatically install chromedriver
  chromedriver_autoinstaller.install()

  # Initialize the WebDriver for Chrome
  driver = webdriver.Chrome()

  # Open Google search page
  driver.get("https://csrankings.org/#/index?all&us")
  driver.implicitly_wait(30) # Wait implicitly for elements to be ready

  
  html_page = open("./profListings/scholar.html", "r")
  soup = BeautifulSoup(html_page, "lxml")
  
  # print(soup)
  
  all_links = soup.find_all('a')
  
  text = 'Year'
  
  targetLink = None
 
  # we will search the tag with in which text is same as given text
  for i in all_links:
    # print(i.string)
    if(i.string == text):
      targetLink = i
      break
  
  yearSortedPage = targetLink['href']
  print(yearSortedPage)
  
  # print(prof_divs)
  # for div in prof_divs:
  #   content = div.get_text()
  #   print(content)

if __name__=="__main__": 
  scrape_professors()