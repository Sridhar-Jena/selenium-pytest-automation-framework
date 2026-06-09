"""
config.py — Environment Configuration
Centralizes all configurable settings for the test framework.
"""

import os


class Config:
    """Central config — override any value via environment variables."""

    # ── URLs ──────────────────────────────────────────────────────────────────
    BASE_URL        = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    LOGIN_URL       = f"{BASE_URL}/login"

    # ── Browser ───────────────────────────────────────────────────────────────
    BROWSER         = os.getenv("BROWSER", "chrome")
    HEADLESS        = os.getenv("HEADLESS", "false").lower() == "true"
    WINDOW_SIZE     = (1920, 1080)

    # ── Timeouts (seconds) ────────────────────────────────────────────────────
    IMPLICIT_WAIT   = 5
    EXPLICIT_WAIT   = 10
    PAGE_LOAD_TIMEOUT = 30

    # ── Reporting ─────────────────────────────────────────────────────────────
    REPORTS_DIR     = os.getenv("REPORTS_DIR", "reports")
    SCREENSHOT_ON_FAIL = True
