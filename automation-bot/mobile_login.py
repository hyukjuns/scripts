import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip

# get naver login page
driver = webdriver.Chrome()
driver.get('URL')

# login (input id/pw)
driver.implicitly_wait(3)
pyperclip.copy('myid')
driver.find_element(By.CSS_SELECTOR, '#id').send_keys(Keys.COMMAND, 'v')

pyperclip.copy('mypw!')
driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.COMMAND, 'v')

btn_login = driver.find_element(By.CSS_SELECTOR, 'button[id="log.login"]')
btn_login.click()
time.sleep(5)
