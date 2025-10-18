import pytest
from pages.home_page import HomePage
from resources.testData import CATEGORIES, DROPDOWN_CATEGORIES
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

@pytest.mark.ui
@pytest.mark.parametrize("category_name", list(CATEGORIES.keys()))
def test_category_filter(driver, category_name):
    home = HomePage(driver)
    home.select_category(category_name)
    logger.info(f"Selected category: {category_name}")
    count = home.get_result_count()
    assert count > 0, f"Expected results for category '{category_name}', but got {count} results"
    logger.info(f"Found {count} results for category '{category_name}'")

@pytest.mark.ui
@pytest.mark.parametrize("select_name", list(DROPDOWN_CATEGORIES))
def test_type_dropdown(driver, select_name):
    home = HomePage(driver)
    home.select_type(select_name)
    logger.info(f"Selected type: {select_name}")
    count = home.get_result_count()
    assert count > 0, f"Expected results for '{select_name}', but got {count} results"
    logger.info(f"Found {count} results for type '{select_name}'")

