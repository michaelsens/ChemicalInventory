from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Chrome
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

#Retrieving the website data
service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
url = 'https://pubchem.ncbi.nlm.nih.gov/compound/106-99-0'
driver.get(url)

#finding IUPAC Name
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#IUPAC-Name p"))) #
IUPACName = (driver.find_element(by=By.CSS_SELECTOR, value="#IUPAC-Name p")).text

print(IUPACName)
