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


# Caso de prueba que valida que el titulo de la pagina sea el correcto
def test_inventory_title(login_driver):

    # Obtiene el título actual de la pestaña del navegador
    # Ejemplo: "Swag Labs"
    titulo = login_driver.title

    # Verifica que el título de la página sea exactamente "Swag Labs"
    # Si el título es distinto, el test falla mostrando el mensaje indicado
    assert titulo == "Swag Labs", "Titulo de la pagina incorrecto"

# Caso de prueba que valida que existan productos en el inventario
def test_productos_desplegados(login_driver):
    # Variable que guard un tiempo de espera
    wait = WebDriverWait(login_driver, 10)

    # Espera a que aparezca al menos un producto
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
    
    # Obtiene todos los productos
    products = login_driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    # Valida que exista al menos uno
    assert len(products) > 0, "No hay productos desplegados"
    

# Caso de prueba que valida que distintos elementos importantes de la interfaz se visualicen correctamente. luego de iniciar sesión
def test_ui_elements(login_driver):

    # Busca el botón del menú lateral utilizando su ID
    menu = login_driver.find_element(By.ID, "react-burger-menu-btn")

    # Busca el filtro de productos utilizando su CLASS_NAME
    filtro = login_driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Busca el ícono/botón del carrito de compras, utilizando su CLASS_NAME
    carrito = login_driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    # Busca el botón "Add to cart" de un producto específico, utilizando el atributo NAME
    añadir_al_carrito = login_driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt")

    # Verifica que el botón del menú sea visible en pantalla
    assert menu.is_displayed(), "Boton menú no se visualiza"

    # Verifica que el filtro de productos sea visible
    assert filtro.is_displayed(), "Boton filtro no se visualiza"

    # Verifica que el carrito de compras sea visible
    assert carrito.is_displayed(), "Boton carrito no se visualiza"

    # Verifica que el botón "Añadir al carrito" sea visible
    assert añadir_al_carrito.is_displayed(), "Boton añadir al carrito no se visualiza"