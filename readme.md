# Proyecto de Automatización QA con Selenium y Pytest

## Propósito del Proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales sobre la plataforma web "SauceDemo" utilizando Python, Selenium WebDriver y Pytest.

Las pruebas automatizadas validan distintos comportamientos de la aplicación, entre ellos:

- Inicio de sesión de usuario
- Visualización de productos
- Validación de elementos de interfaz
- Agregado de productos al carrito
- Validación de navegación entre páginas
- Verificación de títulos y contenido visual

El proyecto fue desarrollado siguiendo buenas prácticas de automatización QA, utilizando fixtures reutilizables y waits explícitos para mejorar la estabilidad de las pruebas.

---

## Tecnologías Utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- Pytest html
- Google Chrome
- ChromeDriver
- Visual Studio Code
- Git
- Github

---

## Instalación

`git clone https://github.com/santiago71/pre-entrega-automation-testing--Santiago-Sanchez-..git`

## Instalación de Dependencias

`pip install -r requirements.txt`

## Cómo ejecutar las pruebas

- test_cart (pytest -v test/test_cart.py):
 - Consiste en agregar productos al carrito de compras y validar que los mismos se agreguen

- test_inventory (pytest -v test/test_inventory.py):
 - Consiste en validar la pantalla inicial de inventario, elementos de UI, que existan productos, etc

- test_login (pytest -v test/test_login.py):
 - Consiste en validar que se pueda realizar un inicio de sesion exitoso

- Para ejecutar todas las pruebas (pytest -v)