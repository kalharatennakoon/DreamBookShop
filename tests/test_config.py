# ======================================================================
# TEST CONFIGURATION FILE
# Dream Book Shop Analysis - Comprehensive Test Suite
# ======================================================================
#
# This configuration file defines all 6 main test cases for the
# Dream Book Shop analysis system. Each test case validates core
# functionality with controlled test data.
#
# To run tests:
# 1. Run all tests: python run_comprehensive_tests.py
# 2. Run specific test: python test_comprehensive_analysis.py
# 3. Run with verbose output: python test_comprehensive_analysis.py -v
#
# ======================================================================

# TEST CASE DEFINITIONS
# =====================

# T001: Publication Trends Analysis
# ---------------------------------
# Purpose: Verify correct counting of books published per year
# Input: Known publication years (2001, 2001, 2002, 2003, 2003, 2003, 2004, 2005)
# Expected: {2001: 2, 2002: 1, 2003: 3, 2004: 1, 2005: 1}
# Method: analyze_publication_trends()

T001_PUBLICATION_TRENDS = {
    "test_name": "test_T001_publication_trends_correct_count",
    "description": "Verify the correct count of books published per year",
    "input_data": "Controlled dataset with known publication years",
    "expected_result": "Dictionary showing count of books per year",
    "validation_points": [
        "Year counts are accurate",
        "Most productive year identified correctly",
        "Total years calculated correctly"
    ]
}

# T002: Top Authors Analysis
# --------------------------
# Purpose: Verify identification of top 5 most prolific authors
# Input: Authors with known book counts (Author A: 4, Author B: 2, etc.)
# Expected: Ranked list of authors by book count
# Method: analyze_top_authors()

T002_TOP_AUTHORS = {
    "test_name": "test_T002_top_authors_identification",
    "description": "Verify the function correctly identifies the top 5 authors",
    "input_data": "Dataset with known author distribution",
    "expected_result": "Top authors ranked by book count",
    "validation_points": [
        "Author ranking is correct",
        "Book counts are accurate",
        "All expected authors are present"
    ]
}

# T003: Language Distribution Analysis
# ------------------------------------
# Purpose: Verify correct counting of books by language
# Input: Languages with known distribution (en: 4, es: 2, fr: 2)
# Expected: Language counts and percentages
# Method: analyze_language_distribution()

T003_LANGUAGE_DISTRIBUTION = {
    "test_name": "test_T003_language_distribution_counts",
    "description": "Verify the function correctly counts books by language",
    "input_data": "Dataset with known language distribution",
    "expected_result": "Language counts and percentages",
    "validation_points": [
        "Language counts are accurate",
        "Percentages calculated correctly",
        "Total books count is correct"
    ]
}

# T004: Publisher Analysis
# ------------------------
# Purpose: Verify counting of books grouped by publisher
# Input: Publishers with known book counts (Publisher X: 4, etc.)
# Expected: Publisher counts ranked by number of books
# Method: analyze_books_by_publisher()

T004_PUBLISHER_ANALYSIS = {
    "test_name": "test_T004_publisher_book_counts",
    "description": "Verify the function counts books grouped by publisher correctly",
    "input_data": "Dataset with known publisher distribution",
    "expected_result": "Publisher counts ranked by number of books",
    "validation_points": [
        "Publisher counts are accurate",
        "Ranking is correct",
        "Total publishers count is correct"
    ]
}

# T005: Missing ISBN Analysis
# ---------------------------
# Purpose: Verify correct detection of missing ISBN fields
# Input: Mixed ISBN data (some missing, some empty, some valid)
# Expected: Correct count of missing vs present ISBN values
# Method: analyze_missing_isbn()

T005_MISSING_ISBN = {
    "test_name": "test_T005_missing_isbn_detection",
    "description": "Verify correct detection of missing ISBN fields",
    "input_data": "Dataset with mixed ISBN13 and ISBN10 data",
    "expected_result": "Correct count of missing vs present ISBN values",
    "validation_points": [
        "Missing ISBN13 count is accurate",
        "Missing ISBN10 count is accurate",
        "Percentages calculated correctly",
        "Empty strings counted as missing"
    ]
}

# T006: Books per Year by Language Analysis
# -----------------------------------------
# Purpose: Verify grouping works for year + language combination
# Input: Year-language combinations with known distribution
# Expected: Correct grouping showing books per year by language
# Method: analyze_books_per_year_by_language()
# Note: Uses first 1000 records only

T006_YEAR_LANGUAGE_GROUPING = {
    "test_name": "test_T006_books_per_year_by_language_grouping",
    "description": "Verify grouping works for publication year combined with language",
    "input_data": "Dataset with known year-language distribution",
    "expected_result": "Correct grouping showing books per year broken down by language",
    "validation_points": [
        "Years identified correctly",
        "Languages identified correctly",
        "Year-language combinations accurate",
        "Uses first 1000 records limitation"
    ]
}

# COMPLETE TEST SUITE
# ===================

ALL_TEST_CASES = [
    T001_PUBLICATION_TRENDS,
    T002_TOP_AUTHORS,
    T003_LANGUAGE_DISTRIBUTION,
    T004_PUBLISHER_ANALYSIS,
    T005_MISSING_ISBN,
    T006_YEAR_LANGUAGE_GROUPING
]

# TEST DATA SUMMARY
# =================
# The test suite uses a controlled dataset with 8 records:
# - Years: 2001(2), 2002(1), 2003(3), 2004(1), 2005(1)
# - Authors: Author A(4), Author B(2), Author C(1), Author D(1)
# - Languages: en(4), es(2), fr(2)
# - Publishers: Publisher X(4), Publisher Y(2), Publisher Z(2)
# - ISBN13: 5 present, 3 missing (37.5% missing)
# - ISBN10: 5 present, 3 missing (37.5% missing)

# EXECUTION INSTRUCTIONS
# ======================
# 1. Ensure all dependencies are installed: pandas, unittest
# 2. Run from tests directory: python test_comprehensive_analysis.py
# 3. For verbose output: python test_comprehensive_analysis.py -v
# 4. To run specific test: python -m unittest test_comprehensive_analysis.TestComprehensiveAnalysis.test_T001_publication_trends_correct_count

print("Test Configuration Loaded Successfully!")
print(f"Total Test Cases: {len(ALL_TEST_CASES)}")
for i, test_case in enumerate(ALL_TEST_CASES, 1):
    print(f"  T{i:03d}: {test_case['description']}")
