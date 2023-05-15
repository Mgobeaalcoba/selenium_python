import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demo-store.seleniumacademy.com/")

    def test_compare_products_removal_alert(self):
        driver = self.driver
        # Identificamos nuestra barra de busqueda:
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        # Buscamos el termino que queremos buscar y submiteamos:
        search_field.send_keys('tee')
        search_field.submit()

        # Ya en los resultados de la busqueda voy a identificar el boton para agregar a una comparación:
        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        # La ultima acción va a desplagar un alert con el que vamos a trabajar: 
        alert = driver.switch_to.alert
        alert_text = alert.text

        # Verificamos que el texto que nos muestra el alert sea el que entendemos que queremos ver:
        self.assertEqual(alert_text, 'Are you sure you would like to remove all products from your comparison?')

        # Finalmente realizamos un click en el botón aceptar con:
        alert.accept()

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './reports/single-reports', report_name='alerts-report', add_timestamp=False))

