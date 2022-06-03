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

def generate_chem_url(cas):
    urlStart = 'https://pubchem.ncbi.nlm.nih.gov/compound/'
    return urlStart + cas

def scrape_chem_page(css, url):
    service = Service('C:\webdrivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service) 
    driver.get(url)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    return driver.find_element(by=By.CSS_SELECTOR, value=css)

def find_chem_info(cas):
    attributeList = []
    url = generate_chem_url(cas)
    IUPACName = scrape_chem_page("#IUPAC-Name p", url).text
    attributeList.append(IUPACName)
    hazards_parent = scrape_chem_page("#main-content > div > div > div > div.summary.p-md-top.p-md-bottom > div > table > tbody > tr:nth-child(3) > td > a > p", url)
    hazards_children = hazards_parent.find_elements_by_xpath("./child::*")
    hazards_list = []
    for hazard in hazards_children:
        hazards_list.append(hazard.get_attribute("data-caption"))
    attributeList.extend(hazards_list)
    return attributeList


#find_chem_info('106-99-0')
