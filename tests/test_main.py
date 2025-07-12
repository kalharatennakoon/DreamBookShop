import unittest
import pandas as pd
import sys
from unittest.mock import patch, MagicMock
sys.path.append('..')
from main import Main

class TestMain(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.main_app = Main()
        
        # Create mock dataset
        self.mock_dataset = pd.DataFrame({
            'title': ['Book 1', 'Book 2'],
            'authors': ['Author A', 'Author B'],
            'publication_date': [2020, 2021],
            'language_code': ['en', 'es'],
            'publisher': ['Publisher X', 'Publisher Y'],
            'isbn': ['123456789', '987654321']
        })
    
    def test_init(self):
        """Test Main class initialization"""
        self.assertIsNotNone(self.main_app.data_loader)
        self.assertIsNotNone(self.main_app.visualizer)
        self.assertIsNotNone(self.main_app.analyzer)
        self.assertIsNone(self.main_app.dataset)
    
    @patch('main.DataLoader.load')
    def test_run_successful_load(self, mock_load):
        """Test successful dataset loading"""
        mock_load.return_value = self.mock_dataset
        
        with patch.object(self.main_app, 'show_menu') as mock_menu:
            self.main_app.run("test_file.csv")
            mock_load.assert_called_with("test_file.csv")
            mock_menu.assert_called_once()
    
    @patch('main.DataLoader.load')
    @patch('builtins.print')
    def test_run_failed_load(self, mock_print, mock_load):
        """Test failed dataset loading"""
        mock_load.return_value = None
        
        self.main_app.run("nonexistent_file.csv")
        mock_print.assert_called_with("Failed to load dataset. Please check the file path and try again.")
    
    @patch('builtins.input', side_effect=['7'])
    @patch('builtins.print')
    def test_show_menu_exit(self, mock_print, mock_input):
        """Test menu exit option"""
        self.main_app.show_menu()
        mock_print.assert_any_call("\nThank you for using Dream Book Shop Analysis Tool!")
    
    @patch('builtins.input', side_effect=['8', '7'])
    @patch('builtins.print')
    def test_show_menu_invalid_choice(self, mock_print, mock_input):
        """Test menu with invalid choice"""
        self.main_app.show_menu()
        mock_print.assert_any_call("\nInvalid choice! Please enter a number between 1-7.")
    
    @patch('builtins.input', side_effect=KeyboardInterrupt())
    @patch('builtins.print')
    def test_show_menu_keyboard_interrupt(self, mock_print, mock_input):
        """Test menu keyboard interrupt handling"""
        self.main_app.show_menu()
        mock_print.assert_any_call("\n\nProcess interrupted by user (Ctrl+C)")
    
    def test_get_dataset(self):
        """Test get_dataset method"""
        self.main_app.dataset = self.mock_dataset
        result = self.main_app.get_dataset()
        self.assertTrue(result.equals(self.mock_dataset))
    
    @patch('builtins.print')
    def test_analyze_and_visualize_publication_trends(self, mock_print):
        """Test publication trends analysis and visualization"""
        self.main_app.dataset = self.mock_dataset
        
        # Mock the analyzer and visualizer methods
        with patch.object(self.main_app.analyzer, 'analyze_publication_trends') as mock_analyze, \
             patch.object(self.main_app.visualizer, 'visualize_publication_trends') as mock_visualize:
            
            mock_analyze.return_value = ({'test': 'data'}, None)
            
            self.main_app.analyze_and_visualize_publication_trends()
            mock_analyze.assert_called_with(self.mock_dataset)
            mock_visualize.assert_called_with({'test': 'data'})
    
    @patch('builtins.print')
    def test_analyze_and_visualize_publication_trends_with_error(self, mock_print):
        """Test publication trends analysis with error"""
        self.main_app.dataset = self.mock_dataset
        
        with patch.object(self.main_app.analyzer, 'analyze_publication_trends') as mock_analyze:
            mock_analyze.return_value = (None, "Test error")
            
            self.main_app.analyze_and_visualize_publication_trends()
            mock_print.assert_any_call("Error: Test error")
    
    def test_display_missing_isbn_data_none(self):
        """Test display ISBN data with None input"""
        with patch('builtins.print') as mock_print:
            self.main_app.display_missing_isbn_data(None)
            mock_print.assert_called_with("No ISBN data available for analysis.")
    
    def test_display_missing_isbn_data_empty(self):
        """Test display ISBN data with empty analysis"""
        analysis_data = {'isbn_analysis': {}}
        with patch('builtins.print') as mock_print:
            self.main_app.display_missing_isbn_data(analysis_data)
            mock_print.assert_called_with("No ISBN data available for analysis.")
    
    def test_display_missing_isbn_data_valid(self):
        """Test display ISBN data with valid analysis"""
        analysis_data = {
            'isbn_analysis': {
                'isbn': {
                    'total_records': 100,
                    'present_count': 95,
                    'missing_count': 5,
                    'missing_percentage': 5.0
                }
            }
        }
        
        with patch('builtins.print') as mock_print:
            self.main_app.display_missing_isbn_data(analysis_data)
            mock_print.assert_called()

def run_single_test():
    """Run this test file individually with detailed output"""
    print("=" * 70)
    print("                  TESTING MAIN CLASS")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
    
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
        if result.errors:
            print(f"\nErrors ({len(result.errors)}):")
            for test, traceback in result.errors:
                print(f"  - {test}")
    
    print("=" * 50)
    return result.wasSuccessful()

if __name__ == '__main__':
    run_single_test()