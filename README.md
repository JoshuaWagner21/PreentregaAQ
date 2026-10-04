# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.


# Automatización de Pruebas - SauceDemo

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales sobre la aplicación web SauceDemo utilizando Python, Pytest y Selenium WebDriver.

Las pruebas automatizadas permiten verificar funcionalidades principales de la aplicación, como:

* Inicio de sesión.
* Navegación y visualización del catálogo.
* Agregado de productos al carrito.
* Verificación del producto agregado al carrito.

## Tecnologías utilizadas

* Python 3.12
* Pytest
* Selenium WebDriver
* Google Chrome
* ChromeDriver
* pytest-html
* Visual Studio Code
* Git
* GitHub

## Estructura del proyecto

```text
PreentregaAQ/
│
├── test_login.py
├── test_catalogo.py
├── test_carrito.py
├── pytest.ini
├── requirements.txt
├── README.md
│
└── reports/
    └── reporte.html
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
```

### 2. Ingresar al proyecto

```bash
cd PreentregaAQ
```

### 3. Crear y activar un entorno virtual

En Windows:

```powershell
python -m venv .venv
```

Activar el entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

## Ejecución de las pruebas

Para ejecutar todas las pruebas:

```powershell
pytest
```

También se pueden ejecutar las pruebas mostrando información detallada:

```powershell
pytest -v -s
```

Las pruebas incluidas son:

* `test_login.py`
* `test_catalogo.py`
* `test_carrito.py`

## Reporte HTML

El proyecto utiliza `pytest-html` para generar un reporte HTML con los resultados de las pruebas.

El reporte se genera automáticamente en:

```text
reports/reporte.html
```

También puede generarse manualmente mediante:

```powershell
pytest -v --html=reports/reporte.html --self-contained-html
```

El reporte permite consultar:

* Pruebas ejecutadas.
* Pruebas aprobadas.
* Pruebas fallidas.
* Duración de las pruebas.
* Información del entorno de ejecución.

## Credenciales utilizadas

Para las pruebas de SauceDemo se utiliza el usuario de prueba proporcionado por la aplicación:

```text
Usuario: standard_user
Contraseña: secret_sauce
```

## Casos automatizados

### Login

Verifica que un usuario válido pueda iniciar sesión correctamente y acceder al catálogo.

### Catálogo

Verifica que el catálogo de productos se cargue correctamente y que los productos y sus precios sean visibles.

### Carrito

Verifica que un producto pueda agregarse al carrito, que el contador se actualice correctamente y que el producto agregado sea el mismo que aparece en el carrito.

## Generación del reporte

Después de ejecutar:

```powershell
pytest
```

el reporte estará disponible en:

```text
reports/reporte.html
```

Este archivo puede abrirse con cualquier navegador web.
