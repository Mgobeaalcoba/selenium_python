import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        sleep(3)

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input("How many elements will you add?: "))
        sleep(2)
        elements_removed = int(input("How many elements will you remove?: "))
        sleep(2)
        total_elements = elements_added - elements_removed

        # Dentro del reto identificamos el boton para agregar elementos:
        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try: 
                delete_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You´re trying to delete more elements that the existent.")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements")
        else:
            print("There 0 elements")

        sleep(3)


    def tearDown(self) -> None:
        driver = self.driver
        driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= './single-reports', report_name='add-remove-report'))


