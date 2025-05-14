#these are utils methods which are used in multiple pages.
class BrowserUtils:
    def __init__(self,driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title
