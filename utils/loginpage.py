# Importa el módulo principal de Selenium para controlar el navegador
from selenium import webdriver

# Importa la librería time para manejar pausas o tiempos de espera
import time

# Importa la clase By, utilizada para localizar elementos en la página
from selenium.webdriver.common.by import By

# Importa Keys para poder enviar teclas especiales del teclado
from selenium.webdriver.common.keys import Keys

# Importa WebDriverWait para realizar esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait

# Importa las condiciones esperadas de Selenium
from selenium.webdriver.support import expected_conditions as EC


# Define una función llamada login que recibe como parámetro el driver del navegador
def login(driver):

    # Abre la página web de SauceDemo
    driver.get("https://www.saucedemo.com/")
    
    # Crea una espera explícita de hasta 10 segundos
    wait = WebDriverWait(driver, 10)

    # Espera hasta que el campo de usuario sea visible en pantalla
    usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    # Escribe el nombre de usuario en el input correspondiente
    usuario.send_keys("standard_user")


    # Espera hasta que el campo de contraseña sea visible
    contrasena = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    # Escribe la contraseña en el input correspondiente
    contrasena.send_keys("secret_sauce")

    # Espera hasta que el botón de login sea clickeable
    ingresar = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    # Hace clic en el botón para iniciar sesión
    ingresar.click()