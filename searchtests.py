import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demo-store.seleniumacademy.com/")

    # Metodo para buscar "tee" o "camisas" dentro de nuestro marketplace:
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        # Metodo para limpiar el campo de busqueda en el caso de haya algún texto:
        search_field.clear()
        # Una vez limpio el campo vamos a escribir en el campo "tee" (camisa en ingles) para buscar camisas en la tienda:
        search_field.send_keys('tee')
        # Luego vamos a decirle a search_field que envié estos datos. Es decir, que haga un submit:
        search_field.submit()
        # Con esto debería mostrarnos el sitio de resultados para la busqueda "camisas"

    # Metodo para buscar un "salero" o "salt_shaker" en nuestro marketplace:
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        # Ahora voy a guardar los elementos encontrados en una lista usando "find_elements" con "S" al final:
        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul')  
        # Luego verificamos si la cantidad de productos es 1 o no:
        self.assertEqual(1, len(products))

    def tearDown(self) -> None:
        self.driver.quit()
