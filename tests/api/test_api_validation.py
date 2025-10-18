import requests
import pytest
from utilities.config import API_BASE
from utilities.logger import get_logger

logger = get_logger()
# Using the actual working API key
WORKING_API_KEY = "add494e96808c55b3ee7f940c9d5e5b6"
@pytest.mark.api
def test_api_popular_movies_schema():
    """Test movie endpoint with popular category"""
    url = f"{API_BASE}/movie/popular"
    params = {'api_key': WORKING_API_KEY}

    logger.info(f"Testing API endpoint: {url}")
    resp = requests.get(url, params=params, timeout=10)
    logger.info(f"Response status: {resp.status_code}")

    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    data = resp.json()
    logger.info(f"API returned {len(data['results'])} movies, total: {data['total_results']}")


@pytest.mark.api
def test_api_search_movie():
    """Test movie search endpoint with query parameter"""
    url = f"{API_BASE}/search/movie"
    params = {
        'api_key': WORKING_API_KEY,
        'query': 'abc',
        'page': 1
    }

    logger.info(f"Testing search endpoint: {url} with query='abc'")
    resp = requests.get(url, params=params, timeout=10)
    logger.info(f"Response status: {resp.status_code}")

    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"

    # Validate response
    data = resp.json()
    assert len(data['results']) > 0, "Expected search results for 'abc'"
    assert data['total_results'] > 0, f"Expected total_results > 0, got {data['total_results']}"

    logger.info(f"Search returned {len(data['results'])} results on page {data['page']}")
    logger.info(f"Total results found: {data['total_results']} across {data['total_pages']} pages")

    # Validate first result structure
    first_result = data['results'][0]
    required_fields = ['id', 'title', 'original_title', 'overview', 'release_date',
                       'vote_average', 'vote_count', 'popularity']

    for field in required_fields:
        assert field in first_result, f"Result missing required field: {field}"

    logger.info(f"First result: '{first_result.get('title')}' ({first_result.get('release_date')})")


@pytest.mark.api
def test_api_search_no_results():
    """Test search endpoint with query that returns no results"""
    url = f"{API_BASE}/search/movie"
    params = {
        'api_key': WORKING_API_KEY,
        'query': 'xyzabc123nonexistent',
        'page': 1
    }

    logger.info(f"Testing negative case with non-existent query")
    resp = requests.get(url, params=params, timeout=10)

    assert resp.status_code == 200, "API should return 200 even for no results"

    data = resp.json()
    assert 'results' in data, "Response should have 'results' key"
    assert len(data['results']) == 0, "Expected empty results for non-existent movie"
    assert data['total_results'] == 0, "Expected total_results to be 0"

    logger.info("Negative test passed: No results returned as expected")