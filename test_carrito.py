from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_agregar_producto_carrito():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.url_contains("/inventory.html")
        )

        productos = wait.until(
            EC.visibility_of_any_elements_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        primer_producto = productos[0]

        nombre = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

        boton = primer_producto.find_element(
            By.TAG_NAME,
            "button"
        )

        boton.click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"),
                "1"
            )
        )

        contador = driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_badge"
        )

        assert contador.text == "1"

        contador_texto = contador.text

        driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()

        wait.until(
            EC.url_contains("/cart.html")
        )

        producto_carrito = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        nombre_carrito = producto_carrito.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

        assert nombre_carrito == nombre

        print(f"Producto agregado: {nombre}")
        print(f"Contador del carrito: {contador_texto}")

    finally:
        driver.quit()