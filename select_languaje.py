import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

class LanguageOptions(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demo-store.seleniumacademy.com/")

    # Caso de prueba para manipular un dropdown
    def test_select_language(self):
        # Para manipular el dropdown necesitamos usar el Select de selenium:
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        # Verifico que le inglessea el idioma por defecto: 
        self.assertEqual('English', select_language.first_selected_option.text)

        # vamos a pedirle ahora que seleccione el idioma Aleman:
        select_language.select_by_visible_text('German')

        # Vamos a verificar que la url venga con el idioma aleman:
        self.assertTrue('store=german' in self.driver.current_url)

        # Vuelvo a poner el idioma en Ingles, pero usando el indice:
        select_language = Select(self.driver.find_element(By.ID, 'select-language')) # ¿Por que vuelvo a guardar la lista? No lo sé pero sin hacer esto no funciona.
        select_language.select_by_index(0)

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './reports/single-reports', report_name='select-language-report', add_timestamp=False))
