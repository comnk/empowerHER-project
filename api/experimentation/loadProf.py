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



# Automatically install chromedriver
chromedriver_autoinstaller.install()

# Initialize the WebDriver for Chrome
driver = webdriver.Chrome()
# website = "https://csrankings.org/#/index?all&us"
website = "https://scholar.google.com/citations?hl=en&user=V5-wYX0AAAAJ&view_op=list_works&sortby=pubdate"
fileName = "./profListings/scholar.html"

# Open Google search page
driver.get(website)
driver.implicitly_wait(20) # Wait implicitly for elements to be ready

# Locate the search box, enter the search query, and submit
# Wait for the results to load
# searchBox = driver.find_element(By.CLASS_NAME, "csr-chart")
# driver.implicitly_wait(20)  
# print(searchBox)
# driver.implicitly_wait(20)  


try:
    pageSource = driver.page_source
    fileToWrite = open(fileName, "w")
    fileToWrite.write(pageSource)
    fileToWrite.close()
except ConnectionResetError:
    print("Connection reset error")
    pass
except Exception as e:
    print("An error occurred" + str(e))
    pass
finally:
    driver.quit()

