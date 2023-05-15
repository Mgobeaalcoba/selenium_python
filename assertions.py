import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demo-store.seleniumacademy.com/")

    # Con el metodo de busqueda creado abajo ahora si voy a generar los distintos tests:
    # Voy a testear que exista el campo de busqueda
    def test_search_field(self):
        # Uso un assertTrue dado que mi metodo de abajo devuelve booleans:
        self.assertTrue(self.is_element_present(By.NAME, 'q')) # Indico que quiero encontrarlo por nombre y le paso un nombre luego

    # Valido si tengo una opción para lenguaje en mi pagina:
    def test_language_options(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self) -> None:
        self.driver.quit()
    
    # Metodo para encontrar a los elementos en mi web: 
    # how nos va indicar el tipo de selector
    # what nos va a indicar el valor que tiene
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by= how, value= what)
        except NoSuchElementException as variable:
            return False
        return True
        