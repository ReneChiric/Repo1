from selenium import webdriver
from selenium.webdriver.common.by import By

from POM2.pages2.home_page1 import HomePage

class SecurePage(HomePage):

    SECURE_PAGE_LINK = 'https://the-internet.herokuapp.com/secure'
    MESSAGE_SUCCES = (By.ID, 'flash')
    LOGOUT_BTN = (By.CLASS_NAME, 'icon-signout')
    CLOSE_MESSAGE = (By.CLASS_NAME, 'success')

    def message_close(self):
        self.click(self.CLOSE_MESSAGE)

    def logout_click(self):
        self.click(self.LOGOUT_BTN)

    def get_message_text(self):
        return self.get_element_text(self.MESSAGE_SUCCES)

    def is_message_displayed(self):
        return self.is_element_displayed(self.MESSAGE_SUCCES)

    def get_close_message_text(self):
        return self.get_element_text(self.CLOSE_MESSAGE)