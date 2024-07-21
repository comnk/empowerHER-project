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
from selenium.common.exceptions import TimeoutException
from requests.exceptions import ConnectionError
from selenium import webdriver
import chromedriver_autoinstaller

# chromedriver_autoinstaller.install() # automatically install chromedriver
driver = webdriver.Chrome() # initialize the WebDriver for Chrome

# url suffixes
most_recent_suffix = "&view_op=list_works&sortby=pubdate"

csrankings_df = pd.read_csv("./csrankings/csrankings.csv")
count = 0
for index, row in csrankings_df.iterrows():
    count += 1
    if count % 30 == 0: # get first X pages
        time.sleep(10)
    if row['scholarid'] == 'NOSCHOLARPAGE':
        continue
    # has google scholar page
    website_url = "https://scholar.google.com/citations?user=" + row['scholarid'] 
    fileName = "./profListings/scholar-" + row['scholarid']  +".html"

    driver.implicitly_wait(200) # Wait implicitly for elements to be ready
    # Open Google search page
    driver.get(website_url)
    driver.implicitly_wait(200) # Wait implicitly for elements to be ready

    try:
        driver.implicitly_wait(200) # Wait implicitly for elements to be ready
        pageSource = driver.page_source
        driver.implicitly_wait(200) # Wait implicitly for elements to be ready
    except ConnectionResetError:
        print("Connection reset error")
        continue
    except Exception as e:
        print("An error occurred" + str(e))
        continue

    file = open(fileName, "w")
    
    file.write(pageSource)
    file.close()
    time.sleep(1)


driver.quit()


# Locate the search box, enter the search query, and submit
# Wait for the results to load
# searchBox = driver.find_element(By.CLASS_NAME, "csr-chart")
# driver.implicitly_wait(20)  
# print(searchBox)
# driver.implicitly_wait(20)  



