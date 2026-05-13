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



# Define un caso de prueba llamado test_cart
# Este test valida que al agregar un producto,
# el carrito muestre correctamente la cantidad "1"
def test_cart(login_driver):
    
    # Crea una espera explícita de hasta 10 segundos, utilizando el navegador autenticado para asegurar que esten todos los elementos cargados antes de empezar a probar
    wait = WebDriverWait(login_driver,10)
    
    # Busca todos los botones que tengan la clase "btn_inventory". Devuelve una lista de botones "Add to cart", [0] selecciona el primer botón de la lista, .click() hace click sobre ese botón
    login_driver.find_elements(By.CLASS_NAME,"btn_inventory")[0].click()
    
    # Espera hasta que el boton del carrito: 1. exista 2. sea visible. Luego obtiene el texto del elemento usando .text
    cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text
    
    # Verifica que el texto del carrito sea exactamente "1"
    assert cart == "1", "El carrito no muestra 1 producto"
    
    # Obtiene todos los elementos que tengan la clase "inventory_item_name". Devuelve una lista de productos encontrados, [0] selecciona el primer producto de la lista, .text obtiene el texto visible del producto
    title_product = login_driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text 
    
    # Busca el ícono/botón del carrito utilizando su clase HTML. Luego hace click para ingresar al carrito de compras
    login_driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    
    
    # Espera hasta 10 segundos a que la URL actual contenga "cart.html". Esto valida que la navegación al carrito se haya realizado correctamente
    wait.until(lambda d:"/cart.html" in d.current_url)
    
    # Busca nuevamente los productos dentro del carrito, obtiene el primer producto encontrado y guarda su texto visible
    title_product_cart = login_driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text
    
    # Compara el nombre del producto original con el nombre del producto dentro del carrito. Si son diferentes, el test falla mostrando el mensaje indicado
    assert title_product == title_product_cart,"El producto en el carrito es diferente al que se agrego"
