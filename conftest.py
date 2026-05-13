from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.loginpage import login

# Define un fixture de pytest llamado "driver"
# Este fixture se encarga de:
# - abrir Chrome
# - configurarlo
# - entregarlo a los tests
# - y cerrarlo automáticamente al finalizar
@pytest.fixture
def driver():

    # Crea un objeto de configuración para Chrome
    options = webdriver.ChromeOptions()

    # Agrega el argumento para abrir Chrome en modo incógnito
    options.add_argument("--incognito")

    # Inicializa el navegador Chrome utilizando
    # las opciones configuradas anteriormente
    driver = webdriver.Chrome(options=options)

    # Entrega la instancia del navegador al test
    # o a otros fixtures que lo necesiten
    yield driver

    # Se ejecuta automáticamente al finalizar el test
    # Cierra completamente el navegador y la sesión Selenium
    driver.quit()


# Define un segundo fixture llamado "login_driver"
# Este fixture reutiliza el fixture "driver"
# y además realiza el login automáticamente
@pytest.fixture
def login_driver(driver):

    # Ejecuta la función login()
    # pasándole la instancia del navegador
    login(driver)

    # Devuelve el navegador ya autenticado
    # para que los tests lo utilicen
    return driver

