import unittest
import sys
from unittest.mock import patch, MagicMock
sys.path.append('..')
from cli import CLI

class TestCLI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.cli = CLI()
    
    def test_init(self):
        """Test CLI initialization"""
        self.assertIsNotNone(self.cli.main_app)
    
    def test_create_parser(self):
        """Test argument parser creation"""
        parser = self.cli.create_parser()
        self.assertIsNotNone(parser)
        
        # Test parsing valid arguments
        args = parser.parse_args(['--trends'])
        self.assertTrue(args.trends)
        
        args = parser.parse_args(['--file', 'test.csv', '--authors'])
        self.assertEqual(args.file, 'test.csv')
        self.assertTrue(args.authors)
    
    def test_load_dataset_success(self):
        """Test successful dataset loading"""
        mock_dataset = MagicMock()
        with patch.object(self.cli.main_app.data_loader, 'load', return_value=mock_dataset):
            result = self.cli.load_dataset('test.csv')
            self.assertEqual(result, mock_dataset)
    
    def test_load_dataset_failure(self):
        """Test failed dataset loading"""
        with patch.object(self.cli.main_app.data_loader, 'load', return_value=None):
            with patch('builtins.print') as mock_print:
                result = self.cli.load_dataset('nonexistent.csv')
                self.assertIsNone(result)
                mock_print.assert_any_call("Error: Failed to load dataset from 'nonexistent.csv'")
    
    @patch('cli.CLI.run_analysis')
    @patch('cli.CLI.load_dataset')
    @patch('sys.argv', ['cli.py', '--trends'])
    def test_run_single_analysis(self, mock_load, mock_run_analysis):
        """Test running single analysis"""
        mock_dataset = MagicMock()
        mock_load.return_value = mock_dataset
        
        self.cli.run()
        mock_run_analysis.assert_called_with('trends', mock_dataset)
    
    @patch('cli.CLI.run_analysis')
    @patch('cli.CLI.load_dataset')
    @patch('sys.argv', ['cli.py', '--trends', '--authors'])
    def test_run_multiple_analyses(self, mock_load, mock_run_analysis):
        """Test running multiple analyses"""
        mock_dataset = MagicMock()
        mock_load.return_value = mock_dataset
        
        self.cli.run()
        # Should call run_analysis for both trends and authors
        self.assertEqual(mock_run_analysis.call_count, 2)
    
    @patch.object(CLI, 'load_dataset')
    @patch('sys.argv', ['cli.py', '--menu'])
    def test_run_menu_mode(self, mock_load):
        """Test running in menu mode"""
        mock_dataset = MagicMock()
        mock_load.return_value = mock_dataset
        
        with patch.object(self.cli.main_app, 'show_menu') as mock_menu:
            self.cli.run()
            mock_menu.assert_called_once()
    
    @patch('cli.CLI.load_dataset')
    @patch('sys.argv', ['cli.py', '--trends'])
    @patch('sys.exit')
    def test_run_load_failure_exit(self, mock_exit, mock_load):
        """Test exit when dataset loading fails"""
        mock_load.return_value = None
        
        self.cli.run()
        mock_exit.assert_called_with(1)
    
    def test_run_analysis_trends(self):
        """Test running trends analysis"""
        mock_dataset = MagicMock()
        
        with patch.object(self.cli.main_app.analyzer, 'analyze_publication_trends') as mock_analyze:
            with patch.object(self.cli.main_app.visualizer, 'visualize_publication_trends') as mock_visualize:
                with patch('builtins.print') as mock_print:
                    mock_analyze.return_value = ({'test': 'data'}, None)
                    
                    self.cli.run_analysis('trends', mock_dataset)
                    
                    mock_analyze.assert_called_with(mock_dataset)
                    mock_visualize.assert_called_with({'test': 'data'})
                    mock_print.assert_any_call("   PUBLICATION TRENDS OVER TIME")
    
    def test_run_analysis_with_error(self):
        """Test running analysis with error"""
        mock_dataset = MagicMock()
        
        with patch.object(self.cli.main_app.analyzer, 'analyze_publication_trends') as mock_analyze:
            with patch('builtins.print') as mock_print:
                mock_analyze.return_value = (None, "Test error")
                
                self.cli.run_analysis('trends', mock_dataset)
                
                mock_print.assert_any_call("Error: Test error")
    
    def test_run_analysis_keyboard_interrupt(self):
        """Test analysis keyboard interrupt"""
        mock_dataset = MagicMock()
        
        with patch.object(self.cli.main_app.analyzer, 'analyze_publication_trends') as mock_analyze:
            with patch('builtins.print') as mock_print:
                mock_analyze.side_effect = KeyboardInterrupt()
                
                self.cli.run_analysis('trends', mock_dataset)
                
                mock_print.assert_any_call("\n\nAnalysis interrupted by user (Ctrl+C)")

def run_single_test():
    """Run this test file individually with detailed output"""
    print("=" * 70)
    print("                  TESTING CLI CLASS")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCLI)
    
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