#!/usr/bin/env python3
"""
Comprehensive Test Runner for Dream Book Shop Analysis
======================================================

This script runs all 6 main test cases defined in the test configuration.
It provides a simple way to execute and monitor all critical functionality tests.

Usage:
    python run_comprehensive_tests.py                          # Run all tests
    python run_comprehensive_tests.py --verbose                # Run with detailed output
    python run_comprehensive_tests.py --list                   # List all available tests
    python run_comprehensive_tests.py --test T001              # Run specific test (T001-T006)
    python run_comprehensive_tests.py --test publication       # Run test by keyword
    python run_comprehensive_tests.py --interactive            # Interactive test selection
"""

import unittest
import sys
import os
import argparse

# Add parent directory to path for imports
sys.path.append('..')

# Import test configuration
from test_config import ALL_TEST_CASES
from test_comprehensive_analysis import TestComprehensiveAnalysis

def list_test_cases():
    """Display all available test cases"""
    print("\n" + "="*60)
    print("DREAM BOOK SHOP - COMPREHENSIVE TEST CASES")
    print("="*60)
    
    for i, test_case in enumerate(ALL_TEST_CASES, 1):
        test_id = f"T{i:03d}"
        print(f"\n{test_id}: {test_case['description']}")
        print(f"      Method: {test_case['test_name']}")
        print(f"      Input:  {test_case['input_data']}")
        print(f"      Result: {test_case['expected_result']}")
        print(f"      Keywords: {get_test_keywords(test_case)}")
    
    print(f"\nTotal Test Cases: {len(ALL_TEST_CASES)}")
    print("\nUsage Examples:")
    print("  python run_comprehensive_tests.py --test T001     # Run specific test by ID")
    print("  python run_comprehensive_tests.py --test author   # Run test by keyword")
    print("  python run_comprehensive_tests.py --interactive   # Interactive selection")
    print("="*60)

def get_test_keywords(test_case):
    """Extract keywords from test case for easier selection"""
    keywords = []
    desc = test_case['description'].lower()
    
    if 'publication' in desc or 'year' in desc:
        keywords.append('publication')
    if 'author' in desc:
        keywords.append('author')
    if 'language' in desc:
        keywords.append('language')
    if 'publisher' in desc:
        keywords.append('publisher')
    if 'isbn' in desc:
        keywords.append('isbn')
    if 'trend' in desc:
        keywords.append('trends')
    
    return ', '.join(keywords)

def find_test_by_identifier(identifier):
    """Find test case by ID (T001-T006) or keyword"""
    identifier = identifier.lower().strip()
    
    # Check if it's a test ID (T001, T002, etc.)
    if identifier.startswith('t') and identifier[1:].isdigit():
        test_num = int(identifier[1:])
        if 1 <= test_num <= len(ALL_TEST_CASES):
            return test_num - 1, ALL_TEST_CASES[test_num - 1]
    
    # Check if it's just a number (001, 1, etc.)
    if identifier.isdigit():
        test_num = int(identifier)
        if 1 <= test_num <= len(ALL_TEST_CASES):
            return test_num - 1, ALL_TEST_CASES[test_num - 1]
    
    # Search by keyword in description
    for i, test_case in enumerate(ALL_TEST_CASES):
        desc = test_case['description'].lower()
        test_name = test_case['test_name'].lower()
        
        if (identifier in desc or identifier in test_name or 
            identifier in get_test_keywords(test_case).lower()):
            return i, test_case
    
    return None, None

def interactive_test_selection():
    """Interactive test selection menu"""
    while True:
        print("\n" + "="*60)
        print("INTERACTIVE TEST SELECTION")
        print("="*60)
        
        for i, test_case in enumerate(ALL_TEST_CASES, 1):
            print(f"{i}. T{i:03d}: {test_case['description']}")
        
        print(f"{len(ALL_TEST_CASES) + 1}. Run ALL tests")
        print(f"{len(ALL_TEST_CASES) + 2}. Exit")
        print("="*60)
        
        try:
            choice = input("\nEnter your choice (1-{}): ".format(len(ALL_TEST_CASES) + 2)).strip()
            
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(ALL_TEST_CASES):
                    return choice_num - 1, ALL_TEST_CASES[choice_num - 1]
                elif choice_num == len(ALL_TEST_CASES) + 1:
                    return None, None  # Run all tests
                elif choice_num == len(ALL_TEST_CASES) + 2:
                    print("Exiting...")
                    sys.exit(0)
            
            print("Invalid choice! Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}. Please try again.")

