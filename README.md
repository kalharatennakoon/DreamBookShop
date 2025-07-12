# Dream Book Shop Analysis Tool

A comprehensive Python application for analyzing book datasets with interactive visualizations and statistical insights.

## 📋 Project Overview

This tool provides detailed analysis of book publication data including trends over time, author productivity, language distribution, publisher statistics, ISBN completeness, and year-by-language breakdowns.

## 🏗️ Project Structure

```
DreamBookShop/
├── main.py              # Main application with interactive menu
├── cli.py               # Command-line interface
├── dataLoader.py        # Dataset loading and preprocessing
├── analyzer.py          # Data analysis algorithms
├── visualizer.py        # Data visualization and charts
├── Dataset_Books.csv    # Sample dataset
├── tests/
│   ├── test_dataloader.py    # DataLoader unit tests
│   ├── test_analyzer.py      # Analyzer unit tests  
│   ├── test_visualizer.py    # Visualizer unit tests
│   ├── test_main.py          # Main application tests
│   ├── test_cli.py           # CLI interface tests
│   ├── test_example.py       # Example/demo tests
│   └── run_all_tests.py      # Test suite runner
└── README.md           # Project documentation
```

## 🔧 Features

### Data Analysis Capabilities
- **Publication Trends**: Analyze books published over time with trend analysis
- **Author Analysis**: Identify top 5 most prolific authors
- **Language Distribution**: Breakdown of books by language with percentages
- **Publisher Statistics**: Top publishers by number of publications
- **ISBN Analysis**: Data quality assessment for missing ISBN information
- **Year-Language Cross Analysis**: Books per year categorized by language

### Visualization Types
- Line charts with trend analysis
- Horizontal and vertical bar charts
- Pie charts for distribution analysis
- Clustered bar charts for multi-dimensional data
- Heatmaps for pattern recognition
- Stacked bar charts for comparative analysis

## 📦 Requirements

### Dependencies
```bash
pip install pandas matplotlib seaborn numpy
```

### System Requirements
- Python 3.7+
- macOS/Windows/Linux
- 4GB RAM minimum
- Display capable of showing matplotlib graphs

## 🚀 How to Run

### Interactive Mode (Recommended)
```bash
python main.py
```
This launches an interactive menu where you can:
1. Browse through 6 different analysis options
2. View results in terminal and graphical format
3. Navigate between analyses seamlessly
4. Exit gracefully with Ctrl+C

### Command Line Mode
```bash
# Show all available options
python cli.py --help

# Run specific analyses
python cli.py --trends                    # Publication trends
python cli.py --authors                   # Top authors
python cli.py --languages                 # Language distribution
python cli.py --publishers                # Publisher statistics
python cli.py --isbn                      # ISBN analysis
python cli.py --year-language             # Year-Language cross analysis
```

## 📊 Example Analysis

### Publication Trends
```bash
python cli.py --trends
```
- **Output**: Displays a line chart of publications over the years with a fitted trend line.

### Top Authors
```bash
python cli.py --authors
```
- **Output**: Lists the top 5 authors with the most publications in the dataset.

### Language Distribution
```bash
python cli.py --languages
```
- **Output**: Pie chart showing the percentage of books written in different languages.

### Publisher Statistics
```bash
python cli.py --publishers
```
- **Output**: Horizontal bar chart of top publishers by number of publications.

### ISBN Analysis
```bash
python cli.py --isbn
```
- **Output**: Summary of ISBN data quality, including number of missing ISBNs.

### Year-Language Cross Analysis
```bash
python cli.py --year-language
```
- **Output**: Heatmap showing the number of books published each year, broken down by language.

## 🧪 Testing

To ensure the reliability of the tool, comprehensive unit tests are provided in the `tests/` directory.

### Running Tests

#### Run All Tests
```bash
cd tests
python run_all_tests.py
```

#### Run Individual Test Suites
```bash
cd tests
python test_dataloader.py      # Test data loading functionality
python test_analyzer.py        # Test analysis algorithms
python test_visualizer.py      # Test visualization components
python test_main.py           # Test main application logic
python test_cli.py            # Test command-line interface
python test_example.py        # Run example tests
```

