from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,'//button[@id="mousehover"]')).perform()

#Right mouse click
action.context_click(driver.find_element(By.LINK_TEXT,'Top')).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,'Reload')).click().perform()