def run_single_test(test_index, test_case, verbose=False):
    """Run a single specific test case"""
    test_id = f"T{test_index + 1:03d}"
    test_method = test_case['test_name']
    
    print("\n" + "="*60)
    print(f"RUNNING SINGLE TEST: {test_id}")
    print("="*60)
    print(f"Test: {test_case['description']}")
    print(f"Method: {test_method}")
    print(f"Input: {test_case['input_data']}")
    print(f"Expected: {test_case['expected_result']}")
    print("-" * 60)
    
    # Create test suite with only the specific test
    suite = unittest.TestSuite()
    test_class = TestComprehensiveAnalysis
    
    # Add only the specific test method
    suite.addTest(test_class(test_method))
    
    # Configure test runner with custom stream to capture output
    import io
    test_output = io.StringIO()
    
    verbosity = 2 if verbose else 1
    runner = unittest.TextTestRunner(
        stream=test_output,
        verbosity=verbosity,
        descriptions=True,
        failfast=True  # Stop on first failure for single test
    )
    
    # Run the test
    print(f"Executing test {test_id}...\n")
    result = runner.run(suite)
    
    # Get the output from test execution
    test_output_str = test_output.getvalue()
    
    # Print the test output (which now includes our detailed output)
    print(test_output_str)
    
    # Display result summary
    print("\n" + "="*60)
    print(f"TEST {test_id} EXECUTION RESULT")
    print("="*60)
    
    if result.wasSuccessful():
        print(f"✅ TEST {test_id} PASSED!")
        print(f"   {test_case['description']}")
        print("   All validations completed successfully.")
    else:
        print(f"❌ TEST {test_id} FAILED!")
        if result.failures:
            print("   FAILURES:")
            for test, failure in result.failures:
                print(f"   - {failure}")
        if result.errors:
            print("   ERRORS:")
            for test, error in result.errors:
                print(f"   - {error}")
    
    print("="*60)
    return result.wasSuccessful()

def run_comprehensive_tests(verbose=False):
    """Run all comprehensive test cases"""
    print("\n" + "="*60)
    print("RUNNING COMPREHENSIVE TEST SUITE")
    print("="*60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestComprehensiveAnalysis)
    
    # Configure test runner
    verbosity = 2 if verbose else 1
    runner = unittest.TextTestRunner(
        verbosity=verbosity,
        descriptions=True,
        failfast=False
    )
    
    # Run tests
    print(f"Executing {suite.countTestCases()} test cases...\n")
    result = runner.run(suite)
    
    # Display summary
    print("\n" + "="*60)
    print("TEST EXECUTION SUMMARY")
    print("="*60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILED TESTS:")
        for test, failure in result.failures:
            print(f"  - {test}")
    
    if result.errors:
        print(f"\nERROR TESTS:")
        for test, error in result.errors:
            print(f"  - {test}")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! The analysis system is working correctly.")
    else:
        print("\n❌ SOME TESTS FAILED! Please review the results above.")
    
    print("="*60)
    
    return result.wasSuccessful()

def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description='Run comprehensive tests for Dream Book Shop Analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python run_comprehensive_tests.py                    # Run all tests
  python run_comprehensive_tests.py --verbose          # Run all tests with verbose output
  python run_comprehensive_tests.py --list             # List all available tests
  python run_comprehensive_tests.py --test T001        # Run specific test T001
  python run_comprehensive_tests.py --test author      # Run test containing 'author'
  python run_comprehensive_tests.py --interactive      # Interactive test selection
  python run_comprehensive_tests.py --test T003 -v     # Run T003 with verbose output

Test Identifiers:
  T001, T002, T003, T004, T005, T006                   # Test by ID
  1, 2, 3, 4, 5, 6                                     # Test by number
  publication, author, language, publisher, isbn       # Test by keyword
        '''
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Run tests with verbose output'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all available test cases'
    )
    
    parser.add_argument(
        '--test', '-t',
        type=str,
        help='Run specific test by ID (T001-T006), number (1-6), or keyword (author, language, etc.)'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Interactive test selection menu'
    )
    
    args = parser.parse_args()
    
    # Load test configuration
    try:
        from test_config import ALL_TEST_CASES
        if not args.list and not args.interactive:
            print(f"Loaded {len(ALL_TEST_CASES)} test case configurations")
    except ImportError:
        print("Warning: Could not load test configuration file")
    
    # Handle different modes
    if args.list:
        list_test_cases()
        return
    
    if args.interactive:
        test_index, test_case = interactive_test_selection()
        if test_case is None:  # Run all tests was selected
            success = run_comprehensive_tests(verbose=args.verbose)
        else:  # Specific test was selected
            success = run_single_test(test_index, test_case, verbose=args.verbose)
        sys.exit(0 if success else 1)
    
    if args.test:
        # Run specific test
        test_index, test_case = find_test_by_identifier(args.test)
        if test_case is None:
            print(f"Error: Test '{args.test}' not found!")
            print("\nAvailable tests:")
            for i, tc in enumerate(ALL_TEST_CASES, 1):
                print(f"  T{i:03d}: {tc['description']}")
                print(f"        Keywords: {get_test_keywords(tc)}")
            sys.exit(1)
        
        success = run_single_test(test_index, test_case, verbose=args.verbose)
        sys.exit(0 if success else 1)
    
    # Default: run all tests
    success = run_comprehensive_tests(verbose=args.verbose)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
