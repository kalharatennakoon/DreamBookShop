# Dream Book Shop - Test Suite Documentation

## Overview

This directory contains comprehensive tests for the Dream Book Shop analysis system. The test suite validates all 6 main analysis functions with controlled test data.

## Test Files

### Core Test Files
- **`test_comprehensive_analysis.py`** - Main comprehensive test file with all 6 test cases
- **`test_config.py`** - Configuration file defining all test cases and their expected behaviors
- **`run_comprehensive_tests.py`** - Advanced test runner with individual test capabilities
- **`run_single_test.py`** - Simple script for running individual tests (NEW! 🎯)

### Individual Component Tests
- `test_dataloader.py` - Tests for data loading functionality
- `test_analyzer.py` - Tests for analysis methods
- `test_visualizer.py` - Tests for visualization components
- `test_main.py` - Tests for main application logic
- `test_cli.py` - Tests for command-line interface

### Test Runners
- `run_all_tests.py` - Runs all tests including comprehensive tests
- `run_comprehensive_tests.py` - Runs only the 6 main comprehensive tests

## The 6 Comprehensive Test Cases

### T001: Publication Trends Analysis
- **Purpose**: Verify correct counting of books published per year
- **Input**: Known publication years (2001, 2001, 2002, 2003, 2003, 2003, 2004, 2005)
- **Expected**: `{2001: 2, 2002: 1, 2003: 3, 2004: 1, 2005: 1}`

### T002: Top Authors Analysis
- **Purpose**: Verify identification of top 5 most prolific authors
- **Input**: Authors with known book counts (Author A: 4, Author B: 2, etc.)
- **Expected**: Ranked list of authors by book count

### T003: Language Distribution Analysis
- **Purpose**: Verify correct counting of books by language
- **Input**: Languages with known distribution (en: 4, es: 2, fr: 2)
- **Expected**: Language counts and percentages

### T004: Publisher Analysis
- **Purpose**: Verify counting of books grouped by publisher
- **Input**: Publishers with known book counts
- **Expected**: Publisher counts ranked by number of books

### T005: Missing ISBN Analysis
- **Purpose**: Verify correct detection of missing ISBN fields
- **Input**: Mixed ISBN data (some missing, some empty, some valid)
- **Expected**: Correct count of missing vs present ISBN values

### T006: Books per Year by Language Analysis
- **Purpose**: Verify grouping works for year + language combination
- **Input**: Year-language combinations with known distribution
- **Expected**: Correct grouping showing books per year by language
- **Note**: Uses first 1000 records only (as per requirement)

## 🎯 **NEW! Detailed Test Case Output**

Each test now shows comprehensive output including:
- **Input Data**: Actual data being analyzed from the test dataset
- **Processing Steps**: What the analysis function is doing
- **Actual Results**: Real output from the analysis functions
- **Expected vs Actual**: Side-by-side comparison with ✅/❌ status indicators
- **Validation Summary**: Clear pass/fail indicators

### Example Output from T001 (Publication Trends):
```
==================================================
T001: PUBLICATION TRENDS ANALYSIS
==================================================
Input Data: Publication years from test dataset
Years in dataset: [2001, 2001, 2002, 2003, 2003, 2003, 2004, 2005]

Actual Results:
Year Counts: {2001: 2, 2002: 1, 2003: 3, 2004: 1, 2005: 1}
Total Years: 5
Most Productive Year: 2003 (3 books)

Expected vs Actual Comparison:
  Year 2001: Expected 2, Got 2 ✅
  Year 2002: Expected 1, Got 1 ✅
  Year 2003: Expected 3, Got 3 ✅

✅ All validations passed!
==================================================
```

### Run Individual Tests (NEW! 🎯)

