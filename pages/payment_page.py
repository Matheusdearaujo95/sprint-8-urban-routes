from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import data

class PaymentPage(BasePage):
    def fill_card(self):
        wait = WebDriverWait(self.driver, 10)

        add_card_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment__card-add"))
        )
        add_card_button.click()

        card_number_input = wait.until(
            EC.visibility_of_element_located((By.ID, "number"))
        )
        card_code_input = wait.until(
            EC.visibility_of_element_located((By.ID, "code"))
        )

        card_number_input.send_keys(data.CARD_NUMBER)
        card_code_input.send_keys(data.CARD_CODE)

        self.driver.find_element(By.CLASS_NAME, "modal__overlay").click()

        link_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button--link"))
        )
        link_button.click()