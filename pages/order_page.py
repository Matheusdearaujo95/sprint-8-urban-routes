from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import data

class OrderPage(BasePage):
    # Localizadores
    ADDRESS_FROM = (By.ID, "address-from")
    ADDRESS_TO = (By.ID, "address-to")
    BUTTON_SUBMIT = (By.ID, "route-button")

    # Ações
    def set_route(self):
        self.type(*self.ADDRESS_FROM, data.ADDRESS_FROM)
        self.type(*self.ADDRESS_TO, data.ADDRESS_TO)
        self.click(*self.BUTTON_SUBMIT)