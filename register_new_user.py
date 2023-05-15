import unittest
from selenium import webdriver
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demo-store.seleniumacademy.com/")

    def test_new_user(self):
        driver = self.driver
        # Ubico el account_button y hago click en el
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        # Busco el elemento de Text Log In en mi pantalla, ahora con el menú de account desplegado. 
        driver.find_element(By.LINK_TEXT, 'Log In').click()


        # Ya estamos dentro de la pantalla para crear un nuevo usuario: 
        # Identifico el boton para crear una cuenta y lo traigo:
        create_account_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        # Verifico que el botón esté visible y disponible antes de hacer click: 
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        # Una vez verificado hacemos click en el botón:
        create_account_button.click()

        # Antes de interactuar con el formulario de creación de cuenta verifiquemos que estamos allí:
        # ¿Como? Por ejemplo verificando el titulo de la pagina:
        self.assertEqual(driver.title, 'Create New Customer Account')

        # Traemos entonces los input por id para luego pasar parametros para ellos:
        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        news_letter_subscription = driver.find_element(By.ID, 'is_subscribed')
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        submit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')

        # Verifiquemos que están habilitados todos estos inputs: 
        self.assertTrue(first_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and middle_name.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and submit_button.is_enabled())
        
        # Ahora vamos a limpiar y luego insertar los datos en cada input:

        first_name.clear()
        first_name.send_keys('Mariano')

        middle_name.clear()
        middle_name.send_keys('Daniel')

        last_name.clear()
        last_name.send_keys('Gobea Alcoba')

        email_address.clear()
        email_address.send_keys('gobeamariano@gmail.com')

        if news_letter_subscription.is_selected():
            pass
        else:
            news_letter_subscription.click()
        
        password.clear()
        password.send_keys('Estoesunaprueba15892!.')

        confirm_password.clear
        confirm_password.send_keys('Estoesunaprueba15892!.')

        driver.implicitly_wait(1)
        submit_button.click()

        # Ya podemos generar nuestro usuario de forma automatica y luego lo verificamos
        # de forma manual. 

    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './reports/single-reports', report_name='register-report', add_timestamp=False))