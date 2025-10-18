# Test Plan - rr-qa-automation-assignment

## Scope
Automate functional UI and API tests for https://tmdb-discover.surge.sh/

## Test Cases (selected)

| ID | Feature | Description | Type |
|----|---------|-------------|------|
| TC_UI_01 | Category Filter | Verify selecting Popular/Trending/Newest/Top Rated updates results | Functional |
| TC_UI_02 | Type Filter | Verify switching between Movies and TV Shows filters results correctly | Functional |
| TC_UI_03 | Title Search | Verify searching a title filters results to matching titles | Functional |
| TC_UI_04 | Year & Rating Filter | Verify Year/Rating filters restrict results appropriately | Functional |
| TC_UI_05 | Genre Filter | Verify selecting a genre filters results | Functional |
| TC_UI_06 | Pagination | Validate "Next" and "Previous" navigation and handle known demo negative cases | Functional / Negative |
| TC_UI_07 | Slug Refresh Negative | Refresh page with slug (e.g., /popular) and assert expected graceful failure handling | Negative |
| TC_API_01 | API Status | Verify relevant TMDB API endpoints return 200 and expected JSON schema | API |
| TC_API_02 | API vs UI Consistency | Cross-check API results against UI rendered items for a selected filter | Integration |

## Test Design Techniques
- Equivalence partitioning (rating/year ranges)
- Boundary value analysis (page numbers for pagination)
- Risk-based selection (focus on filters most used)
- Positive & negative tests (including known demo issues)

## Reporting & Logging
- HTML reports generated with `pytest-html` (--html)
- Execution logs saved to `reports/test_log.log`
- Artifacts (reports/logs) to be uploaded in CI pipeline


