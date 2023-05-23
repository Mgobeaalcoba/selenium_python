import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from google_page import GooglePage
from selenium import webdriver
import webbrowser
import os

class AddRemoveElements(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Mariano Gobea')

        self.assertEqual('Platzi',google.keyword())
    
    @classmethod
    def tearDown(cls) -> None:
        driver = cls.driver
        driver.implicitly_wait(3)
        cls.driver.close()

        # Ruta al ejecutable de Google Chrome:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        # Abrir el archivo HTML generado como reporte al finalizar el script:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open('file://' + os.path.realpath('reports/single-reports/google-page-report.html'))

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './single-reports', report_name='google-page-report'))


