import pytest
from pages.home_page import HomePage


def users_data():
    return [
        ("administrative@test.com", "g4mr3n0v4c10n"),
        ("client@test.com", "g4mr3n0v4c10n"),
        ("ecommerce@test.com", "g4mr3n0v4c10n"),
        ("general_administrator@test.com", "g4mr3n0v4c10n"),
        ("logistic@test.com", "g4mr3n0v4c10n"),
        ("manager_gba@test.com", "g4mr3n0v4c10n"),
        ("manager_zonal@test.com", "g4mr3n0v4c10n"),
        ("staff@test.com", "g4mr3n0v4c10n"),
        ("admin@guialemor.com", "g4mr3n0v4c10n")
    ]


@pytest.fixture(autouse=True)
def setup_login(request, driver):
    home_page = HomePage(request.cls.driver)
    request.cls.home_page = home_page


class TestLogOut:
    @pytest.mark.parametrize("username,password", users_data())
    def test_log_out(self, username, password):
        print("\n\t\t-----Test log out-----")
        self.home_page.login(username, password)
        inicio = self.home_page.select_element_by_xpath(self.home_page.mensaje_inicio)
        try:
            assert inicio.text == "Gam", "ERROR. Log in failed."
        except Exception as e:
            print(e)
        try:
            self.home_page.log_out()
            welcome_message = self.home_page.select_element_by_xpath(self.home_page.mensaje_bienvenido)
        except Exception as e:
            print("Not able to log out. ")
        try:
            assert welcome_message.text == "Bienvenido a Gam", "ERROR. Log out failed."
            print("Log in and log out successful. ")
        except Exception as e:
            print(e)
