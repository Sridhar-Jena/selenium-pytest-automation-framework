"""
Login Page - Page Object Model
Handles all interactions on the Login page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Login screen."""

    URL = "https://the-internet.herokuapp.com/login"

    # ── Locators ─────────────────────────────────────────────────────────────
    USERNAME_INPUT   = (By.ID, "username")
    PASSWORD_INPUT   = (By.ID, "password")
    LOGIN_BUTTON     = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE  = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE    = (By.CSS_SELECTOR, ".flash.error")
    LOGOUT_BUTTON    = (By.CSS_SELECTOR, "a[href='/logout']")

    # ── Actions ───────────────────────────────────────────────────────────────

    def open_login_page(self):
        self.open(self.URL)

    def enter_username(self, username: str):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Full login flow: enter credentials and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ── Assertions / Verifications ────────────────────────────────────────────

    def is_login_successful(self) -> bool:
        return self.is_displayed(self.SUCCESS_MESSAGE)

    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_displayed(self.ERROR_MESSAGE)

    def is_logout_button_visible(self) -> bool:
        return self.is_displayed(self.LOGOUT_BUTTON)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
