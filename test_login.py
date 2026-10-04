
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        # 1. Abrir la página de login
        driver.get("https://www.saucedemo.com/")

        # 2. Ingresar las credenciales
        driver.find_element(By.ID, "user-name").send_keys(
            "standard_user"
        )
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce"
        )

        # 3. Hacer clic en Login
        driver.find_element(By.ID, "login-button").click()

        # 4. Esperar explícitamente a que aparezca
        # la página de inventario
        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.url_contains("/inventory.html")
        )

        # 5. Validar la URL
        assert driver.current_url.endswith(
            "/inventory.html"
        )

        # 6. Validar el título Products
        titulo = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        assert titulo.text == "Products"

        print("Login exitoso: prueba aprobada")

    finally:
        # 7. Cerrar el navegador
        driver.quit()