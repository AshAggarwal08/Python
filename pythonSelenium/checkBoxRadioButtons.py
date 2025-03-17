import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkboxes))

for i in checkboxes :
    if i.get_attribute('value') ==  'option2':
        print('Found Option2')
        i.click()
        assert i.is_selected()  #returns false if not selected
        time.sleep(1)
        break

radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radios))

for radio in radios :
    if radio.get_attribute('value') == 'radio3':
        radio.click()
        #assert radio.is_selected()
        time.sleep(2)
    break

#is displayed

assert driver.find_element(By.ID,'displayed-text').is_displayed()

driver.find_element(By.ID,'hide-textbox').click()
assert not driver.find_element(By.ID,'displayed-text').is_displayed() #Return true if failed

driver.find_element(By.ID, 'show-textbox').click()
assert driver.find_element(By.ID,'displayed-text').is_displayed()

