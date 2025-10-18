import pytest
from utilities.driver_factory import get_driver
from utilities.logger import get_logger
from utilities.config import BASE_URL

logger = get_logger()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope='session')
def base_url():
    return BASE_URL

@pytest.fixture
def driver(request, base_url):
    # Initialize browser for UI tests
    browser_name = request.config.getoption("browser_name")
    drv = get_driver(browser_name)
    drv.get(base_url)
    drv.maximize_window()
    yield drv
    try:
        drv.quit()
    except Exception:
        logger.exception("Error quitting driver")

