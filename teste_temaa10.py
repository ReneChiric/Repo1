import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC


class testing(TestCase):
    driver = None
    LINK = "https://www.saucedemo.com/"
    login_button = (By.ID, 'login-button')
    username = (By.ID, 'user-name')
    password = (By.ID, 'password')
    add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")


    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def wait_for_element_to_disappear(self, element, timp):
        wait = WebDriverWait(self.driver, timp)
        return wait.until(EC.none_of(EC.presence_of_element_located(element)))

    def test_basic_auth(self):
        self.driver.find_element(*self.username).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()

    def test_url_after_login(self):
        self.driver.find_element(*self.username).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()
        expected_url = "https://www.saucedemo.com/inventory.html"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, "The url is wrong!")

    def test_inventory_update(self):
        self.driver.find_element(*self.username).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.add_to_cart).click()
        cart_symbol_updated = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_symbol_updated.is_displayed(), f'The cart does not show any updates'

    def test_error_msg_login_is_correct(self):
        self.driver.find_element(*self.username).send_keys("locked_out_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        self.assertEqual(expected_error, error_message, f'Error message is not correct!')
