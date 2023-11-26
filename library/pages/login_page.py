import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    _login_field_locator = (By.CSS_SELECTOR, '#form-login input[type=text]')
    _password_field_locator = (By.CSS_SELECTOR, '#form-login input[type=password]')
    _login_btn_locator = (By.CSS_SELECTOR, '#form-login button[type=submit]')

    def fill_login(self, login: str) -> None:
        """
        Заполнение поля 'E-Mail Address'
        
        :param str login: логин пользователя
        """
        with allure.step(f'Заполнение поля "E-Mail Address" {login}'):
            field = self.wait_element_to_be_clickable(self._login_field_locator)
            field.clear()
            field.send_keys(login)

    def fill_password(self, passwd: str) -> None:
        """
        Заполнение поля 'Password'
        
        :param str passwd: пароль пользователя
        """
        with allure.step('Заполнение поля "E-Mail Address"'):
            field = self.wait_element_to_be_clickable(self._password_field_locator)
            field.clear()
            field.send_keys(passwd)

    def do_login(self) -> None:
        """Нажатие кнопки 'Login'"""
        with allure.step('Нажатие кнопки "Login"'):
            url = self.driver.current_url
            self.wait_element_to_be_clickable(self._login_btn_locator).click()
            self.wait_url_changes(url)
