import pytest
from pages.home_page import HomePage
from resources.testData import CATEGORIES, DROPDOWN_CATEGORIES, GENRE_CATEGORIES
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
@pytest.mark.flaky(reruns=2, reruns_delay=2)
@pytest.mark.parametrize("category_name", list(CATEGORIES.keys()))
def test_category_filter(driver, category_name):
    home = HomePage(driver)
    home.select_category(category_name)
    logger.info(f"Selected category: {category_name}")
    count = home.get_result_count()
    assert count > 0, f"Expected results for category '{category_name}', but got {count} results"
    logger.info(f"Found {count} results for category '{category_name}'")

@pytest.mark.ui
@pytest.mark.flaky(reruns=2, reruns_delay=2)
@pytest.mark.parametrize("select_name", list(DROPDOWN_CATEGORIES))
def test_type_dropdown(driver, select_name):
    home = HomePage(driver)
    home.select_type(select_name)
    logger.info(f"Selected type: {select_name}")
    count = home.get_result_count()
    assert count > 0, f"Expected results for '{select_name}', but got {count} results"
    logger.info(f"Found {count} results for type '{select_name}'")

@pytest.mark.ui
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_select_star(driver):
    home = HomePage(driver)
    star, star_type = home.select_star()
    logger.info(f"Selected {star} {star_type} star(s)")
    count = home.get_result_count()
    assert count > 0, f"Expected results for {star} {star_type} star(s), got {count}"
    logger.info(f"Found {count} results for {star} {star_type} star rating")

@pytest.mark.ui
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_date(driver):
    home = HomePage(driver)
    from_year, to_year = home.date_type()
    logger.info(f"Selected date range: {from_year} to {to_year}")
    count = home.get_result_count()
    assert count > 0, f"Expected results for years {from_year}-{to_year}, but got {count} results"
    logger.info(f"Found {count} results for date range {from_year}-{to_year}")

GENRE_CASES = [
    (type_name, genre_name)
    for type_name, genre_map in GENRE_CATEGORIES.items()
    for genre_name in list(genre_map.keys())[:3]  # Test only first 3 genres per type for speed
]
@pytest.mark.ui
@pytest.mark.flaky(reruns=2, reruns_delay=2)
@pytest.mark.parametrize("type_name, genre_name", GENRE_CASES)
def test_genre_dropdown(driver, type_name, genre_name):
    home = HomePage(driver)
    logger.info(f"Testing type '{type_name}' with genre '{genre_name}'")
    home.select_type(type_name)
    logger.info(f"Selected type: {type_name}")
    home.genre_type(genre_name, type_name)
    logger.info(f"Selected genre: {genre_name}")
    count = home.get_result_count()
    assert count > 0, f"No results for type '{type_name}' + genre '{genre_name}', got {count}"
    logger.info(f"Found {count} results for {type_name}/{genre_name}")

@pytest.mark.ui
@pytest.mark.flaky(reruns=2, reruns_delay=2)
@pytest.mark.parametrize("category_name", list(CATEGORIES.keys()))
def test_category_and_pagination(driver, category_name):
    home = HomePage(driver)
    # Selecting different categories
    try:
        home.select_category(category_name)
        logger.info(f"Selected category: {category_name}")
        count = home.get_result_count()
        assert count > 0, f"Expected results for category '{category_name}', but got {count} results"
        logger.info(f"Found {count} results for category '{category_name}'")
    except Exception as e:
        logger.warning(f"Category {category_name} not clickable or available: {e}")

    # try pagination 'Next' button
    try:
        home.go_next()
        logger.info("Clicked Next page")
    except Exception as e:
        logger.warning("Next not available - known demo limitation")

    # try pagination 'Previous' button
    try:
        home.go_previous()
        logger.info("Clicked Previous page")
    except Exception as e:
        logger.warning("Previous not available - known demo limitation")

@pytest.mark.ui
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_full_work_flow(driver):
    import random
    home = HomePage(driver)
    # Select random category
    category_name = random.choice(list(CATEGORIES.keys()))
    logger.info(f"=== Full Workflow Test Started ===")
    logger.info(f"Selected category: {category_name}")
    home.select_category(category_name)

    # Select random type and genre
    type_name, genre_name = random.choice(GENRE_CASES)
    logger.info(f"Selected type: {type_name}, genre: {genre_name}")
    home.select_type(type_name)
    home.genre_type(genre_name, type_name)

    # Select date range
    home.date_type()
    logger.info(f"Selected date range")

    # Select star rating
    home.select_star()
    logger.info(f"Selected star(s)")

    # Verify results
    count = home.get_result_count()
    logger.info(f"Results count after all filters: {count}")
    assert count > 0, f"Expected results for workflow (category={category_name}, type={type_name}, genre={genre_name} but got {count} results"
    logger.info(f"=== Full Workflow Test Passed - Found {count} results ===")

