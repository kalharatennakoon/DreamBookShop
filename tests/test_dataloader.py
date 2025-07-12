import unittest
import pandas as pd
import tempfile
import os
from unittest.mock import patch, MagicMock
import sys
sys.path.append('..')
from dataLoader import DataLoader

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.data_loader = DataLoader()
        
        # Create a temporary CSV file for testing
        self.test_data = {
            'title': ['Book 1', 'Book 2', 'Book 3'],
            'authors': ['Author A', 'Author B', 'Author C'],
            'publication_date': [2020, 2021, 2022],
            'language_code': ['en', 'es', 'fr'],
            'publisher': ['Publisher X', 'Publisher Y', 'Publisher Z'],
            'isbn': ['123456789', '987654321', '456789123']
        }
        
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
        pd.DataFrame(self.test_data).to_csv(self.temp_file.name, index=False)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up test fixtures"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_load_valid_csv(self):
        """Test loading a valid CSV file"""
        result = self.data_loader.load(self.temp_file.name)
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 3)
        self.assertIn('title', result.columns)
        self.assertIn('authors', result.columns)
    
    def test_load_nonexistent_file(self):
        """Test loading a non-existent file"""
        result = self.data_loader.load('nonexistent_file.csv')
        self.assertIsNone(result)
    
    def test_load_empty_filename(self):
        """Test loading with empty filename"""
        result = self.data_loader.load('')
        self.assertIsNone(result)
    
    def test_load_none_filename(self):
        """Test loading with None filename"""
        result = self.data_loader.load(None)
        self.assertIsNone(result)
    
    def test_load_invalid_file_format(self):
        """Test loading a non-CSV file"""
        # Create a temporary text file
        temp_txt = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        temp_txt.write("This is not a CSV file")
        temp_txt.close()
        
        try:
            result = self.data_loader.load(temp_txt.name)
            self.assertIsNone(result)
        finally:
            os.unlink(temp_txt.name)
    
    def test_load_empty_csv(self):
        """Test loading an empty CSV file"""
        empty_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
        empty_file.write("")
        empty_file.close()
        
        try:
            result = self.data_loader.load(empty_file.name)
            self.assertIsNone(result)
        finally:
            os.unlink(empty_file.name)

def run_single_test():
    """Run this test file individually with detailed output"""
    print("=" * 70)
    print("                TESTING DATA LOADER CLASS")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataLoader)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        stream=sys.stdout,
        buffer=True
    )
    
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print("              TEST SUMMARY")
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED!")
        if result.failures:
            print(f"\nFailures ({len(result.failures)}):")
            for test, traceback in result.failures:
                print(f"  - {test}")
                print(f"    {traceback}")
        if result.errors:
            print(f"\nErrors ({len(result.errors)}):")
            for test, traceback in result.errors:
                print(f"  - {test}")
                print(f"    {traceback}")
    
    print("=" * 50)
    return result.wasSuccessful()

if __name__ == '__main__':
    run_single_test()