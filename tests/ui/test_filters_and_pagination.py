import pytest
from pages.home_page import HomePage
from utilities.logger import get_logger

logger = get_logger()

@pytest.mark.ui
def test_search_title(driver):
    home = HomePage(driver)
    home.search("batman")
    logger.info("Searched for 'batman'")
    count = home.get_result_count()
    assert count > 0, "Expected 1 or more results"
    logger.info(f"Found {count} results for 'batman'")

@pytest.mark.ui
def test_negative_search_title(driver):
    home = HomePage(driver)
    home.search("xyzan")
    logger.info("Searched for 'xyzan'")
    error_Message = home.get_error_message()
    logger.info(f"Error message received: '{error_Message}'")
    assert error_Message == "No results found.", "Expected Error Message"
    logger.info("Negative search test passed")

