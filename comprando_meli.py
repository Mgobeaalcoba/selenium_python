import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from CONSTANTES import Buyer, Seller
from time import sleep

class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= "./chromedriver.exe")
        driver = self.driver
        driver.get("https://www.mercadolibre.com.ar/#from=homecom")
        driver.maximize_window()
        driver.implicitly_wait(5)

    # Prueba para buscar y encontrar un elemento por el id:
    def test_buy_book(self):
        driver = self.driver

        login_field = driver.find_element(By.XPATH, '//*[@id="nav-header-menu"]/a[2]')
        login_field.click()

        # Instanceo un objeto buyer para cuidar el user y password:
        user_complete = Buyer()

        user_field = driver.find_element(By.NAME, 'user_id')
        user_field.click()
        user_field.clear()
        user_field.send_keys(user_complete.user)

        continue_button = driver.find_element(By.XPATH, '//*[@id="login_user_form"]/div[2]/button/span')
        continue_button.click()
        
        pass_field = driver.find_element(By.NAME, 'password')
        pass_field.click()
        pass_field.clear()
        pass_field.send_keys(user_complete.password)

        init_sesion = driver.find_element(By.XPATH, '//*[@id="action-complete"]/span')
        init_sesion.click()

        driver.get('https://articulo.mercadolibre.com.ar/MLA-1103501755-libro-test-_JM')

        buy_now = driver.find_element(By.XPATH, '//*[@id="main_actions"]/form/div/button[1]/span')
        buy_now.click()

        shipping_button = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div/div/div[3]/form/section[1]/div/div/div/ul/li/div/label/div[2]/div')
        shipping_button.click()

        continue_button2 = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div/div/div[5]/div[2]/button')
        continue_button2.click()

        mp_option = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/section/div/form/div[2]/ul/li/div/label/div[2]/div')
        mp_option.click()

        continue_button3 = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/section/div/form/div[4]/div[2]/button')
        continue_button3.click()

        continue_button4 = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div/section/div[2]/div/div/div/div/form/div[2]/button')
        continue_button4.click()

        confirm_button = driver.find_element(By.XPATH, '//*[@id="aside-container"]/div/div/aside/section/form/button')
        confirm_button.click()

    def test_print_label(self):
        driver = self.driver
        driver.get("https://www.mercadolibre.com.ar/#from=homecom")

        login_field = driver.find_element(By.XPATH, '//*[@id="nav-header-menu"]/a[2]')
        login_field.click()

        # Instanceo un objeto buyer para cuidar el user y password:
        user_complete = Seller()

        user_field = driver.find_element(By.NAME, 'user_id')
        user_field.click()
        user_field.clear()
        user_field.send_keys(user_complete.user)

        continue_button = driver.find_element(By.XPATH, '//*[@id="login_user_form"]/div[2]/button/span')
        continue_button.click()

        pass_field = driver.find_element(By.NAME, 'password')
        pass_field.click()
        pass_field.clear()
        pass_field.send_keys(user_complete.password)

        init_sesion = driver.find_element(By.XPATH, '//*[@id="action-complete"]/span')
        init_sesion.click()

        user_button = driver.find_element(By.XPATH, '//*[@id="nav-header-menu"]/div/label/a/span')
        user_button.click()

        sales_button = driver.find_element(By.LINK_TEXT, 'Ventas')
        sales_button.click()

        select = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/input')
        self.assertTrue(select.is_displayed() and select.is_enabled)
        sleep(5)
        select.click()
        
        print_last = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/button')
        self.assertTrue(print_last.is_displayed() and print_last.is_enabled())
        sleep(5)
        print_last.click()
        sleep(5)


    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './reports/single-reports', report_name='comprando-report', add_timestamp=False))