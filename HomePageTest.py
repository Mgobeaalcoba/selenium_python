import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        # Defino el driver: 
        self.driver = webdriver.Chrome(executable_path= "./chromedriver.exe")
        driver = self.driver
        # Le indico a que sitio web tenemos ir para probar sus elementos:
        # El driver get lo podemos usar acá si todas las pruebas serán en el mismo
        # dominio o lo podemos usar en algún test si vamos a cambiar de dominio segun la prueba.
        driver.get("http://demo-store.seleniumacademy.com/")
        # Le voy a pedir que maximize la ventana dado que pueden haber elementos 
        # responsivos que pueden cambiar su ubicación segun el tamaño. 
        driver.maximize_window()
        # Añado una pequeña pausa.
        driver.implicitly_wait(15)

    # Prueba para buscar y encontrar un elemento por el id:
    def test_search_text_field(self):
        # Guardo el campo de busqueda de la pagina en una variable:
        search_field = self.driver.find_element("id", "search")

    # Prueba para buscar y encontrar un elemento por el name:
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element("name", "q")

    # Ahora voy a buscar y seleccionar a traves de la clase:
    def test_search_text_field_by_class(self):
        search_field = self.driver.find_element("class name", "input-text")

    # Verificamos que el botón de la barra de busqueda esté disponible: 
    def test_search_button_enabled(self):
        search_button = self.driver.find_element("class name", "button")

    def tearDown(self) -> None:
        # Le indico que cierre la ventana y cualquier sesión que tenga iniciada:
        self.driver.quit()

    # Cuantas imagenes con enlaces tenemos en el sitio? Lo hacemos con una lista:
    def test_count_of_promo_banner_images(self):
        # Identifico el elemento contenedor de los banners
        banner_list = self.driver.find_element("class name", "promos")
        # Cuento cuantas img hay en ese elemento contenedor que identifique:
        # Ojo acá se usa find_elements con s al final
        banners = banner_list.find_elements("tag name", "img")
        # Valido con una assertion que sean 3 imagenes:
        self.assertEqual(3, len(banners), "It´s ok. There are three images") # La leyenda del asser no suma nada, dado que unittest no la muestra

    # Cuando no tenemos un elemento lo suficientemente explicitado por los selectores
    # anteriores podemos recurrir a su xpath para identificarlo y traerlo:
    def test_img_by_xpath(self):
        img = self.driver.find_element("xpath", '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    # Tmb podemos identificar por su identificador en CSS:
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element("css selector", "div.header-minicart span.icon")

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name='home-page-test-report'))