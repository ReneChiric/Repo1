from selenium.webdriver.common.by import By

from POM.utils.driverfactory import DriverFactory
import unittest
from POM2.pages2.login_page1 import LoginPage

class TestLoginPage(unittest.TestCase):


    USERNAME = 'tomsmith'
    PASSWORD = 'SuperSecretPassword!'
    WRONG_USER = 'sdajk'
    WRONG_PASS = 'sadjkas'
    ERROR_USER = 'Your password is invalid!'
    ERROR_PASS = 'Your password is invalid!'
    SECURE_PAGE_LINK = 'https://the-internet.herokuapp.com/secure'
    ERROR_MESSAGE = (By.CLASS_NAME, 'error')
    ERROR_CLOSE = (By.XPATH, '//*[@id="flash"]/a')

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login_url(self):
        loginpage = LoginPage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmith')
        loginpage.set_password('SuperSecretPassword!')
        loginpage.click_login_button()
        correct_url = 'https://the-internet.herokuapp.com/secure'

        self.assertEqual(self.driver.current_url, correct_url, f'Url is not correct!')

    def test_invalid_email_error(self):
        loginpage = LoginPage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmitdash')
        loginpage.set_password('SuperSecretPassword!')
        loginpage.click_login_button()

        error_message_text = loginpage.get_element_text(self.ERROR_MESSAGE)
        self.assertEqual(self.ERROR_USER, error_message_text, f'Error message is not correct!')

    def test_invalid_password_error(self):
        loginpage = LoginPage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmith')
        loginpage.set_password('SuperSecretPassword!!!')
        loginpage.click_login_button()

        error_message_password = loginpage.get_main_error_message_text()
        self.assertEqual(self.ERROR_PASS, error_message_password, f'Error message for wrong password is not correct!')


    def test_error_message_dissapears_after_click(self):
        loginpage = LoginPage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmith')
        loginpage.set_password('SuperSecretPassword!!!')
        loginpage.click_login_button()

        loginpage.click(self.ERROR_CLOSE)

        self.assertTrue(loginpage.is_element_displayed(self.ERROR_CLOSE))




