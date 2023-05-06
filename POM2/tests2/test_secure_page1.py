from selenium.webdriver.common.by import By

from POM.utils.driverfactory import DriverFactory
import unittest
from POM2.pages2.login_page1 import LoginPage
from POM2.pages2.secure_page1 import SecurePage

class TestSecurePage(unittest.TestCase):

    MESSAGE_SUCCES = (By.ID, 'flash')
    LOG_OUT_MESSAGE = 'You logged out of the secure area!'

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_succes_message_is_correct(self):
        loginpage = LoginPage(self.driver)
        securepage = SecurePage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmith')
        loginpage.set_password('SuperSecretPassword!')
        loginpage.click_login_button()

        mesaj_succes = securepage.get_message_text()

        self.assertEqual(mesaj_succes, securepage.get_message_text(), f'Message is not correct!')

    def test_message_is_displayed(self):
        loginpage = LoginPage(self.driver)
        securepage = SecurePage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmith')
        loginpage.set_password('SuperSecretPassword!')
        loginpage.click_login_button()

        self.assertTrue(securepage.is_element_displayed)

    def test_logout_message(self):
        loginpage = LoginPage(self.driver)
        securepage = SecurePage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.set_email('tomsmith')
        loginpage.set_password('SuperSecretPassword!')
        loginpage.click_login_button()
        securepage.logout_click()

        self.assertEqual(self.LOG_OUT_MESSAGE, securepage.get_close_message_text(), "Error, messages do not match")

