import unittest
import csv
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from ddt import ddt, data, unpack
from time import sleep
import webbrowser
import os

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)

    # Omito la cabecera con los headers de mi csv:
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    # Incorporo decorador @data con los terminos y la cantidad de resultados que espero:
    @data(*get_data('./testdata.csv'))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')

        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            messege = driver.find_element(By.CLASS_NAME, 'note-msg')
            self.assertEqual('Your search returns no results.', messege)

        print(f'Found {len(products)} products')

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.close()

        # Ruta al ejecutable de Google Chrome:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        # Abrir el archivo HTML generado como reporte al finalizar el script:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open('file://' + os.path.realpath('reports/single-reports/search-ddt-report.html'))

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './single-reports', report_name='search-ddt-report'))