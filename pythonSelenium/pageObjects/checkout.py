from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.purchase import PurchasePage
from pythonSelenium.utils.browser_utils import BrowserUtils


class CheckoutPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, '//button[@class="btn btn-success"]')


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        purchase_page = PurchasePage(self.driver)
        return purchase_page

