# Importa el módulo principal de Selenium para controlar el navegador
from selenium import webdriver

# Importa la librería time para manejar tiempos de espera
import time

# Importa la clase By para localizar elementos dentro de la página
from selenium.webdriver.common.by import By

# Importa Keys para utilizar teclas especiales del teclado
from selenium.webdriver.common.keys import Keys

# Importa WebDriverWait para implementar esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait

# Importa las condiciones esperadas de Selenium
from selenium.webdriver.support import expected_conditions as EC


# Define una función de prueba llamada test_login_validation
# El parámetro login_driver es un fixture de pytest
# que ya entrega el navegador con la sesión iniciada

def test_login_validation(login_driver):

        # Guarda la instancia del navegador en la variable driver
        driver = login_driver
        # Guarda el tiempo de espera
        wait = WebDriverWait(driver, 10)
        
        # Espera hasta 10 segundos a que la URL actual contenga "/inventory.html", indicando que el login fue exitoso
        wait.until(lambda d: "/inventory.html" in d.current_url)
        
        # Espera hasta que se cumpla la condicion de que el elemento (Products) sea visible durante un máximo de 10 segundos
        elemento = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        
        # Verifica que la URL actual efectivamente contenga "/inventory.html"
        assert "/inventory.html" in driver.current_url, "No redirigio al escritorio"
        
        # Verifica que se cargue el elemento titulo en el body de la pagina
        assert elemento.is_displayed(), "No se desplego el titulo Products"
        