#### Run with Verbose Output
```bash
python test_dataloader.py -v   # Detailed test execution info
```

### Test Results Summary

| Test ID | Test Suite | Test Name | Component | Expected Result | Actual Result | Status | Last Updated |
|---------|------------|-----------|-----------|----------------|---------------|--------|--------------|
| **DataLoader Tests** |
| DL001 | TestDataLoader | test_load_valid_csv | DataLoader | Load CSV successfully | DataFrame returned | ✅ PASS | 2025-01-12 |
| DL002 | TestDataLoader | test_load_nonexistent_file | DataLoader | Return None for missing file | None returned | ✅ PASS | 2025-01-12 |
| DL003 | TestDataLoader | test_load_empty_filename | DataLoader | Return None for empty filename | None returned | ✅ PASS | 2025-01-12 |
| DL004 | TestDataLoader | test_load_none_filename | DataLoader | Return None for None filename | None returned | ✅ PASS | 2025-01-12 |
| DL005 | TestDataLoader | test_load_invalid_file_format | DataLoader | Return None for non-CSV file | None returned | ✅ PASS | 2025-01-12 |
| DL006 | TestDataLoader | test_load_empty_csv | DataLoader | Return None for empty CSV | None returned | ✅ PASS | 2025-01-12 |
| **Analyzer Tests** |
| AN001 | TestAnalyzer | test_limit_dataset_with_limit | Analyzer | Limit dataset to n records | Limited DataFrame | ✅ PASS | 2025-01-12 |
| AN002 | TestAnalyzer | test_limit_dataset_no_limit | Analyzer | Return full dataset when n=None | Full DataFrame | ✅ PASS | 2025-01-12 |
| AN003 | TestAnalyzer | test_limit_dataset_empty_df | Analyzer | Handle empty DataFrame | Empty DataFrame | ✅ PASS | 2025-01-12 |
| AN004 | TestAnalyzer | test_analyze_publication_trends_success | Analyzer | Analyze publication trends | Trend data returned | ✅ PASS | 2025-01-12 |
| AN005 | TestAnalyzer | test_analyze_publication_trends_missing_column | Analyzer | Handle missing date column | Error message returned | ✅ PASS | 2025-01-12 |
| AN006 | TestAnalyzer | test_analyze_top_authors_success | Analyzer | Analyze top authors | Author counts returned | ✅ PASS | 2025-01-12 |
| AN007 | TestAnalyzer | test_analyze_top_authors_missing_column | Analyzer | Handle missing authors column | Error message returned | ✅ PASS | 2025-01-12 |
| AN008 | TestAnalyzer | test_analyze_language_distribution_success | Analyzer | Analyze language distribution | Language stats returned | ✅ PASS | 2025-01-12 |
| AN009 | TestAnalyzer | test_analyze_language_distribution_missing_column | Analyzer | Handle missing language column | Error message returned | ✅ PASS | 2025-01-12 |
| AN010 | TestAnalyzer | test_analyze_books_by_publisher_success | Analyzer | Analyze publisher statistics | Publisher counts returned | ✅ PASS | 2025-01-12 |
| AN011 | TestAnalyzer | test_analyze_books_by_publisher_missing_column | Analyzer | Handle missing publisher column | Error message returned | ✅ PASS | 2025-01-12 |
| AN012 | TestAnalyzer | test_analyze_missing_isbn_success | Analyzer | Analyze ISBN completeness | ISBN analysis returned | ✅ PASS | 2025-01-12 |
| AN013 | TestAnalyzer | test_analyze_missing_isbn_no_column | Analyzer | Handle missing ISBN column | Error message returned | ✅ PASS | 2025-01-12 |
| AN014 | TestAnalyzer | test_analyze_books_per_year_by_language_success | Analyzer | Analyze year-language data | Cross-analysis returned | ✅ PASS | 2025-01-12 |
| AN015 | TestAnalyzer | test_analyze_books_per_year_by_language_missing_columns | Analyzer | Handle missing required columns | Error message returned | ✅ PASS | 2025-01-12 |
| **Visualizer Tests** |
| VZ001 | TestVisualizer | test_display_first_records_valid_data | Visualizer | Display dataset records | Records displayed | ✅ PASS | 2025-01-12 |
| VZ002 | TestVisualizer | test_display_first_records_none_data | Visualizer | Handle None dataset | Error message shown | ✅ PASS | 2025-01-12 |
| VZ003 | TestVisualizer | test_display_first_records_empty_data | Visualizer | Handle empty dataset | Empty message shown | ✅ PASS | 2025-01-12 |
| VZ004 | TestVisualizer | test_display_dataset_info_valid_data | Visualizer | Display dataset info | Info displayed | ✅ PASS | 2025-01-12 |
| VZ005 | TestVisualizer | test_display_dataset_info_none_data | Visualizer | Handle None dataset | Error message shown | ✅ PASS | 2025-01-12 |
| VZ006 | TestVisualizer | test_visualize_publication_trends_valid_data | Visualizer | Create publication trend chart | Chart created and shown | ✅ PASS | 2025-01-12 |
| VZ007 | TestVisualizer | test_visualize_publication_trends_none_data | Visualizer | Handle None trend data | None returned | ✅ PASS | 2025-01-12 |
| VZ008 | TestVisualizer | test_visualize_publication_trends_empty_data | Visualizer | Handle empty trend data | Error message shown | ✅ PASS | 2025-01-12 |
| VZ009 | TestVisualizer | test_visualize_top_authors_valid_data | Visualizer | Create author chart | Chart created and shown | ✅ PASS | 2025-01-12 |
| VZ010 | TestVisualizer | test_visualize_top_authors_none_data | Visualizer | Handle None author data | None returned | ✅ PASS | 2025-01-12 |
| VZ011 | TestVisualizer | test_visualize_language_distribution_valid_data | Visualizer | Create language pie chart | Chart created and shown | ✅ PASS | 2025-01-12 |
| VZ012 | TestVisualizer | test_visualize_books_by_publisher_valid_data | Visualizer | Create publisher chart | Chart created and shown | ✅ PASS | 2025-01-12 |
| VZ013 | TestVisualizer | test_visualize_missing_isbn_valid_data | Visualizer | Create ISBN analysis chart | Chart created and shown | ✅ PASS | 2025-01-12 |
| VZ014 | TestVisualizer | test_visualize_missing_isbn_no_graph | Visualizer | Display ISBN data without graph | Data displayed | ✅ PASS | 2025-01-12 |
| VZ015 | TestVisualizer | test_visualize_books_per_year_by_language_valid_data | Visualizer | Create year-language heatmap | Chart created and shown | ✅ PASS | 2025-01-12 |
| **Main Application Tests** |
| MA001 | TestMain | test_init | Main | Initialize main application | All components initialized | ✅ PASS | 2025-01-12 |
| MA002 | TestMain | test_run_successful_load | Main | Run with successful data load | Menu shown | ✅ PASS | 2025-01-12 |
| MA003 | TestMain | test_run_failed_load | Main | Handle failed data load | Error message shown | ✅ PASS | 2025-01-12 |
| MA004 | TestMain | test_show_menu_exit | Main | Menu exit functionality | Graceful exit | ✅ PASS | 2025-01-12 |
| MA005 | TestMain | test_show_menu_invalid_choice | Main | Handle invalid menu choice | Error message shown | ✅ PASS | 2025-01-12 |
| MA006 | TestMain | test_show_menu_keyboard_interrupt | Main | Handle Ctrl+C interrupt | Graceful interrupt handling | ✅ PASS | 2025-01-12 |
| MA007 | TestMain | test_get_dataset | Main | Retrieve loaded dataset | Dataset returned | ✅ PASS | 2025-01-12 |
| MA008 | TestMain | test_analyze_and_visualize_publication_trends | Main | Execute publication analysis | Analysis completed | ✅ PASS | 2025-01-12 |
| MA009 | TestMain | test_analyze_and_visualize_publication_trends_with_error | Main | Handle analysis error | Error message shown | ✅ PASS | 2025-01-12 |
| MA010 | TestMain | test_display_missing_isbn_data_none | Main | Handle None ISBN data | No data message shown | ✅ PASS | 2025-01-12 |
| MA011 | TestMain | test_display_missing_isbn_data_empty | Main | Handle empty ISBN analysis | No data message shown | ✅ PASS | 2025-01-12 |
| MA012 | TestMain | test_display_missing_isbn_data_valid | Main | Display valid ISBN data | Data displayed | ✅ PASS | 2025-01-12 |
| **CLI Tests** |
| CLI001 | TestCLI | test_init | CLI | Initialize CLI | CLI initialized with main app | ✅ PASS | 2025-01-12 |
| CLI002 | TestCLI | test_create_parser | CLI | Create argument parser | Parser created with arguments | ✅ PASS | 2025-01-12 |
| CLI003 | TestCLI | test_load_dataset_success | CLI | Load dataset successfully | Dataset loaded | ✅ PASS | 2025-01-12 |
| CLI004 | TestCLI | test_load_dataset_failure | CLI | Handle dataset load failure | Error message shown | ✅ PASS | 2025-01-12 |
| CLI005 | TestCLI | test_run_single_analysis | CLI | Run single analysis command | Analysis executed | ✅ PASS | 2025-01-12 |
| CLI006 | TestCLI | test_run_multiple_analyses | CLI | Run multiple analysis commands | Multiple analyses executed | ✅ PASS | 2025-01-12 |
| CLI007 | TestCLI | test_run_menu_mode | CLI | Run interactive menu mode | Menu shown | ✅ PASS | 2025-01-12 |
| CLI008 | TestCLI | test_run_load_failure_exit | CLI | Exit on load failure | System exit called | ✅ PASS | 2025-01-12 |
| CLI009 | TestCLI | test_run_analysis_trends | CLI | Execute trends analysis | Trends analysis completed | ✅ PASS | 2025-01-12 |
| CLI010 | TestCLI | test_run_analysis_with_error | CLI | Handle analysis error | Error message shown | ✅ PASS | 2025-01-12 |
| CLI011 | TestCLI | test_run_analysis_keyboard_interrupt | CLI | Handle analysis interrupt | Interrupt handled gracefully | ✅ PASS | 2025-01-12 |
| **Example Tests** |
| EX001 | TestExample | test_example_pass | Example | Basic arithmetic test | 1+1=2 validated | ✅ PASS | 2025-01-12 |
| EX002 | TestExample | test_example_string | Example | String operation test | String uppercase validated | ✅ PASS | 2025-01-12 |
| EX003 | TestExample | test_example_list | Example | List operation test | List operations validated | ✅ PASS | 2025-01-12 |

### Test Coverage Summary

| Component | Total Tests | Passed | Failed | Coverage |
|-----------|-------------|---------|---------|----------|
| **DataLoader** | 6 | 6 | 0 | 100% |
| **Analyzer** | 15 | 15 | 0 | 100% |
| **Visualizer** | 15 | 15 | 0 | 100% |
| **Main** | 12 | 12 | 0 | 100% |
| **CLI** | 11 | 11 | 0 | 100% |
| **Example** | 3 | 3 | 0 | 100% |
| **TOTAL** | **62** | **62** | **0** | **100%** |

### Key Test Features

- ✅ **Comprehensive Coverage**: All critical functions tested
- ✅ **Error Handling**: Invalid inputs and edge cases covered
- ✅ **Mocking**: External dependencies properly mocked
- ✅ **Data Validation**: Input/output validation for all components
- ✅ **Integration Testing**: Component interaction testing
- ✅ **Custom Test Runner**: Detailed test summaries with ✅/❌ indicators

---

Thank you for using the Dream Book Shop Analysis Tool! Happy reading and analyzing! 📚



