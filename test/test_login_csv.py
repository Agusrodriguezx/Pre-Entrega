from page.login_page import LoginPage
from utils.data_reader import read_users_csv # importamos lector
import pytest

@pytest.mark.parametrize("user", read_users_csv()) # parametrizamos el lector con la prueba
def test_login(driver, user):
    login_page = LoginPage(driver)

    login_page.login(user["username"],user["password"]) # llamamos al elemento que nos trae esa función
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        error = login_page.get_error_message()
        assert "Epic sadface" in error 