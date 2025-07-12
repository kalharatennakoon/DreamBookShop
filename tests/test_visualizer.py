import unittest
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import sys
from unittest.mock import patch, MagicMock
sys.path.append('..')
from visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.visualizer = Visualizer()
        
        # Sample analysis data for testing
        self.publication_data = {
            'year_counts': pd.Series({2020: 100, 2021: 150, 2022: 120}),
            'total_years': 3,
            'most_productive_year': 2021,
            'most_productive_count': 150,
            'least_productive_year': 2020,
            'least_productive_count': 100
        }
        
        self.author_data = {
            'author_counts': pd.Series({'Author A': 15, 'Author B': 12, 'Author C': 10}),
            'top_n': 3
        }
        
        self.language_data = {
            'lang_counts': pd.Series({'en': 200, 'es': 100, 'fr': 50}),
            'lang_percentages': pd.Series({'en': 57.1, 'es': 28.6, 'fr': 14.3}),
            'total_books': 350
        }
        
        self.publisher_data = {
            'publisher_counts': pd.Series({'Publisher A': 50, 'Publisher B': 30, 'Publisher C': 20}),
            'total_publishers': 10,
            'top_n': 3
        }
        
        self.isbn_data = {
            'isbn_analysis': {
                'isbn': {
                    'total_records': 1000,
                    'present_count': 950,
                    'missing_count': 50,
                    'missing_percentage': 5.0
                }
            }
        }
        
        self.year_lang_data = {
            'year_lang_counts': pd.DataFrame({
                'en': [100, 120, 110],
                'es': [50, 60, 55]
            }, index=[2020, 2021, 2022]),
            'years': [2020, 2021, 2022],
            'languages': ['en', 'es']
        }
    
    def test_display_first_records_valid_data(self):
        """Test displaying first records with valid data"""
        test_df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': ['a', 'b', 'c', 'd', 'e']
        })
        
        with patch('builtins.print') as mock_print:
            self.visualizer.display_first_records(test_df, n=3)
            mock_print.assert_called()
    
    def test_display_first_records_none_data(self):
        """Test displaying first records with None data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.display_first_records(None, n=3)
            mock_print.assert_called_with("Error: No dataset provided to display.")
    
    def test_display_first_records_empty_data(self):
        """Test displaying first records with empty dataframe"""
        empty_df = pd.DataFrame()
        with patch('builtins.print') as mock_print:
            self.visualizer.display_first_records(empty_df, n=3)
            mock_print.assert_called_with("The dataset is empty.")
    
    def test_display_dataset_info_valid_data(self):
        """Test displaying dataset info with valid data"""
        test_df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })
        
        with patch('builtins.print') as mock_print:
            self.visualizer.display_dataset_info(test_df)
            mock_print.assert_called()
    
    def test_display_dataset_info_none_data(self):
        """Test displaying dataset info with None data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.display_dataset_info(None)
            mock_print.assert_called_with("Error: No dataset provided.")
    
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.pause')
    def test_visualize_publication_trends_valid_data(self, mock_pause, mock_show):
        """Test publication trends visualization with valid data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_publication_trends(self.publication_data)
            mock_print.assert_called()
            mock_show.assert_called()
    
    def test_visualize_publication_trends_none_data(self):
        """Test publication trends visualization with None data"""
        result = self.visualizer.visualize_publication_trends(None)
        self.assertIsNone(result)
    
    def test_visualize_publication_trends_empty_data(self):
        """Test publication trends visualization with empty data"""
        empty_data = {'year_counts': pd.Series(dtype=int)}
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_publication_trends(empty_data)
            mock_print.assert_called_with("No publication data available for visualization.")
    
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.pause')
    def test_visualize_top_authors_valid_data(self, mock_pause, mock_show):
        """Test top authors visualization with valid data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_top_authors(self.author_data)
            mock_print.assert_called()
            mock_show.assert_called()
    
    def test_visualize_top_authors_none_data(self):
        """Test top authors visualization with None data"""
        result = self.visualizer.visualize_top_authors(None)
        self.assertIsNone(result)
    
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.pause')
    def test_visualize_language_distribution_valid_data(self, mock_pause, mock_show):
        """Test language distribution visualization with valid data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_language_distribution(self.language_data)
            mock_print.assert_called()
            mock_show.assert_called()
    
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.pause')
    def test_visualize_books_by_publisher_valid_data(self, mock_pause, mock_show):
        """Test publisher visualization with valid data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_books_by_publisher(self.publisher_data)
            mock_print.assert_called()
            mock_show.assert_called()
    
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.pause')
    def test_visualize_missing_isbn_valid_data(self, mock_pause, mock_show):
        """Test ISBN visualization with valid data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_missing_isbn(self.isbn_data, show_graph=True)
            mock_print.assert_called()
            mock_show.assert_called()
    
    def test_visualize_missing_isbn_no_graph(self):
        """Test ISBN visualization without graph"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_missing_isbn(self.isbn_data, show_graph=False)
            mock_print.assert_called()
    
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.pause')
    def test_visualize_books_per_year_by_language_valid_data(self, mock_pause, mock_show):
        """Test year-language visualization with valid data"""
        with patch('builtins.print') as mock_print:
            self.visualizer.visualize_books_per_year_by_language(self.year_lang_data)
            mock_print.assert_called()
            mock_show.assert_called()

def run_single_test():
    """Run this test file individually with detailed output"""
    print("=" * 70)
    print("               TESTING VISUALIZER CLASS")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVisualizer)
    
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