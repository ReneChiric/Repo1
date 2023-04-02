from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):

    driver = None
    LINK = "https://the-internet.herokuapp.com/"

    def setUp(self):
        print(f'Se executa metoda setUp() pentru {self._testMethodName}')
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        self.driver.implicitly_wait(2)


    def tearDown(self):
        print(f'Se executa metoda tearDown() pentru {self._testMethodName}')
        self.driver.quit()

    def test_url_link(self):
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Invalid url: Expected url is {expected_url}, but actual url is {actual_url}'

    def test_page_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title
        assert expected_title == actual_title, f'Invalid title: Expected title is {expected_title}, but actual title is {actual_title}'


    def test_text(self):
        actual_text = self.driver.find_element(By.XPATH, "//h2").text
        expected_text = "Login Page"
        assert actual_text == expected_text, f'Invalid text: Expected text is {expected_text}, but actual text is {actual_text}'

    def test_login_btn_is_displayed(self):
        btn_displayed = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').is_displayed()
        assert btn_displayed, f'Button is not displayed'

    def test_href_attribute(self):
        href_element = self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a')
        href = href_element.get_attribute("href")
        self.assertEqual('http://elementalselenium.com/', href)

    def test_empty_login(self):
        login = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        eroarea = self.driver.find_element(By.XPATH, '//*[@id="flash"]')
        assert eroarea.is_displayed(), f'Eroarea nu este afisata'

    def test_invalid_login(self):
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("Andrei")
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Andrei")
        login = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        actual = self.driver.find_element(By.XPATH, '//*[@id="flash"]').text
        expected = "Your username is invalid!"
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    def test_error_dissapears(self):
        login = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        eroarea = self.driver.find_element(By.XPATH, '//*[@id="flash"]').click()
        self.assertTrue(eroarea.is_displayed(), f'Error message is still displayed') #aici cred ca am avut o varianta care a functionat, desi ar trebui sa pice testul deoarece eroarea este inca afisata. Din pacate nu am salvat varianta functionala si am uitat-o, as fi recunoscator daca mi-ai arata o varianta.

    def test_label(self):
        lista_label = self.driver.find_elements(By.XPATH, '//label')
        print(lista_label)
        expected_label_1 = "Username"
        expected_label_2 = "Password"
        actual_label_1 = lista_label[0].text
        actual_label_2 = lista_label[1].text
        self.assertEqual(actual_label_1, expected_label_1, f'Labels are not identical: Expected label is {expected_label_1}, but actual label is {actual_label_1}')
        self.assertEqual(actual_label_2, expected_label_2, f'Labels are not identical: Expected label is {expected_label_2}, but actual label is {actual_label_2}')



    def test_secure(self):
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
        login = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        actual_url = self.driver.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        assert actual_url == expected_url, f'Noul url nu contine /secure'
        wait = WebDriverWait(self.driver, 7)
        flash_succes = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='flash success']")))
        assert flash_succes.is_displayed()
        flash_success_message = self.driver.find_element(By.XPATH, "//*[@class='flash success']").text
        expected_message = "secure area!"
        self.assertIn(expected_message, flash_success_message, f' Mesajul nu contine textul "secure area!"')

    def test_login_url_after_disconnect(self):
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
        login = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        logout = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()
        actual_url = self.driver.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual_url, expected_url, f'Invalid url: Expected url is {expected_url}, but actual url is {actual_url}')




