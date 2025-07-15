# Quick Test Reference Guide

## 🎯 Running Individual Tests - Quick Commands

### Simple & Fast (Recommended)
```bash
python run_single_test.py T001        # Run T001
python run_single_test.py author      # Run author test  
python run_single_test.py 3           # Run test #3
python run_single_test.py             # Interactive menu
```

### Advanced Options
```bash
python run_comprehensive_tests.py --test T001          # Run T001
python run_comprehensive_tests.py --test language      # Run by keyword
python run_comprehensive_tests.py --interactive        # Interactive mode
```

### Direct Test File
```bash
python test_comprehensive_analysis.py --test T001      # Run T001
python test_comprehensive_analysis.py --test author    # Run by keyword
```

## 🔍 **NEW! Detailed Test Output**

Each test now shows:
- **Input data** being tested
- **Actual results** from analysis functions  
- **Expected vs Actual** comparisons with ✅/❌ indicators
- **Validation summaries** for easy verification

Example: `python run_single_test.py T001` shows detailed publication trends analysis!

## 📋 Test Quick Reference

| ID   | Keyword    | Test Description                           |
|------|------------|--------------------------------------------|
| T001 | publication| Publication trends over time               |
| T002 | author     | Top 5 most prolific authors              |
| T003 | language   | Language distribution of books            |
| T004 | publisher  | Books by publisher analysis              |
| T005 | isbn       | Missing ISBN detection                    |
| T006 | year-language | Books per year by language (1000 records) |

## 🚀 All Tests
```bash
python run_comprehensive_tests.py              # All 6 tests
python run_all_tests.py                        # All tests + components
```

## 📖 Help & Options
```bash
python run_comprehensive_tests.py --help       # Show all options
python run_comprehensive_tests.py --list       # List all tests
python test_comprehensive_analysis.py --help   # Direct test file help
```
