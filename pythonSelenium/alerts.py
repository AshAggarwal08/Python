from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

name = 'TestUser'
driver.find_element(By.CSS_SELECTOR,'#name').send_keys(name)

driver.find_element(By.ID,'alertbtn').click()
alert_box = driver.switch_to.alert
alert_text = alert_box.text
print(alert_text)

assert name in alert_text
alert_box.accept()

