import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#Id , xpath , css , linktext, Classname

driver.find_element(By.NAME, 'email').send_keys("helo@gmail.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()


# Xpath = //tagname[@attribute='value']

driver.find_element(By.XPATH,'//input[@type="submit"]').click()
msg = driver.find_element(By.CLASS_NAME,"alert-success").text
print(msg)

# if msg == 'Success! The Form has been submitted successfully!.':
#     print('successfully loggedin')
#     print('hi')
#
# else:
#     print('unsuccessful login')


# CSS = tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,'input[name="name"]')
assert "Success" in msg

driver.find_element(By.CSS_SELECTOR,'#inlineRadio2').click()
time.sleep(2)