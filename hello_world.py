import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# Creo una clase que hereda de unittest.TestCase
class HelloWorld(unittest.TestCase):
    
    # Defino los metodos de mi testing:

    # setUp prepara el entorno de la prueba misma: 
    def setUp(self) -> None:
        # Puede que en Windows no sirva la ruta así y haya que ponerle un "r" delante y la ruta completa.
        self.driver = webdriver.Chrome(executable_path= './chromedriver.exe')
        driver = self.driver
        # Le indico al driver que espere implicitamente hasta 10 segundos antes de
        # realizar la proxima acción, que estarán en nuestras pruebas:
        driver.implicitly_wait(10)
    
    # Prueba sobre el codigo (siempre debe llevar la palabra test delante para ejecutarse)
    def test_hello_world(self):
        # Aquí iran una serie de acciones para que el navegador se automatize:
        driver = self.driver
        driver.get('https://www.platzi.com') # Con esto nuestro navegador debería ir a la URL de platzi

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    # Salida de lo que estamos haciendo
    def tearDown(self) -> None:
        # Acciones al finalizar la prueba. Por ejemplo cerrar el navegador para 
        # evitar fuga de recursos y que nuestro equipo se ponga lento. 
        self.driver.quit()
    
# Entry Point para inicializar las pruebas:
if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name='hello-world-report'))

# """
# Resultado del script:

# Running tests...
# ----------------------------------------------------------------------
#  test_hello_world (__main__.HelloWorld.test_hello_world) ... C:\Users\mgobea\Documents\develop\Python\selenium_python\hello_world.py:13: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#   self.driver = webdriver.Chrome(executable_path= './chromedriver.exe')

# DevTools listening on ws://127.0.0.1:61244/devtools/browser/46b2b832-306c-4c18-a975-3a3ff0fcdc30
# OK (7.000337)s

# ----------------------------------------------------------------------
# Ran 1 test in 11.088s

# OK



# Generating HTML reports...
# Template is not specified, load default template instead.
# Reports generated: C:\Users\mgobea\Documents\develop\Python\selenium_python\reports\reportes\hello-world-report.html


# Resultado del test en HTML:

# Test Result
# Start Time: 2023-05-10 16:26:26

# Duration: 11.088s

# Status: Pass: 1

# reportes	Status
# test_hello_world (__main__.HelloWorld.test_hello_world)	Pass
# Total Test Runned: 1	Pass: 1

# Este mismo report se genera en una nueva carpeta que se va a llamar reports en la raiz del proyecto.
# """