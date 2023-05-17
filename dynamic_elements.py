import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
import webbrowser
import os

class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()
        sleep(3)

    def test_name_elements(self):
        driver = self.driver

        # Variable que contendrá las opciones del menú: 
        options = []
        menu = 5 # Las opciones totales del menu cuando aparecen todas
        tries = 1 # Contador de intentos

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries += 1
                    driver.refresh()

        print(f"Finished in {tries} tries.")

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.close()

        # Ruta al ejecutable de Google Chrome:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        # Abrir el archivo HTML generado como reporte al finalizar el script:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open('file://' + os.path.realpath('reports/single-reports/dynamic-element-report.html'))

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './single-reports', report_name='dynamic-element-report'))


