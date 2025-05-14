import json
import os
import sys

import pytest

from pythonSelenium.pageObjects.login import LoginPage
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)  #convert json to python object
    test_list = test_data['data'] #list

@pytest.mark.smoke()
#fixture to run with multiple data.
# test_input is variable. It keeps pushing test list data in input. Test will run twice

@pytest.mark.parametrize("test_input",test_list)

def test_e2e(browserInstance, test_input):
    driver = browserInstance
    driver.maximize_window()

    #Create the class's object and then call the login method from pageObjects.
    #sending driver as a parameter is necessary for constructor to work
    lp = LoginPage(driver)
    print(lp.get_title()) #get_title is a method from BrowserUtils
    shop_page = lp.loginfunc(test_input['userEmail'],test_input['password']) #catches the returned object of ShopPage from loginpage
    shop_page.add_to_cart(test_input['productName'])
    print(shop_page.get_title())
    checkout_page = shop_page.go_to_cart()
    purchase_page = checkout_page.checkout()
    purchase_page.purchase(test_input['country'])





