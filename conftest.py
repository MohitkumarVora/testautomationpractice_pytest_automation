# conftest.py
import time
import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright


# conftest.py or utils/decorators.py
from pytest_bdd import given as _given, when as _when, then as _then, parsers


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

def pytest_bdd_before_scenario(request, feature, scenario):
    """Print the scenario name before its steps."""
    print(f"\nScenario: {scenario.name}")

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """Print each Gherkin step as it runs."""
    print(f"{step.keyword} {step.name}")



def given(step_text, *args, **kwargs):
    return _given(parsers.parse(step_text), *args, **kwargs)

def when(step_text, *args, **kwargs):
    return _when(parsers.parse(step_text), *args, **kwargs)

def then(step_text, *args, **kwargs):
    return _then(parsers.parse(step_text), *args, **kwargs)