
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navegacion_catalogo():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Ingresar a SauceDemo
        driver.get("https://www.saucedemo.com/")

        # 2. Iniciar sesión
        driver.find_element(By.ID, "user-name").send_keys(
            "standard_user"
        )
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce"
        )
        driver.find_element(By.ID, "login-button").click()

        # 3. Esperar a que cargue el catálogo
        wait.until(
            EC.url_contains("/inventory.html")
        )

        # 4. Validar el título Products
        titulo = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        assert titulo.text == "Products"

        # 5. Verificar que haya productos visibles
        productos = wait.until(
            EC.visibility_of_any_elements_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        assert len(productos) >= 1

        # 6. Verificar el menú
        menu = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "react-burger-menu-btn")
            )
        )

        assert menu.is_displayed()

        # 7. Verificar el filtro de ordenamiento
        filtro = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "product_sort_container")
            )
        )

        assert filtro.is_displayed()

        # 8. Obtener nombre y precio del primer producto
        primer_producto = productos[0]

        nombre = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        precio = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        print(f"Primer producto: {nombre}")
        print(f"Precio: {precio}")

        print("Catálogo verificado correctamente")

    finally:
        driver.quit()