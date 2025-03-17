import time
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5) #saves remaining time if object identified early
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
print(driver.title)


driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys('ber')

time.sleep(2) #this is used for find elements here. It will help load list
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
len = len(products)
print(len)
assert len > 0

for product in products:
    product.find_element(By.XPATH,"div/button").click() #chaining of locators

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[.='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()