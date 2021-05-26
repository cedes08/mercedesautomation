from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get("https://facebook.com")
driver.maximize_window()

usernametb = driver.find_element_by_id('email').send_keys('superagent@geeksnest')
time.sleep(5)

passwordtb = driver.find_element_by_id('pass').send_keys('Tester2021!')
time.sleep(5)

loginbtn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
loginbtn.click()

