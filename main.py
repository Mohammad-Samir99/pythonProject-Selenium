from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup")

firstname = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'firstName')))
firstname.send_keys("Mohammad")

lastname = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'lastName')))
lastname.send_keys("Sabbah")

username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'Username')))
username.send_keys("Mohammad99")

password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
password.send_keys("19991999")

ConfirmPasswd = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'ConfirmPasswd')))
ConfirmPasswd.send_keys("19991999")

create = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accountDetailsNext"]/div/button')))
# create.click()

# password.send.keys(Keys.ENTER)