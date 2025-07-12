import unittest
import sys
import os

# Add parent directory to path so we can import our modules
sys.path.append('..')

# Import all test classes
from test_dataloader import TestDataLoader
from test_analyzer import TestAnalyzer
from test_visualizer import TestVisualizer
from test_main import TestMain
from test_cli import TestCLI

def create_test_suite():
    """Create a comprehensive test suite for all components"""
    test_suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestDataLoader,
        TestAnalyzer,
        TestVisualizer,
        TestMain,
        TestCLI
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    return test_suite

def run_all_tests():
    """Run all tests and generate report"""
    print("="*70)
    print("         DREAM BOOK SHOP - COMPREHENSIVE TEST SUITE")
    print("="*70)
    
    # Create test suite
    suite = create_test_suite()
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        stream=sys.stdout,
        buffer=True,
        failfast=False
    )
    
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("                        TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED! Your application is working correctly.")
    else:
        print("\n❌ SOME TESTS FAILED! Please check the output above.")
        if result.failures:
            print(f"\nFailures ({len(result.failures)}):")
            for test, traceback in result.failures:
                print(f"  - {test}")
        if result.errors:
            print(f"\nErrors ({len(result.errors)}):")
            for test, traceback in result.errors:
                print(f"  - {test}")
    
    print("="*70)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)