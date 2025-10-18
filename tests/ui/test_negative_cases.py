import random
import time

import pytest
from pages.home_page import HomePage
from resources.testData import CATEGORIES, DROPDOWN_CATEGORIES, GENRE_CATEGORIES
from utilities.logger import get_logger

logger = get_logger()

@pytest.mark.ui_negative
def test_negative_search_title(driver):
    home = HomePage(driver)
    home.search("xyzan")
    logger.info("Searched for 'xyzan'")
    error_Message = home.get_error_message()
    logger.info(f"Error message received: '{error_Message}'")
    assert error_Message == "No results found.", "Expected Error Message"
    logger.info("Negative search test passed")

@pytest.mark.ui_negative
def test_negative_pagination(driver):
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



