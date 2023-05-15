import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Para trabajar esperas explicitas
from selenium.webdriver.support import expected_conditions as EC # Tmb para trabajar esperas explicitas
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demo-store.seleniumacademy.com")

    def test_account_link(self):
        # WebDriverWeb se configura con un tiempo máximo y una condición. Si la condición
        # se cumple antes del tiempo entonces se corta la espera. Sino se corta por el tiempo
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, 'select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):
        self.driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()

        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './reports/single-reports', report_name='waits-report', add_timestamp=False))

