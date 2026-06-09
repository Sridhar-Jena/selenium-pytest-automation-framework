"""
conftest.py — PyTest Fixtures
Shared fixtures available to all test files automatically.
"""

import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ── Browser Fixture ──────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes Chrome WebDriver before each test.
    Quits browser after each test.
    Supports headless mode via ENV variable: HEADLESS=true
    """
    options = Options()

    headless = os.getenv("HEADLESS", "false").lower() == "true"
    if headless:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(5)

    yield browser

    # Teardown
    browser.quit()


# ── Test Data Fixture ─────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def test_data():
    """
    Loads test data from JSON file once per session.
    Usage: def test_login(driver, test_data): ...
    """
    data_path = os.path.join(os.path.dirname(__file__), "utils", "test_data.json")
    with open(data_path, "r") as f:
        return json.load(f)


# ── Screenshot on Failure ─────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Auto-capture screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports", exist_ok=True)
            screenshot_name = f"reports/FAIL_{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"\n📸 Screenshot saved: {screenshot_name}")
