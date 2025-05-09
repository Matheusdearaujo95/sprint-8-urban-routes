# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def type(self, by, locator, value):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def is_present(self, by, locator):
        try:
            self.wait.until(EC.presence_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False