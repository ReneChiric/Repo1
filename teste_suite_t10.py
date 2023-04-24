import unittest
import HtmlTestRunner
from teste_t09 import Login
import time
from test_01_alerts import TestAlerts
from test_02_authentication import TestFirefoxAuthentication
from test_03_context_menu import TestContextMenu
from test_04_keys import TestKeys
from test_05_dropdown import TestDropdown

class TestSuite(unittest.TestCase):

    def teste_suite(self):

        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFirefoxAuthentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDropdown)
       ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="My first HTML report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)