import argparse
import sys
from main import Main

class CLI:
    def __init__(self):
        """Initialize CLI class"""
        self.main_app = Main()
        
    def create_parser(self):
        """Create and configure argument parser"""
        parser = argparse.ArgumentParser(
            description='Dream Book Shop Analysis Tool - Command Line Interface',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Examples:
  python cli.py --menu                           # Show interactive menu
  python cli.py --trends                         # Show publication trends
  python cli.py --authors                        # Show top authors
  python cli.py --languages                      # Show language distribution
  python cli.py --publishers                     # Show top publishers
  python cli.py --isbn                          # Show ISBN analysis
  python cli.py --year-language                 # Show books per year by language
  python cli.py --file custom_dataset.csv       # Use custom dataset file
            '''
        )
        
        # File input option
        parser.add_argument(
            '--file', '-f',
            type=str,
            default='Dataset_Books.csv',
            help='Path to the dataset CSV file (default: Dataset_Books.csv)'
        )
        
        # Analysis options
        parser.add_argument(
            '--menu', '-m',
            action='store_true',
            help='Show interactive menu (default behavior)'
        )
        
        parser.add_argument(
            '--trends', '-t',
            action='store_true',
            help='Show publication trends over time'
        )
        
        parser.add_argument(
            '--authors', '-a',
            action='store_true',
            help='Show top 5 most prolific authors'
        )
        
        parser.add_argument(
            '--languages', '-l',
            action='store_true',
            help='Show language distribution of books'
        )
        
        parser.add_argument(
            '--publishers', '-p',
            action='store_true',
            help='Show top publishers by number of books'
        )
        
        parser.add_argument(
            '--isbn', '-i',
            action='store_true',
            help='Show missing ISBN analysis'
        )
        
        parser.add_argument(
            '--year-language', '-yl',
            action='store_true',
            help='Show books per year categorized by language (first 1000 records only)'
        )
        
        # Output options
        parser.add_argument(
            '--no-graph', '-ng',
            action='store_true',
            help='Disable graph display (terminal output only)'
        )
        
        parser.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='Enable verbose output'
        )
        
        return parser
    
    def load_dataset(self, file_path):
        """Load dataset and handle errors"""
        try:
            dataset = self.main_app.data_loader.load(file_path)
            if dataset is not None:
                if hasattr(self, 'verbose') and self.verbose:
                    print(f"Successfully loaded dataset from '{file_path}'")
                return dataset
            else:
                print(f"Error: Failed to load dataset from '{file_path}'")
                return None
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return None
    
    def run_analysis(self, analysis_type, dataset):
        """Run specific analysis based on type"""
        try:
            if analysis_type == 'trends':
                print("\n" + "="*50)
                print("   PUBLICATION TRENDS OVER TIME")
                print("="*50)
                analysis_data, error = self.main_app.analyzer.analyze_publication_trends(dataset)
                if error:
                    print(f"Error: {error}")
                else:
                    self.main_app.visualizer.visualize_publication_trends(analysis_data)
                    
            elif analysis_type == 'authors':
                print("\n" + "="*50)
                print("   TOP 5 MOST PROLIFIC AUTHORS")
                print("="*50)
                analysis_data, error = self.main_app.analyzer.analyze_top_authors(dataset)
                if error:
                    print(f"Error: {error}")
                else:
                    self.main_app.visualizer.visualize_top_authors(analysis_data)
                    
            elif analysis_type == 'languages':
                print("\n" + "="*50)
                print("   LANGUAGE DISTRIBUTION")
                print("="*50)
                analysis_data, error = self.main_app.analyzer.analyze_language_distribution(dataset)
                if error:
                    print(f"Error: {error}")
                else:
                    self.main_app.visualizer.visualize_language_distribution(analysis_data)
                    
            elif analysis_type == 'publishers':
                print("\n" + "="*50)
                print("   BOOKS BY PUBLISHER")
                print("="*50)
                analysis_data, error = self.main_app.analyzer.analyze_books_by_publisher(dataset)
                if error:
                    print(f"Error: {error}")
                else:
                    self.main_app.visualizer.visualize_books_by_publisher(analysis_data)
                    
            elif analysis_type == 'isbn':
                print("\n" + "="*50)
                print("   MISSING ISBN ANALYSIS")
                print("="*50)
                analysis_data, error = self.main_app.analyzer.analyze_missing_isbn(dataset)
                if error:
                    print(f"Error: {error}")
                else:
                    self.main_app.display_missing_isbn_data(analysis_data)
                    
            elif analysis_type == 'year-language':
                print("\n" + "="*50)
                print("   BOOKS PER YEAR BY LANGUAGE (FIRST 1000 RECORDS)")
                print("="*50)
                analysis_data, error = self.main_app.analyzer.analyze_books_per_year_by_language(dataset)
                if error:
                    print(f"Error: {error}")
                else:
                    self.main_app.visualizer.visualize_books_per_year_by_language(analysis_data)
                    
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
        except Exception as e:
            print(f"Error during analysis: {e}")
    
    def run(self):
        """Main CLI execution method"""
        parser = self.create_parser()
        args = parser.parse_args()
        
        # Store verbose flag
        self.verbose = args.verbose
        
        # Load dataset
        dataset = self.load_dataset(args.file)
        if dataset is None:
            sys.exit(1)
        
        self.main_app.dataset = dataset
        
        # Determine which analysis to run
        analysis_flags = [
            ('trends', args.trends),
            ('authors', args.authors),
            ('languages', args.languages),
            ('publishers', args.publishers),
            ('isbn', args.isbn),
            ('year-language', args.year_language)
        ]
        
        # Count how many analysis flags are set
        active_analyses = [flag for flag, is_set in analysis_flags if is_set]
        
        if len(active_analyses) == 0 or args.menu:
            # No specific analysis requested or menu explicitly requested
            if self.verbose:
                print("Starting interactive menu mode...")
            self.main_app.show_menu()
        elif len(active_analyses) == 1:
            # Single analysis requested
            analysis_type = active_analyses[0]
            self.run_analysis(analysis_type, dataset)
        else:
            # Multiple analyses requested - run them in sequence
            if self.verbose:
                print(f"Running {len(active_analyses)} analyses in sequence...")
            
            for analysis_type in active_analyses:
                self.run_analysis(analysis_type, dataset)
                if len(active_analyses) > 1:  # Add separator between analyses
                    print("\n" + "-"*60 + "\n")

def main():
    """Entry point for CLI"""
    try:
        cli = CLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user (Ctrl+C)")
        print("Thank you for using Dream Book Shop Analysis Tool!")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()