from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def type(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, locator)))
        except:
            return False

    def is_present(self, by, locator):
        try:
            self.wait.until(EC.presence_of_element_located((by, locator)))
            return True
        except:
            return False