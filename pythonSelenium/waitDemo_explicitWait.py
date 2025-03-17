import time
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(1) #saves remaining time if object identified early. implicit wait is global
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
print(driver.title)


driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys('ber')

time.sleep(2) #this is used for find elements here. It will help load list
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")

productNames = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
names=[]
for name in productNames:
    names = name.text
    print(names)



#Total items displayed after search
len = len(products)
print(len)
assert len > 0

for product in products:
    product.find_element(By.XPATH,"div/button").click() #chaining of locators

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[.='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys('rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()

waitobj = WebDriverWait(driver,10)
waitobj.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.promoInfo')))

promomsg = driver.find_element(By.CSS_SELECTOR, '.promoInfo').text

assert 'Code applied' in promomsg
print(promomsg)


#Summing up the total of items
Amounts = driver.find_elements(By.CSS_SELECTOR,'td:nth-child(5) p')
print(Amounts)
total = 0
for amount in Amounts:
    total = total + int(amount.text)  #48+160+180
print(total)

#Compare the expected amount with actual
ExpectedAmt = int(driver.find_element(By.XPATH,'//span[@class="totAmt"]').text)

assert ExpectedAmt == total

#Verifying discount amount is always less than total amount
discAmt = float(driver.find_element(By.CSS_SELECTOR,'.discountAmt').text)
print(discAmt)

assert discAmt < total

#Verify if products on checkout are same as products searched
finalProducts = driver.find_elements(By.CSS_SELECTOR,'.product-name')
for final in finalProducts:
    f = final.text
    print(f)

assert names == f

