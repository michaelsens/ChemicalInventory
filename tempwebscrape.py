from re import I
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

def scrape(css):
    service = Service('C:\webdrivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    url = 'https://pubchem.ncbi.nlm.nih.gov/compound/106-99-0'
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    return driver.find_element(by=By.CSS_SELECTOR, value=css).text

IUPACName = scrape("#IUPAC-Name p")
