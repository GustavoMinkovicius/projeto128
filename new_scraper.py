from cmath import exp
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome('C:/Users/user/OneDrive/Área de Trabalho/programa/projeto127/chromedriver.exe')
browser.get(START_URL)

time.sleep(5)

page = requests.get(START_URL)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all('table', attrs={'class': 'wikitable sortable jquery-tablesorter'})
temp_list = []
tr_tags = table.find_all('tr')

for table in enumerate(tr_tags):
    try:
        temp_list.append(table.find_all('td'))
    except:
        temp_list.append('')

new_scraper = pd.DataFrame(temp_list)
new_scraper.to_csv('new_scraped_data.csv', index = True, index_lable='id')