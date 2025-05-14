import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pythonSelenium.utils.browser_utils import BrowserUtils


class PurchasePage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.country= (By.ID, 'country')
        self.country_click = (By.CSS_SELECTOR, 'div[class="suggestions"]')
        self.checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
        self.submit = (By.XPATH, '//input[@type="submit"]')
        self.success = (By.CSS_SELECTOR, '.alert-success')


    def purchase(self, country_name):
        self.driver.find_element(*self.country).send_keys(country_name)

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located(self.country_click)) #no need to unpack with *self

        self.driver.find_element(*self.country_click).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()
        success_msg = self.driver.find_element(*self.success).text

        assert "Success! Thank you!" in success_msg
        time.sleep(3)