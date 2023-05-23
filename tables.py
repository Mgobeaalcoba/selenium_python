import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import webbrowser
import os

class Tables(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
        sleep(3)

    def test_sort_tables(self):
        driver = self.driver

        # Armo una lista de listas vacias para extraer la información de mi web. Cada lista va a contener la info de 1 columna. La ultima columna "Action" no me interesa:

        table_data = [[] for i in range(5)] # 5 son las columnas que quiero registrar de mi web.
        print(table_data)

        # Itero por cada uno de los headers y por cada uno de los datos: 
        # Una iteración por cada header de mis columnas:
        for i in range(5):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            # Una iteración por cada fila con datos
            for j in range(4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                table_data[i].append(row_data.text)

        print(table_data)

                # //*[@id="table1"]/tbody/tr[1]/td[2]
                # //*[@id="table1"]/tbody/tr[1]/td[1]
                # //*[@id="table1"]/tbody/tr[2]/td[1]

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.close()

        # Ruta al ejecutable de Google Chrome:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        # Abrir el archivo HTML generado como reporte al finalizar el script:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open('file://' + os.path.realpath('reports/single-reports/tables-report.html'))

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './single-reports', report_name='tables-report'))