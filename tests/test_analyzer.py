import unittest
import pandas as pd
import sys
sys.path.append('..')
from analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = Analyzer()
        
        # Create test data
        self.test_df = pd.DataFrame({
            'title': ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'],
            'authors': ['Author A', 'Author B', 'Author A', 'Author C', 'Author A'],
            'publication_date': [2020, 2021, 2022, 2020, 2023],
            'language_code': ['en', 'es', 'en', 'fr', 'en'],
            'publisher': ['Publisher X', 'Publisher Y', 'Publisher X', 'Publisher Z', 'Publisher X'],
            'isbn': ['123456789', None, '456789123', '789123456', '']
        })
    
    def test_limit_dataset_with_limit(self):
        """Test limiting dataset to specific number of records"""
        result = self.analyzer.limit_dataset(self.test_df, n=3)
        self.assertEqual(len(result), 3)
    
    def test_limit_dataset_no_limit(self):
        """Test dataset without limit (n=None)"""
        result = self.analyzer.limit_dataset(self.test_df, n=None)
        self.assertEqual(len(result), len(self.test_df))
    
    def test_limit_dataset_empty_df(self):
        """Test limiting empty dataframe"""
        empty_df = pd.DataFrame()
        result = self.analyzer.limit_dataset(empty_df, n=5)
        self.assertTrue(result.empty)
    
    def test_analyze_publication_trends_success(self):
        """Test successful publication trends analysis"""
        analysis_data, error = self.analyzer.analyze_publication_trends(self.test_df)
        
        self.assertIsNone(error)
        self.assertIsNotNone(analysis_data)
        self.assertIn('year_counts', analysis_data)
        self.assertIn('total_years', analysis_data)
        self.assertIn('most_productive_year', analysis_data)
    
    def test_analyze_publication_trends_missing_column(self):
        """Test publication trends with missing date column"""
        df_no_date = self.test_df.drop(['publication_date'], axis=1)
        analysis_data, error = self.analyzer.analyze_publication_trends(df_no_date)
        
        self.assertIsNone(analysis_data)
        self.assertIsNotNone(error)
        self.assertIn("Publication date column not found", error)
    
    def test_analyze_top_authors_success(self):
        """Test successful top authors analysis"""
        analysis_data, error = self.analyzer.analyze_top_authors(self.test_df, top_n=3)
        
        self.assertIsNone(error)
        self.assertIsNotNone(analysis_data)
        self.assertIn('author_counts', analysis_data)
        self.assertEqual(analysis_data['top_n'], 3)
        # Author A should be top with 3 books
        self.assertEqual(analysis_data['author_counts'].iloc[0], 3)
    
    def test_analyze_top_authors_missing_column(self):
        """Test top authors with missing authors column"""
        df_no_authors = self.test_df.drop(['authors'], axis=1)
        analysis_data, error = self.analyzer.analyze_top_authors(df_no_authors)
        
        self.assertIsNone(analysis_data)
        self.assertIsNotNone(error)
        self.assertIn("Authors column not found", error)
    
    def test_analyze_language_distribution_success(self):
        """Test successful language distribution analysis"""
        analysis_data, error = self.analyzer.analyze_language_distribution(self.test_df)
        
        self.assertIsNone(error)
        self.assertIsNotNone(analysis_data)
        self.assertIn('lang_counts', analysis_data)
        self.assertIn('lang_percentages', analysis_data)
        self.assertEqual(analysis_data['total_books'], 5)
        # English should be most common (3 out of 5 = 60%)
        self.assertEqual(analysis_data['lang_counts']['en'], 3)
    
    def test_analyze_language_distribution_missing_column(self):
        """Test language distribution with missing language column"""
        df_no_lang = self.test_df.drop(['language_code'], axis=1)
        analysis_data, error = self.analyzer.analyze_language_distribution(df_no_lang)
        
        self.assertIsNone(analysis_data)
        self.assertIsNotNone(error)
        self.assertIn("Language column not found", error)
    
    def test_analyze_books_by_publisher_success(self):
        """Test successful publisher analysis"""
        analysis_data, error = self.analyzer.analyze_books_by_publisher(self.test_df, top_n=5)
        
        self.assertIsNone(error)
        self.assertIsNotNone(analysis_data)
        self.assertIn('publisher_counts', analysis_data)
        self.assertIn('total_publishers', analysis_data)
        # Publisher X should be top with 3 books
        self.assertEqual(analysis_data['publisher_counts'].iloc[0], 3)
    
    def test_analyze_books_by_publisher_missing_column(self):
        """Test publisher analysis with missing publisher column"""
        df_no_publisher = self.test_df.drop(['publisher'], axis=1)
        analysis_data, error = self.analyzer.analyze_books_by_publisher(df_no_publisher)
        
        self.assertIsNone(analysis_data)
        self.assertIsNotNone(error)
        self.assertIn("Publisher column not found", error)
    
    def test_analyze_missing_isbn_success(self):
        """Test successful ISBN analysis"""
        analysis_data, error = self.analyzer.analyze_missing_isbn(self.test_df)
        
        self.assertIsNone(error)
        self.assertIsNotNone(analysis_data)
        self.assertIn('isbn_analysis', analysis_data)
        
        isbn_data = analysis_data['isbn_analysis']['isbn']
        self.assertEqual(isbn_data['total_records'], 5)
        self.assertEqual(isbn_data['missing_count'], 2)  # None and empty string
        self.assertEqual(isbn_data['present_count'], 3)
    
    def test_analyze_missing_isbn_no_column(self):
        """Test ISBN analysis with no ISBN column"""
        df_no_isbn = self.test_df.drop(['isbn'], axis=1)
        analysis_data, error = self.analyzer.analyze_missing_isbn(df_no_isbn)
        
        self.assertIsNone(analysis_data)
        self.assertIsNotNone(error)
        self.assertIn("No ISBN columns found", error)
    
    def test_analyze_books_per_year_by_language_success(self):
        """Test successful year-language analysis"""
        analysis_data, error = self.analyzer.analyze_books_per_year_by_language(self.test_df)
        
        self.assertIsNone(error)
        self.assertIsNotNone(analysis_data)
        self.assertIn('year_lang_counts', analysis_data)
        self.assertIn('years', analysis_data)
        self.assertIn('languages', analysis_data)
    
    def test_analyze_books_per_year_by_language_missing_columns(self):
        """Test year-language analysis with missing columns"""
        df_missing = self.test_df.drop(['publication_date', 'language_code'], axis=1)
        analysis_data, error = self.analyzer.analyze_books_per_year_by_language(df_missing)
        
        self.assertIsNone(analysis_data)
        self.assertIsNotNone(error)
        self.assertIn("publication date and language column(s) not found", error)

def run_single_test():
    """Run this test file individually with detailed output"""
    print("=" * 70)
    print("                TESTING ANALYZER CLASS")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnalyzer)
    
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