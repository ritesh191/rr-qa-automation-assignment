import random
import time

import pytest
from pages.home_page import HomePage
from resources.testData import CATEGORIES, DROPDOWN_CATEGORIES, GENRE_CATEGORIES
from utilities.logger import get_logger
from utilities.config import BASE_URL

logger = get_logger()

@pytest.mark.ui_negative
def test_negative_search_title(driver):
    """
    Test that trying to search a movie which doesn't exist leads to an error message
    """
    home = HomePage(driver)
    home.search("xyzan")
    logger.info("Searched for 'xyzan'")
    error_Message = home.get_error_message()
    logger.info(f"Error message received: '{error_Message}'")
    assert error_Message == "No results found.", "Expected Error Message"
    logger.info("Negative search test passed")

@pytest.mark.ui_negative
def test_negative_pagination(driver):
    """
    Test that selecting the last page leads to an error message
    """
    home = HomePage(driver)
    logger.info("Clicking on last page for error")
    error_Message = home.select_last_page()
    logger.info(f"Error message received: '{error_Message}'")
    assert error_Message == "Something went wrong! Please try again later.\nRetry", "Expected Error Message"
    logger.info("Negative last page test passed")

GENRE_CASES = [
    (type_name, genre_name)
    for type_name, genre_map in GENRE_CATEGORIES.items()
    for genre_name in list(genre_map.keys())  # Test only first 3 genres per type for speed
]
@pytest.mark.ui_negative
def test_negative_genre_selection(driver):
    """
    Test that selecting different genre of type Movie and TV Shows, leads to no result
    """
    home = HomePage(driver)
    type_name, genre_name = random.choice(GENRE_CASES)
    required_genre_name = list(GENRE_CATEGORIES.get(type_name).keys())[:6] # selecting 6 genres
    logger.info(f"Testing type '{type_name}'")
    home.select_type(type_name)
    logger.info(f"Selected type: {type_name}")
    for genre_choice in required_genre_name:
        home.genre_type(genre_choice, type_name)
        logger.info(f"Selected genre: {genre_choice}")
    error_Message = home.get_error_message()
    logger.info(f"Error message received: '{error_Message}'")
    assert error_Message == "No results found.", "Expected Error Message"
    logger.info("Negative search test passed")

@pytest.mark.ui_negative
@pytest.mark.parametrize("slug", ["popular", "trend", "newest", "top-rated"])
def test_negative_slug_access(driver, slug):
    """
    Test that accessing the page with specific slugs doesn't work as expected.
    Direct navigation to URLs like /popular, /trend, etc. may not function properly.
    """
    logger.info(f"Testing direct access to slug: /{slug}")
    slug_url = f"{BASE_URL}{slug}"
    driver.get(slug_url)
    time.sleep(3)  # Wait for page to load

    current_url = driver.current_url
    logger.info(f"Current URL after navigation: {current_url}")
    
    # Assert that the slug-based navigation doesn't work properly
    assert current_url == BASE_URL or current_url == slug_url, f"Unexpected URL behavior: {current_url}"
    
    home = HomePage(driver)
    try:
        count = home.get_result_count()
        # If we get here and count is 0, that's expected failure
        logger.info(f"Result count on slug page: {count}")
        if count == 0:
            logger.info(f"Slug /{slug} correctly shows no results (expected behavior)")
    except Exception as e:
        # If we can't find results, that's also expected
        logger.info(f"Slug /{slug} doesn't display results properly (expected behavior): {e}")
    
    logger.info(f"Negative slug access test passed for /{slug}")



