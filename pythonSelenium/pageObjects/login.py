from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.shop import ShopPage
from pythonSelenium.utils.browser_utils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'signInBtn')

    def loginfunc(self, username , password):
        # click on login. * here unpacks the tuple
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        shop_page = ShopPage(self.driver) #create object of next page class
        return shop_page