# Configurations, you should edit these
SB_NAME = 'Master Hearts'   # actual name of the soul break
NUM_FILES = 6               # number of files you want to generate (each file contains 100 friend codes)
FILE_PREFIX = 'sora_aasb'   # name of the file
# Do not edit below here

import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get('https://friends-ffrk.com')
time.sleep(5)
delay = 3
try:
    page_loaded = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sb-dropdown"]')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
sb_select = Select(browser.find_element_by_id('sb-dropdown'))
sb_select.select_by_visible_text(SB_NAME)
try:
    table_processed = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rw-table_processing" and @style="display: none;"]')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
for file_num in range(1, NUM_FILES + 1):
    file_name = FILE_PREFIX + str(file_num) + '.csv'
    with open(file_name, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for page in range(0, 10):
            rw_table = browser.find_element_by_id('rw-table')
            rw_table_body = rw_table.find_element_by_css_selector('tbody')
            for row in rw_table_body.find_elements_by_css_selector('tr'):
                wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
            next_button = browser.find_element_by_id('rw-table_next')
            next_button.click()
            try:
                table_processed = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rw-table_processing" and @style="display: none;"]')))
                print("Page is ready!")
            except TimeoutException:
                print("Loading took too much time!")

browser.quit()