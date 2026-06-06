# Proyecto de Automatización QA - Agustina Rodriguez

## Descripción

Proyecto de automatización de pruebas funcionales desarrollado con Python, Selenium WebDriver y Pytest.

Las pruebas cubren los flujos principales de la aplicación web Swag Labs: login, visualización del inventario y manejo del carrito de compras.

El proyecto utiliza el patrón de diseño Page Object Model (POM) para mejorar la organización, reutilización y mantenibilidad del código.

Además, se implementó un enfoque de Data-Driven Testing utilizando archivos CSV para ejecutar múltiples escenarios de autenticación con diferentes conjuntos de datos y resultados esperados.


## Tecnologías usadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- CSV (Data-Driven Testing)
- Google Chrome + ChromeDriver
- Git

## Instalación
`git clone https://github.com/Agusrodriguezx/Pre-Proyecto.git
cd Pre-Proyecto`


## Instalación de Dependencias
pip install -r requirements.txt


## Ejecutar pruebas
pytest


## Generar reporte HTML
pytest --html=report.html --self-contained-html


## Fucionamiento de las pruebas

### test_login.py — Pruebas de autenticación

- `test_login_ok`
    - Verifica que el usuario sea redirigido correctamente al inventario después de iniciar sesión.

- `test_login_invalid_password`
    - Verifica que se muestre el mensaje de error correspondiente al ingresar una contraseña inválida.

---

### test_login_csv.py — Pruebas de automatización con datos parametrizados

- Implementa Data-Driven Testing mediante `pytest.mark.parametrize()`.

- Utiliza datos externos almacenador en `data/users.csv`.

- Lee los datos de prueba a través de `utils/data_reader.py`.

- Ejecuta múltiples escenarios de autenticación utilizando un único caso de prueba.

- Valida tanto escenarios positivos como negativos:
    - Credenciales válidas → acceso exitoso al inventario.
    - Credenciales inválidas → visualización del mensaje de error correspondiente.

---

### test_inventory.py — Pruebas del inventario

- `test_inventory_title`
    - Verifica que el título de la página sea "Swag Labs".

- `test_productos_visibles`
    - Verifica que exista al menos un producto visible en el inventario.

- `test_ui_elements` 
    - Verifica la presencia del menú hamburguesa y del filtro de productos.

---

### test_cart.py — Pruebas del carrito

- `test_cart`
    - Agrega un producto al carrito.
    - Verifica la actualización del contador del carrito.
    - Navega al carrito
    - Comprueba que el producto agregado sea el esperado.


## Patrón de diseño utilizado

### Page Object Model (POM)
Se implementó el patrón Page Object Model para separar los elementos y acciones de cada página de las validaciones realizadas en los tests.

Las páginas se representan mediante clases independientes:
- LoginPage
- InventoryPage

Esto permite mejorar la reutilización del código y facilitar el mantenimiento de las pruebas automatizadas.