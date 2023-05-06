from selenium import webdriver
from selenium.webdriver.common.by import By

from POM2.pages2.home_page1 import HomePage


class LoginPage(HomePage):

    LOGIN_PAGE_URL = 'https://the-internet.herokuapp.com/login'
    EMAIL_INPUT = (By.ID, 'username')
    PASS_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.CLASS_NAME, 'fa')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error')


    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.type(self.PASS_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BTN)

    def is_main_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE)

    def get_main_error_message_text(self):
        return self.get_element_text(self.ERROR_MESSAGE)

