from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

# Cargamos en variables los tests que queremos realizar: 
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

# contruimos la suite de pruebas:
smoke_test = TestSuite([assertions_test, search_tests])

# para generar los reporters
kwargs = {
    "output": './reports/suite-reports',
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
    }

# la variable runner almacena un reporte generado por HTMLTestRuner
# usa como argumento "**kwargs" o multiples argumentos en función de 
# cuantos output tengamos.  
runner = HTMLTestRunner(**kwargs)

# corro el rurner con la suite de prueba
runner.run(smoke_test) 