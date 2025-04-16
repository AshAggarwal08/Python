import time
from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

#click on Shop
driver.find_element(By.CSS_SELECTOR,'a[href*="shop"]').click()
driver.implicitly_wait(5)

#find all products
all_products = driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

#in these all products, search desired product.
#product.findelement is used NOT driver.findelement because we are using chaining
#Try to traverse to product name and add button from //div[@class="card h-100"]
for product in all_products :
    productName = product.find_element(By.XPATH,'div/h4').text
    if productName == 'Blackberry':
        product.find_element(By.XPATH,'div/button').click()

driver.find_element(By.CSS_SELECTOR,'.nav-link.btn.btn-primary').click()
driver.find_element(By.CSS_SELECTOR,'button[class="btn btn-success"]').click()

driver.find_element(By.ID,'country').send_keys('Ind')
wait = WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
success_msg= driver.find_element(By.CSS_SELECTOR,'.alert-success').text

assert "Success! Thank you!" in success_msg
time.sleep(3)
driver.close()


