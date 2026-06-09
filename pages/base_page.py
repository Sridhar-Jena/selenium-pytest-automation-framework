"""
Base Page Class - Page Object Model (POM)
All page classes inherit from this base class.
Provides reusable Selenium wrapper methods.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base class for all Page Objects."""

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ── Navigation ──────────────────────────────────────────────────────────

    def open(self, url: str):
        """Navigate to a URL."""
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    # ── Element Interactions ─────────────────────────────────────────────────

    def find_element(self, locator: tuple):
        """Wait and find a single element."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise

    def click(self, locator: tuple):
        """Wait for element to be clickable, then click."""
        logger.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator: tuple, text: str):
        """Clear field and type text."""
        logger.info(f"Typing '{text}' into: {locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get visible text of an element."""
        return self.find_element(locator).text

    def is_displayed(self, locator: tuple) -> bool:
        """Check if element is visible on page."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator: tuple) -> bool:
        """Check element presence without throwing exception."""
        try:
            self.find_element(locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    # ── Wait Utilities ───────────────────────────────────────────────────────

    def wait_for_text(self, locator: tuple, text: str):
        """Wait until element contains specific text."""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_url_contains(self, partial_url: str):
        """Wait until the URL contains a specific substring."""
        return self.wait.until(EC.url_contains(partial_url))

    # ── JavaScript Utilities ─────────────────────────────────────────────────

    def scroll_to_element(self, locator: tuple):
        """Scroll element into view using JavaScript."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, locator: tuple):
        """Click element using JavaScript (useful for hidden elements)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # ── Screenshot ───────────────────────────────────────────────────────────

    def take_screenshot(self, filename: str):
        """Save a screenshot to the reports folder."""
        path = f"reports/{filename}.png"
        self.driver.save_screenshot(path)
        logger.info(f"Screenshot saved: {path}")
