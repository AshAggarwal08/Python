from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,'Forgot password?').click()
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys('demo@gmail.com')
driver.find_element(By.CSS_SELECTOR,"input[type='Password']").send_keys('Hello@1234')
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys('Hello@1234')
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()


#Static Dropdown

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, 'email').send_keys("helo@gmail.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()

###Static Dropdown
dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
dropdown.select_by_index(0)
dropdown.select_by_visible_text('Female')



