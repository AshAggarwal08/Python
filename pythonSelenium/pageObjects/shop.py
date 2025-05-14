from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.checkout import CheckoutPage
from pythonSelenium.utils.browser_utils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)   #this will call parent class constructor
        self.driver = driver
        self.shop_click = (By.CSS_SELECTOR, 'a[href*="shop"]')
        self.all_products = (By.XPATH, '//div[@class="card h-100"]')
        self.cart_click = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')


    def add_to_cart(self,product_name):
        # click on Shop
        self.driver.find_element(*self.shop_click).click()
        # find all products
        products = self.driver.find_elements(*self.all_products)

        # in these all products, search desired product.
        # product.findelement is used NOT driver.findelement because we are using chaining
        # Try to traverse to product name and add button from //div[@class="card h-100"]
        for product in products:
            productName = product.find_element(By.XPATH, 'div/h4/a').text
            if productName == product_name:
                product.find_element(By.XPATH, 'div/button').click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_click).click()

        checkout_page = CheckoutPage(self.driver)
        return checkout_page
