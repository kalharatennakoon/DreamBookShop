from dataLoader import DataLoader
from visualizer import Visualizer
from analyzer import Analyzer
import pandas as pd
import signal
import sys

class Main:
    def __init__(self):
        """Initialize Main class with DataLoader, Analyzer, and Visualizer instances"""
        self.data_loader = DataLoader()
        self.visualizer = Visualizer()
        self.analyzer = Analyzer()
        self.dataset = None
        
        # Set up signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Handle Ctrl+C signal gracefully"""
        print("\n\nProcess interrupted by user (Ctrl+C)")
        print("Thank you for using Dream Book Shop Analysis Tool!")
        sys.exit(0)
    
    def run(self, file_path="Dataset_Books.csv"):
        try:
            # Load the dataset using DataLoader
            self.dataset = self.data_loader.load(file_path)
            
            if self.dataset is not None:
                # Show menu and handle user selections
                self.show_menu()
            else:
                print("Failed to load dataset. Please check the file path and try again.")
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user (Ctrl+C)")
            print("Thank you for using Dream Book Shop Analysis Tool!")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Exiting application...")
            sys.exit(1)
    
    def show_menu(self):
        """Display the analysis menu and handle user selections"""
        try:
            while True:
                print("\n" + "="*60)
                print("           DREAM BOOK SHOP - ANALYSIS MENU")
                print("="*60)
                print("1. Show publication trends over time")
                print("2. Show top 5 most prolific authors")
                print("3. Show language distribution of books")
                print("4. Show number of books published by each publisher")
                print("5. Show missing ISBN analysis")
                print("6. Show books published per year categorized by language (first 1000 records)")
                print("7. Exit")
                print("="*60)
                
                try:
                    choice = input("\nEnter your choice (1-7): ").strip()
                    
                    if choice == '1':
                        self.analyze_and_visualize_publication_trends()
                    elif choice == '2':
                        self.analyze_and_visualize_top_authors()
                    elif choice == '3':
                        self.analyze_and_visualize_language_distribution()
                    elif choice == '4':
                        self.analyze_and_visualize_books_by_publisher()
                    elif choice == '5':
                        self.analyze_and_visualize_missing_isbn()
                    elif choice == '6':
                        self.analyze_and_visualize_books_per_year_by_language()
                    elif choice == '7':
                        print("\nThank you for using Dream Book Shop Analysis Tool!")
                        break
                    else:
                        print("\nInvalid choice! Please enter a number between 1-7.")
                        
                    if choice in ['1', '2', '3', '4', '5', '6']:
                        try:
                            input("\nPress Enter to continue...")
                        except KeyboardInterrupt:
                            print("\n\nProcess interrupted by user (Ctrl+C)")
                            print("Thank you for using Dream Book Shop Analysis Tool!")
                            break
                        
                except KeyboardInterrupt:
                    print("\n\nProcess interrupted by user (Ctrl+C)")
                    print("Thank you for using Dream Book Shop Analysis Tool!")
                    break
                except Exception as e:
                    print(f"\nAn error occurred: {e}")
                    try:
                        input("Press Enter to continue...")
                    except KeyboardInterrupt:
                        print("\n\nProcess interrupted by user (Ctrl+C)")
                        print("Thank you for using Dream Book Shop Analysis Tool!")
                        break
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user (Ctrl+C)")
            print("Thank you for using Dream Book Shop Analysis Tool!")

    def analyze_and_visualize_publication_trends(self):
        """Analyze and visualize publication trends over time"""
        try:
            print("\n" + "="*50)
            print("   PUBLICATION TRENDS OVER TIME")
            print("="*50)
            
            analysis_data, error = self.analyzer.analyze_publication_trends(self.dataset)
            
            if error:
                print(f"Error: {error}")
            else:
                self.visualizer.visualize_publication_trends(analysis_data)
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
            return
        except Exception as e:
            print(f"Error during publication trends analysis: {e}")

    def analyze_and_visualize_top_authors(self):
        """Analyze and visualize top prolific authors"""
        try:
            print("\n" + "="*50)
            print("   TOP 5 MOST PROLIFIC AUTHORS")
            print("="*50)
            
            analysis_data, error = self.analyzer.analyze_top_authors(self.dataset)
            
            if error:
                print(f"Error: {error}")
            else:
                self.visualizer.visualize_top_authors(analysis_data)
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
            return
        except Exception as e:
            print(f"Error during top authors analysis: {e}")

    def analyze_and_visualize_language_distribution(self):
        """Analyze and visualize language distribution"""
        try:
            print("\n" + "="*50)
            print("   LANGUAGE DISTRIBUTION")
            print("="*50)
            
            analysis_data, error = self.analyzer.analyze_language_distribution(self.dataset)
            
            if error:
                print(f"Error: {error}")
            else:
                self.visualizer.visualize_language_distribution(analysis_data)
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
            return
        except Exception as e:
            print(f"Error during language distribution analysis: {e}")

    def analyze_and_visualize_books_by_publisher(self):
        """Analyze and visualize books by publisher"""
        try:
            print("\n" + "="*50)
            print("   BOOKS BY PUBLISHER")
            print("="*50)
            
            analysis_data, error = self.analyzer.analyze_books_by_publisher(self.dataset)
            
            if error:
                print(f"Error: {error}")
            else:
                self.visualizer.visualize_books_by_publisher(analysis_data)
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
            return
        except Exception as e:
            print(f"Error during books by publisher analysis: {e}")

    def analyze_and_visualize_missing_isbn(self):
        """Analyze missing ISBN data and display only in terminal"""
        try:
            print("\n" + "="*50)
            print("   MISSING ISBN ANALYSIS")
            print("="*50)
            
            analysis_data, error = self.analyzer.analyze_missing_isbn(self.dataset)
            
            if error:
                print(f"Error: {error}")
            else:
                # Only display data in terminal, no visualization
                self.display_missing_isbn_data(analysis_data)
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
            return
        except Exception as e:
            print(f"Error during missing ISBN analysis: {e}")

    def display_missing_isbn_data(self, analysis_data):
        """Display missing ISBN analysis data in terminal only"""
        if analysis_data is None:
            print("No ISBN data available for analysis.")
            return
        
        isbn_analysis = analysis_data['isbn_analysis']
        
        if not isbn_analysis:
            print("No ISBN data available for analysis.")
            return
        
        # Print detailed summary (removed duplicate title and extra line)
        isbn_cols = list(isbn_analysis.keys())
        for isbn_col in isbn_cols:
            data = isbn_analysis[isbn_col]
            print(f"\n{isbn_col.upper()} Analysis:")
            print("-" * 40)
            print(f"   Total records: {data['total_records']:,}")
            print(f"   Present: {data['present_count']:,}")
            print(f"   Missing: {data['missing_count']:,}")
            print(f"   Missing percentage: {data['missing_percentage']:.2f}%")
            print(f"   Completeness: {100 - data['missing_percentage']:.2f}%")
        
        # Summary table
        print(f"\nISBN Data Summary Table:")
        print("=" * 60)
        print(f"{'ISBN Type':<15} {'Total':<10} {'Present':<10} {'Missing':<10} {'Missing %':<12}")
        print("-" * 60)
        
        for isbn_col in isbn_cols:
            data = isbn_analysis[isbn_col]
            print(f"{isbn_col.upper():<15} {data['total_records']:<10,} {data['present_count']:<10,} {data['missing_count']:<10,} {data['missing_percentage']:<12.2f}%")
        
        # Overall assessment
        print(f"\nData Quality Assessment:")
        print("-" * 40)
        for isbn_col in isbn_cols:
            data = isbn_analysis[isbn_col]
            completeness = 100 - data['missing_percentage']
            if completeness >= 90:
                status = "Excellent"
            elif completeness >= 75:
                status = "Good"
            elif completeness >= 50:
                status = "Fair"
            else:
                status = "Poor"
            print(f"   {isbn_col.upper()}: {status} ({completeness:.1f}% complete)")

    def analyze_and_visualize_books_per_year_by_language(self):
        """Analyze and visualize books per year by language"""
        try:
            print("\n" + "="*50)
            print("   BOOKS PER YEAR BY LANGUAGE (FIRST 1000 RECORDS)")
            print("="*50)
            
            analysis_data, error = self.analyzer.analyze_books_per_year_by_language(self.dataset)
            
            if error:
                print(f"Error: {error}")
            else:
                self.visualizer.visualize_books_per_year_by_language(analysis_data)
        except KeyboardInterrupt:
            print("\n\nAnalysis interrupted by user (Ctrl+C)")
            return
        except Exception as e:
            print(f"Error during books per year by language analysis: {e}")

    def get_dataset(self):
        return self.dataset

# Entry point for running the application
if __name__ == "__main__":
    try:
        # Create Main instance and run the application
        app = Main()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user (Ctrl+C)")
        print("Thank you for using Dream Book Shop Analysis Tool!")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
