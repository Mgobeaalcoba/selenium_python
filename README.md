# Selenium Python 

¿Que es selenium?

Suite de herramientas para automatización de navegadores. 

Compatible con Firefox, Chrome, Explorer, Safari y Opera

Compatible con distintos lenguajes de programación como: Java, C#, Kotlin, PHP, Python, Ruby y JavaScript

El objetivo de Selenium NO fue para el Testing ni para el Web Scraping (aunque se puede usar para eso), por lo tanto, no es el más optimo para estas actividades.

Protocolo: WebDriver, herramienta que se conecta a un API.
Selenium WebDriver es la herramienta que utilizaremos en el curso.

- Selenium NO es un Software, ES una SUIT de Softwares.
- DDT: Data Drive Testing: Ingresar datos para que realice varias pruebas (sin intervención humana).

Cuando hablemos de Selenium en el curso estaremos hablando de **"Selenium Web Driver"**

-----------------------------------

Algunas herramientas de testing y automatización:

**Puppeteer:**

• PROS: Soporte por parte de Google, te brinda datos del Performance Analysis de Chrome y un mayor control de este navegador. No requiere archivos externos como lo hace Selenium con WebDriver.

• CONTRAS: Solo funciona para Google Chrome con JavaScript, tiene una comunidad pequeña así que el apoyo será poco.

**Cypress.io:**

• PROS: Tiene una comunidad emergente y va creciendo a pasos acelerados, tiene muy buena documentación para implementar Cypress en los proyectos. Es muy ágil en pruebas E2E, está orientado a desarrolladores y tiene un excelente manejo del asincronismo, logrando que las esperas sean dinámicas y también se puedan manejar fácilmente.

• CONTRAS: Solo funciona en Google Chrome con JavaScript, se pueden realizar pruebas en paralelo únicamente en la versión de pago.

-----------------------------------------

**Configuración de entorno Selenium:**

Python V 3.6 o superior

si estas en la terminal de ubuntu

1 : sudo apt update
2 : apt install python3-pip
3 : pip3 --version
4 : pip3 install selenium
5 : pip3 install pyunitreport (Librería para hacer reportes en HTML para python)
6 : pip freeze > requirements.txt

Finalmente debemos buscar los drivers del navegador con el queramos trabajar. En mi caso busco los ChromeDriver - WebDriver e instalo el que corresponde a mi sistema operativo. 

---------------------------------------

**Unittest (PyTest):**

<img src="./unittest.PNG">

