"""
Dashboard Page - Page Object Model
Handles all interactions on the Dashboard / Home page post-login.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page Object for the Dashboard screen (post-login)."""

    # ── Locators ─────────────────────────────────────────────────────────────
    PAGE_HEADING     = (By.TAG_NAME, "h2")
    FLASH_MESSAGE    = (By.CSS_SELECTOR, ".flash")
    LOGOUT_LINK      = (By.CSS_SELECTOR, "a[href='/logout']")
    SUBHEADER        = (By.CSS_SELECTOR, ".subheader")

    # ── Actions ───────────────────────────────────────────────────────────────

    def get_heading(self) -> str:
        return self.get_text(self.PAGE_HEADING)

    def get_flash_message(self) -> str:
        return self.get_text(self.FLASH_MESSAGE)

    def is_dashboard_loaded(self) -> bool:
        return self.is_displayed(self.PAGE_HEADING)

    def logout(self):
        self.click(self.LOGOUT_LINK)
