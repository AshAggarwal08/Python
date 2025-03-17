import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()

driver.find_element(By.ID, 'autosuggest').send_keys('Ind')
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for i in countries :
    if i.text == 'India':
        i.click()
        break

else :
    print('No desired country found')

# It is not possible to get dynamic text in gettext method hence using get_attribute
assert driver.find_element(By.ID , 'autosuggest').get_attribute('value') == 'India12'