#### Using the Comprehensive Test Runner
```bash
# Run specific test by ID
python run_comprehensive_tests.py --test T001
python run_comprehensive_tests.py --test T002

# Run test by keyword
python run_comprehensive_tests.py --test author        # Runs T002
python run_comprehensive_tests.py --test language      # Runs T003
python run_comprehensive_tests.py --test publisher     # Runs T004
python run_comprehensive_tests.py --test isbn          # Runs T005
python run_comprehensive_tests.py --test publication   # Runs T001

# Run test by number
python run_comprehensive_tests.py --test 1             # Runs T001
python run_comprehensive_tests.py --test 3             # Runs T003

# Interactive test selection
python run_comprehensive_tests.py --interactive
```

#### Using the Simple Test Runner
```bash
# Quick single test execution
python run_single_test.py T001                         # Run T001
python run_single_test.py author                       # Run author test
python run_single_test.py 3                           # Run test #3
python run_single_test.py                             # Interactive menu
```

#### Using the Test File Directly
```bash
# Run specific test with the test file
python test_comprehensive_analysis.py --test T001
python test_comprehensive_analysis.py --test author    # By keyword
python test_comprehensive_analysis.py --test T003 -v   # With verbose output

# Run by exact method name
python test_comprehensive_analysis.py --method test_T001_publication_trends_correct_count
```

### Run All Comprehensive Tests
```bash
# Basic execution
python run_comprehensive_tests.py

# With verbose output
python run_comprehensive_tests.py --verbose

# List all test cases
python run_comprehensive_tests.py --list
```

### Run Individual Test Cases (Alternative Methods)
```bash
# Using unittest directly
python -m unittest test_comprehensive_analysis.TestComprehensiveAnalysis.test_T001_publication_trends_correct_count

# Run all comprehensive tests with detailed output
python test_comprehensive_analysis.py -v
```

### Run All Tests (Including Component Tests)
```bash
python run_all_tests.py
```

## Available Test Identifiers

### By Test ID
- `T001` - Publication Trends Analysis
- `T002` - Top Authors Analysis  
- `T003` - Language Distribution
- `T004` - Publisher Analysis
- `T005` - Missing ISBN Analysis
- `T006` - Year-Language Grouping

### By Number
- `1` - T001 (Publication Trends)
- `2` - T002 (Top Authors)
- `3` - T003 (Language Distribution)
- `4` - T004 (Publisher Analysis)
- `5` - T005 (Missing ISBN)
- `6` - T006 (Year-Language Grouping)

### By Keywords
- `publication`, `trends` - T001
- `author`, `authors` - T002
- `language`, `languages` - T003
- `publisher`, `publishers` - T004
- `isbn` - T005
- `year-language`, `grouping` - T006

## Test Data

The comprehensive tests use a controlled dataset with 8 records:

- **Years**: 2001(2), 2002(1), 2003(3), 2004(1), 2005(1)
- **Authors**: Author A(4), Author B(2), Author C(1), Author D(1)
- **Languages**: en(4), es(2), fr(2)
- **Publishers**: Publisher X(4), Publisher Y(2), Publisher Z(2)
- **ISBN13**: 5 present, 3 missing (37.5% missing)
- **ISBN10**: 5 present, 3 missing (37.5% missing)

## Expected Output

When all tests pass, you should see:
```
============================================================
TEST EXECUTION SUMMARY
============================================================
Tests Run: 6
Failures: 0
Errors: 0
Success Rate: 100.0%

🎉 ALL TESTS PASSED! The analysis system is working correctly.
============================================================
```

## Configuration

The `test_config.py` file contains detailed configuration for each test case, including:
- Test descriptions
- Input data specifications
- Expected results
- Validation points

This makes it easy to understand what each test validates and modify test parameters if needed.

## Requirements

- Python 3.x
- pandas
- unittest (built-in)
- All Dream Book Shop analysis modules (analyzer.py, etc.)

## Troubleshooting

1. **Import Errors**: Make sure you're running from the tests directory
2. **Module Not Found**: Ensure the parent directory is in the Python path
3. **Test Failures**: Check that the analyzer methods haven't changed their return format

For detailed test output, always use the `-v` or `--verbose` flag.
