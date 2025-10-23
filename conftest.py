# conftest.py
import time

import pytest
import os
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright



CONFIG_PATH = Path(__file__).parent / "configs" / "config.yaml"

@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture(scope="session")
def browser_instance(config):
    """Start playwright and browser for the test session."""
    playwright = sync_playwright().start()
    browser_name = config.get("browser", "chromium")
    headless = config.get("headless", True)
    browser = getattr(playwright, browser_name).launch(headless=headless)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser_instance, config):
    """Create a fresh context + page for each test to isolate sessions."""
    viewport = config.get("viewport", {"width": 1280, "height": 720})
    context = browser_instance.new_context(
        viewport=viewport
    )
    page = context.new_page()
    # set default timeout (ms)
    page.set_default_timeout(config.get("timeout", 10000))
    yield page
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page_fixture = item.funcargs.get("page")  # our fixture name
        if page_fixture:
            screenshots_dir = Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            file = screenshots_dir / f"{item.name}_{int(time.time())}.png"
            page_fixture.screenshot(path=str(file))