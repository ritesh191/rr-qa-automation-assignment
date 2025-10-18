# Test Plan - rr-qa-automation-assignment

## Scope
Automate functional UI and API tests for https://tmdb-discover.surge.sh/ and https://api.themoviedb.org/3

## Test Strategy

### Positive Scenarios (UI)
All positive scenarios cover the main filter types available on the home page:
- **Category filters:** Popular, Trend, Newest, Top Rated
- **Type filters:** TV Shows, Movies
- **Genre filters:** Multiple genres for both Movies and TV Shows
- **Year range filters:** From/To year selection
- **Rating filters:** Star ratings (1-5 stars, half and full)
- **Pagination:** Next/Previous navigation
- **Integration test:** End-to-end workflow combining all filters with random data selection

### Negative Scenarios (UI)
Negative scenarios focus on edge cases and error handling:
- **Invalid search queries:** Non-existent movie/show names
- **Pagination errors:** Last page navigation (known limitation)
- **Multiple genre selection:** Selecting too many genres leading to no results
- **Slug-based URLs:** Direct URL access with category slugs (e.g., /popular, /trend)

### API Scenarios
API tests validate TMDB API endpoints:
- **Popular movies endpoint:** Schema validation and response structure
- **Search functionality:** Query parameters and result validation
- **Negative search:** Non-existent queries returning empty results

## Test Cases

### Positive Test Cases (test_filters_and_pagination.py)

| ID | Test Function | Feature | Description | Status |
|----|---------------|---------|-------------|--------|
| TC_UI_01 | `test_search_title` | Title Search | Validates that searching for "batman" returns valid results and verifies result count > 0 | ✅ Automated |
| TC_UI_02 | `test_category_filter` | Category Filter | Verifies that selecting different categories (Popular, Trend, Newest, Top Rated) displays filtered results. Parametrized test covering all 4 categories | ✅ Automated |
| TC_UI_03 | `test_type_dropdown` | Type Filter | Tests switching between Movie and TV Shows types and validates results are displayed correctly. Parametrized for both types | ✅ Automated |
| TC_UI_04 | `test_select_star` | Star Rating Filter | Validates that selecting a random star rating (1-5 stars, half or full) filters results appropriately. Uses random selection for variety | ✅ Automated |
| TC_UI_05 | `test_date` | Year/Date Filter | Tests date range filtering by selecting random from/to years and validates filtered results. Ensures from_year < to_year | ✅ Automated |
| TC_UI_06 | `test_genre_dropdown` | Genre Filter | Verifies genre filtering for both Movies and TV Shows. Parametrized test covering 3 genres per type (6 total combinations) | ✅ Automated |
| TC_UI_07 | `test_category_and_pagination` | Pagination | Tests category selection combined with pagination (Next/Previous buttons). Handles known demo limitations gracefully | ✅ Automated |
| TC_UI_08 | `test_full_work_flow` | Integration Test | Comprehensive workflow test combining multiple filters (category, type, genre, date range, star rating) to verify end-to-end functionality | ✅ Automated |

### Negative Test Cases (test_negative_cases.py)

| ID | Test Function | Feature | Description | Status |
|----|---------------|---------|-------------|--------|
| TC_NEG_01 | `test_negative_search_title` | Invalid Search | Validates that searching for a non-existent movie ("xyzan") displays "No results found" error message | ✅ Automated |
| TC_NEG_02 | `test_negative_pagination` | Last Page Error | Tests clicking on the last page (page 53111) and verifies error message: "Something went wrong! Please try again later.\nRetry" | ✅ Automated |
| TC_NEG_03 | `test_negative_genre_selection` | Multiple Genre Selection | Selects 6 different genres of a random type (Movie or TV) expecting no results and validates "No results found" error handling | ✅ Automated |
| TC_NEG_04 | `test_negative_slug_access` | Slug-based URL Access | Tests direct URL access with slugs (/popular, /trend, /newest, /top-rated) and validates that slug-based navigation doesn't work as expected. Parametrized for 4 slugs | ✅ Automated |

### API Test Cases (test_api_validation.py)

| ID | Test Function | Feature | Description | Status |
|----|---------------|---------|-------------|--------|
| TC_API_01 | `test_api_popular_movies_schema` | Popular Movies API | Tests TMDB API endpoint for popular movies (/movie/popular). Validates 200 status code and verifies response contains expected data structure with results and total_results | ✅ Automated |
| TC_API_02 | `test_api_search_movie` | Movie Search API | Tests TMDB movie search endpoint (/search/movie) with query parameter 'abc'. Validates response structure including required fields (id, title, overview, release_date, vote_average, etc.) and ensures results are returned | ✅ Automated |
| TC_API_03 | `test_api_search_no_results` | Search No Results (Negative) | Tests search endpoint with non-existent query ('xyzabc123nonexistent'). Validates that API returns 200 status with empty results array and total_results = 0 | ✅ Automated |

## Test Design Techniques
- Equivalence partitioning (rating/year ranges)
- Boundary value analysis (page numbers for pagination)
- Risk-based selection (focus on filters most used)
- Positive & negative tests (including known demo issues)

## Reporting & Logging
- HTML reports generated with `pytest-html` (--html)
- Execution logs saved to `reports/test_log.log`
- Artifacts (reports/logs) to be uploaded in CI pipeline


