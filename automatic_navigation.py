import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://google.com")

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('Mariano Gobea Alcoba')
        search_field.submit()

        # Acciones sobre el navegador:
        driver.back() # Vuelve a la anterior pagina
        sleep(3) # demora 3 segundo para la siguiente acción
        driver.forward() # Va a la siguiente pagina
        sleep(3)
        driver.refresh() # Refresca la pagina
        sleep(3)

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './reports/single-reports', report_name='automatic-navigation-report', add_timestamp=False))

