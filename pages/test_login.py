"""
test_login.py — Login Feature Test Suite
Covers: valid login, invalid login, empty fields, logout flow.
Uses: PyTest, Page Object Model, Data-Driven Testing
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:
    """Test suite for Login functionality."""

    # ── Positive Tests ────────────────────────────────────────────────────────

    def test_valid_login(self, driver, test_data):
        """TC001: User should be able to login with valid credentials."""
        login_page = LoginPage(driver)
        login_page.open_login_page()

        login_page.login(
            test_data["valid_user"]["username"],
            test_data["valid_user"]["password"]
        )

        assert login_page.is_login_successful(), "Login success message not displayed"
        assert "You logged into a secure area!" in login_page.get_success_message()

    def test_dashboard_loaded_after_login(self, driver, test_data):
        """TC002: Dashboard should load after successful login."""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(
            test_data["valid_user"]["username"],
            test_data["valid_user"]["password"]
        )

        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_loaded(), "Dashboard did not load after login"

    def test_logout_flow(self, driver, test_data):
        """TC003: User should be able to logout successfully."""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(
            test_data["valid_user"]["username"],
            test_data["valid_user"]["password"]
        )
        login_page.logout()

        assert "login" in driver.current_url, "User was not redirected to login page after logout"

    # ── Negative Tests ────────────────────────────────────────────────────────

    @pytest.mark.parametrize("username, password, expected_error", [
        ("wronguser",   "wrongpass",  "Your username is invalid!"),
        ("tomsmith",    "wrongpass",  "Your password is invalid!"),
        ("",            "",           "Your username is invalid!"),
        ("tomsmith",    "",           "Your password is invalid!"),
    ])
    def test_invalid_login(self, driver, username, password, expected_error):
        """TC004–007: Login should fail with invalid or empty credentials."""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(username, password)

        assert login_page.is_error_displayed(), "Error message was not displayed"
        assert expected_error in login_page.get_error_message(), \
            f"Expected: '{expected_error}' | Got: '{login_page.get_error_message()}'"

    # ── UI Validation Tests ───────────────────────────────────────────────────

    def test_login_page_title(self, driver):
        """TC008: Login page should have correct browser title."""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        assert "The Internet" in login_page.get_title()

    def test_login_page_url(self, driver):
        """TC009: Login page URL should be correct."""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        assert "login" in login_page.get_current_url()
