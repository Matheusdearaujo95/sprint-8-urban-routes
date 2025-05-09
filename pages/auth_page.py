from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import data
import helpers

class AuthPage(BasePage):
    PHONE_INPUT = (By.ID, "phone")
    SMS_CODE_INPUT = (By.ID, "code")

    def fill_phone_number(self):
        self.type(*self.PHONE_INPUT, data.PHONE_NUMBER)
        self.click(*self.PHONE_INPUT)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SMS_CODE_INPUT)
        )

        code = helpers.retrieve_phone_code(self.driver)
        self.type(*self.SMS_CODE_INPUT, code)