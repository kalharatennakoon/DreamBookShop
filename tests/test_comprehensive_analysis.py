import unittest
import pandas as pd
import sys
import os

# Add parent directory to path so we can import our modules
sys.path.append('..')

from analyzer import Analyzer

class TestComprehensiveAnalysis(unittest.TestCase):
    def setUp(self):
        self.analyzer = Analyzer()

        self.test_data = pd.DataFrame({
            'publication_date': [2001, 2001, 2002, 2003, 2003, 2003, 2004, 2005],
            'authors': ['Author A', 'Author B', 'Author A', 'Author C', 'Author A', 'Author B', 'Author A', 'Author D'],
            'language_code': ['en', 'en', 'es', 'en', 'fr', 'es', 'en', 'fr'],
            'publisher': ['Publisher X', 'Publisher Y', 'Publisher X', 'Publisher Z', 'Publisher X', 'Publisher Y', 'Publisher X', 'Publisher Z'],
            'isbn13': ['978-1234567890', '', '978-0987654321', '978-1111111111', None, '978-2222222222', '978-3333333333', ''],
            'isbn10': ['1234567890', '0987654321', '', None, '1111111111', '', '3333333333', '4444444444']
        })
    
    def test_T001_publication_trends_correct_count(self):
        print("\n" + "="*50)
        print("T001: PUBLICATION TRENDS ANALYSIS")
        print("="*50)
        print("Input Data: Publication years from test dataset")
        print("Years in dataset:", list(self.test_data['publication_date']))
        
        analysis_data, error = self.analyzer.analyze_publication_trends(self.test_data)
        
        # Verify no error occurred
        self.assertIsNone(error, f"Analysis failed with error: {error}")
        self.assertIsNotNone(analysis_data, "Analysis data should not be None")
        
        # Show actual results
        year_counts = analysis_data['year_counts']
        print("\nActual Results:")
        print("Year Counts:", dict(year_counts))
        print("Total Years:", analysis_data['total_years'])
        print("Most Productive Year:", analysis_data['most_productive_year'], f"({analysis_data['most_productive_count']} books)")
        print("Least Productive Year:", analysis_data['least_productive_year'], f"({analysis_data['least_productive_count']} books)")
        
        # Verify the year counts are correct
        expected_counts = {2001: 2, 2002: 1, 2003: 3, 2004: 1, 2005: 1}
        print("\nExpected vs Actual Comparison:")
        for year, expected_count in expected_counts.items():
            actual_count = year_counts.get(year, 0)
            status = "✅" if actual_count == expected_count else "❌"
            print(f"  Year {year}: Expected {expected_count}, Got {actual_count} {status}")
            self.assertEqual(actual_count, expected_count, 
                           f"Year {year}: expected {expected_count} books, got {actual_count}")
        
        # Verify total years and most/least productive years
        self.assertEqual(analysis_data['total_years'], 5, "Should have 5 different years")
        self.assertEqual(analysis_data['most_productive_year'], 2003, "2003 should be most productive year")
        self.assertEqual(analysis_data['most_productive_count'], 3, "Most productive year should have 3 books")
        
        print("\n✅ All validations passed!")
        print("="*50)
    
    def test_T002_top_authors_identification(self):
        print("\n" + "="*50)
        print("T002: TOP AUTHORS ANALYSIS")
        print("="*50)
        print("Input Data: Authors from test dataset")
        print("Authors in dataset:", list(self.test_data['authors']))
        
        analysis_data, error = self.analyzer.analyze_top_authors(self.test_data, top_n=5)
        
        # Verify no error occurred
        self.assertIsNone(error, f"Analysis failed with error: {error}")
        self.assertIsNotNone(analysis_data, "Analysis data should not be None")
        
        # Show actual results
        author_counts = analysis_data['author_counts']
        print("\nActual Results:")
        print("Author Rankings:")
        for i, (author, count) in enumerate(author_counts.items(), 1):
            print(f"  {i}. {author}: {count} books")
        
        expected_authors = {
            'Author A': 4,  # Most prolific
            'Author B': 2,  # Second most prolific
            'Author C': 1,  # Tied for third
            'Author D': 1   # Tied for third
        }
        
        print("\nExpected vs Actual Comparison:")
        for author, expected_count in expected_authors.items():
            actual_count = author_counts.get(author, 0)
            status = "✅" if actual_count == expected_count else "❌"
            print(f"  {author}: Expected {expected_count}, Got {actual_count} {status}")
        
        # Check that Author A is the top author
        self.assertEqual(author_counts.iloc[0], 4, "Author A should have 4 books")
        self.assertEqual(author_counts.index[0], 'Author A', "Author A should be ranked first")
        
        # Check that Author B is second
        self.assertEqual(author_counts.iloc[1], 2, "Author B should have 2 books")
        self.assertEqual(author_counts.index[1], 'Author B', "Author B should be ranked second")
        
        # Verify all expected authors are present
        for author, expected_count in expected_authors.items():
            self.assertIn(author, author_counts.index, f"Author {author} should be in results")
            actual_count = author_counts[author]
            self.assertEqual(actual_count, expected_count, 
                           f"Author {author}: expected {expected_count} books, got {actual_count}")
        
        print("\n✅ All validations passed!")
        print("="*50)
    
    def test_T003_language_distribution_counts(self):
        print("\n" + "="*50)
        print("T003: LANGUAGE DISTRIBUTION ANALYSIS")
        print("="*50)
        print("Input Data: Languages from test dataset")
        print("Languages in dataset:", list(self.test_data['language_code']))
        
        analysis_data, error = self.analyzer.analyze_language_distribution(self.test_data)
        
        # Verify no error occurred
        self.assertIsNone(error, f"Analysis failed with error: {error}")
        self.assertIsNotNone(analysis_data, "Analysis data should not be None")
        
        # Show actual results
        lang_counts = analysis_data['lang_counts']
        lang_percentages = analysis_data['lang_percentages']
        print(f"\nActual Results (Total books: {analysis_data['total_books']}):")
        print("Language Distribution:")
        for lang, count in lang_counts.items():
            percentage = lang_percentages[lang]
            print(f"  {lang}: {count} books ({percentage}%)")
        
        expected_counts = {'en': 4, 'es': 2, 'fr': 2}
        expected_percentages = {'en': 50.0, 'es': 25.0, 'fr': 25.0}
        
        print("\nExpected vs Actual Comparison:")
        print("Counts:")
        for lang, expected_count in expected_counts.items():
            actual_count = lang_counts.get(lang, 0)
            status = "✅" if actual_count == expected_count else "❌"
            print(f"  {lang}: Expected {expected_count}, Got {actual_count} {status}")
            self.assertEqual(actual_count, expected_count, 
                           f"Language {lang}: expected {expected_count} books, got {actual_count}")
        
        print("Percentages:")
        for lang, expected_percentage in expected_percentages.items():
            actual_percentage = lang_percentages.get(lang, 0)
            status = "✅" if actual_percentage == expected_percentage else "❌"
            print(f"  {lang}: Expected {expected_percentage}%, Got {actual_percentage}% {status}")
            self.assertEqual(actual_percentage, expected_percentage, 
                           f"Language {lang}: expected {expected_percentage}%, got {actual_percentage}%")
        
        # Verify total books count
        self.assertEqual(analysis_data['total_books'], 8, "Should have 8 total books")
        
        print("\n✅ All validations passed!")
        print("="*50)
    
    def test_T004_publisher_book_counts(self):
        print("\n" + "="*50)
        print("T004: PUBLISHER ANALYSIS")
        print("="*50)
        print("Input Data: Publishers from test dataset")
        print("Publishers in dataset:", list(self.test_data['publisher']))
        
        analysis_data, error = self.analyzer.analyze_books_by_publisher(self.test_data, top_n=10)
        
        # Verify no error occurred
        self.assertIsNone(error, f"Analysis failed with error: {error}")
        self.assertIsNotNone(analysis_data, "Analysis data should not be None")
        
        # Show actual results
        publisher_counts = analysis_data['publisher_counts']
        print(f"\nActual Results (Total publishers: {analysis_data['total_publishers']}):")
        print("Publisher Rankings:")
        for i, (publisher, count) in enumerate(publisher_counts.items(), 1):
            print(f"  {i}. {publisher}: {count} books")
        
        expected_counts = {'Publisher X': 4, 'Publisher Y': 2, 'Publisher Z': 2}
        
        print("\nExpected vs Actual Comparison:")
        for publisher, expected_count in expected_counts.items():
            actual_count = publisher_counts.get(publisher, 0)
            status = "✅" if actual_count == expected_count else "❌"
            print(f"  {publisher}: Expected {expected_count}, Got {actual_count} {status}")
            self.assertEqual(actual_count, expected_count, 
                           f"Publisher {publisher}: expected {expected_count} books, got {actual_count}")
        
        # Verify Publisher X is the top publisher
        self.assertEqual(publisher_counts.iloc[0], 4, "Publisher X should have 4 books")
        self.assertEqual(publisher_counts.index[0], 'Publisher X', "Publisher X should be ranked first")
        
        # Verify total publishers count
        self.assertEqual(analysis_data['total_publishers'], 3, "Should have 3 total publishers")
        
        print("\n✅ All validations passed!")
        print("="*50)
    
    def test_T005_missing_isbn_detection(self):
        print("\n" + "="*50)
        print("T005: MISSING ISBN ANALYSIS")
        print("="*50)
        print("Input Data: ISBN fields from test dataset")
        print("ISBN13 values:", list(self.test_data['isbn13']))
        print("ISBN10 values:", list(self.test_data['isbn10']))
        
        analysis_data, error = self.analyzer.analyze_missing_isbn(self.test_data)
        
        # Verify no error occurred
        self.assertIsNone(error, f"Analysis failed with error: {error}")
        self.assertIsNotNone(analysis_data, "Analysis data should not be None")
        
        isbn_analysis = analysis_data['isbn_analysis']
        
        print(f"\nActual Results (Total records: {analysis_data['total_records']}):")
        
        # Show ISBN13 results
        isbn13_data = isbn_analysis['isbn13']
        print("ISBN13 Analysis:")
        print(f"  Total records: {isbn13_data['total_records']}")
        print(f"  Present: {isbn13_data['present_count']}")
        print(f"  Missing: {isbn13_data['missing_count']}")
        print(f"  Missing percentage: {isbn13_data['missing_percentage']:.1f}%")
        
        # Show ISBN10 results
        isbn10_data = isbn_analysis['isbn10']
        print("ISBN10 Analysis:")
        print(f"  Total records: {isbn10_data['total_records']}")
        print(f"  Present: {isbn10_data['present_count']}")
        print(f"  Missing: {isbn10_data['missing_count']}")
        print(f"  Missing percentage: {isbn10_data['missing_percentage']:.1f}%")
        
        print("\nExpected vs Actual Comparison:")
        
        print("ISBN13:")
        expected_missing_13 = 3
        expected_present_13 = 5
        actual_missing_13 = isbn13_data['missing_count']
        actual_present_13 = isbn13_data['present_count']
        
        print(f"  Missing: Expected {expected_missing_13}, Got {actual_missing_13} {'✅' if actual_missing_13 == expected_missing_13 else '❌'}")
        print(f"  Present: Expected {expected_present_13}, Got {actual_present_13} {'✅' if actual_present_13 == expected_present_13 else '❌'}")
        
        self.assertEqual(isbn13_data['total_records'], 8, "Should have 8 total records")
        self.assertEqual(isbn13_data['missing_count'], 3, "Should have 3 missing ISBN13 values")
        self.assertEqual(isbn13_data['present_count'], 5, "Should have 5 present ISBN13 values")
        self.assertEqual(isbn13_data['missing_percentage'], 37.5, "Should have 37.5% missing ISBN13")
        
        print("ISBN10:")
        expected_missing_10 = 3
        expected_present_10 = 5
        actual_missing_10 = isbn10_data['missing_count']
        actual_present_10 = isbn10_data['present_count']
        
        print(f"  Missing: Expected {expected_missing_10}, Got {actual_missing_10} {'✅' if actual_missing_10 == expected_missing_10 else '❌'}")
        print(f"  Present: Expected {expected_present_10}, Got {actual_present_10} {'✅' if actual_present_10 == expected_present_10 else '❌'}")
        
        self.assertEqual(isbn10_data['total_records'], 8, "Should have 8 total records")
        self.assertEqual(isbn10_data['missing_count'], 3, "Should have 3 missing ISBN10 values")
        self.assertEqual(isbn10_data['present_count'], 5, "Should have 5 present ISBN10 values")
        self.assertEqual(isbn10_data['missing_percentage'], 37.5, "Should have 37.5% missing ISBN10")
        
        print("\n✅ All validations passed!")
        print("="*50)
    
    def test_T006_books_per_year_by_language_grouping(self):
        print("\n" + "="*50)
        print("T006: YEAR-LANGUAGE GROUPING ANALYSIS")
        print("="*50)
        print("Input Data: Year-Language combinations from test dataset")
        print("Years:", list(self.test_data['publication_date']))
        print("Languages:", list(self.test_data['language_code']))
        print("Combined pairs:", list(zip(self.test_data['publication_date'], self.test_data['language_code'])))
        
        analysis_data, error = self.analyzer.analyze_books_per_year_by_language(self.test_data)
        
        # Verify no error occurred
        self.assertIsNone(error, f"Analysis failed with error: {error}")
        self.assertIsNotNone(analysis_data, "Analysis data should not be None")
        
        year_lang_counts = analysis_data['year_lang_counts']
        
        # Show actual results
        print("\nActual Results:")
        print("Years identified:", analysis_data['years'])
        print("Languages identified:", analysis_data['languages'])
        print("\nYear-Language Matrix:")
        print(year_lang_counts)
        
        print("\nDetailed breakdown:")
        for year in analysis_data['years']:
            print(f"  {int(year)}:")
            for lang in analysis_data['languages']:
                count = year_lang_counts.loc[year, lang]
                if count > 0:
                    print(f"    {lang}: {count} books")
        
        # Verify the data structure
        self.assertFalse(year_lang_counts.empty, "Year-language counts should not be empty")
        
        # Verify years are correctly identified
        expected_years = [2001, 2002, 2003, 2004, 2005]
        actual_years = sorted(analysis_data['years'])
        print(f"\nExpected years: {expected_years}")
        print(f"Actual years: {actual_years}")
        print(f"Years match: {'✅' if actual_years == expected_years else '❌'}")
        self.assertEqual(actual_years, expected_years, "Should have correct years")
        
        # Verify languages are correctly identified
        expected_languages = ['en', 'es', 'fr']
        actual_languages = sorted(analysis_data['languages'])
        print(f"Expected languages: {expected_languages}")
        print(f"Actual languages: {actual_languages}")
        print(f"Languages match: {'✅' if actual_languages == expected_languages else '❌'}")
        self.assertEqual(actual_languages, expected_languages, "Should have correct languages")
        
        # Verify specific year-language combinations
        # Test data breakdown:
        # 2001: en (2 books), 2002: es (1 book), 2003: en (1 book), es (1 book), fr (1 book)
        # 2004: en (1 book), 2005: fr (1 book)
        
        print("\nExpected vs Actual Combination Checks:")
        
        # Check 2001 - should have 2 English books
        expected_2001_en = 2
        actual_2001_en = year_lang_counts.loc[2001, 'en']
        print(f"2001 English: Expected {expected_2001_en}, Got {actual_2001_en} {'✅' if actual_2001_en == expected_2001_en else '❌'}")
        self.assertEqual(year_lang_counts.loc[2001, 'en'], 2, "2001 should have 2 English books")
        
        expected_2001_es = 0
        actual_2001_es = year_lang_counts.loc[2001, 'es']
        print(f"2001 Spanish: Expected {expected_2001_es}, Got {actual_2001_es} {'✅' if actual_2001_es == expected_2001_es else '❌'}")
        self.assertEqual(year_lang_counts.loc[2001, 'es'], 0, "2001 should have 0 Spanish books")
        
        expected_2001_fr = 0
        actual_2001_fr = year_lang_counts.loc[2001, 'fr']
        print(f"2001 French: Expected {expected_2001_fr}, Got {actual_2001_fr} {'✅' if actual_2001_fr == expected_2001_fr else '❌'}")
        self.assertEqual(year_lang_counts.loc[2001, 'fr'], 0, "2001 should have 0 French books")
        
        # Check 2003 - should have 1 book in each language
        expected_2003_en = 1
        actual_2003_en = year_lang_counts.loc[2003, 'en']
        print(f"2003 English: Expected {expected_2003_en}, Got {actual_2003_en} {'✅' if actual_2003_en == expected_2003_en else '❌'}")
        self.assertEqual(year_lang_counts.loc[2003, 'en'], 1, "2003 should have 1 English book")
        
        expected_2003_es = 1
        actual_2003_es = year_lang_counts.loc[2003, 'es']
        print(f"2003 Spanish: Expected {expected_2003_es}, Got {actual_2003_es} {'✅' if actual_2003_es == expected_2003_es else '❌'}")
        self.assertEqual(year_lang_counts.loc[2003, 'es'], 1, "2003 should have 1 Spanish book")
        
        expected_2003_fr = 1
        actual_2003_fr = year_lang_counts.loc[2003, 'fr']
        print(f"2003 French: Expected {expected_2003_fr}, Got {actual_2003_fr} {'✅' if actual_2003_fr == expected_2003_fr else '❌'}")
        self.assertEqual(year_lang_counts.loc[2003, 'fr'], 1, "2003 should have 1 French book")
        
        print("\n✅ All validations passed!")
        print("Note: This analysis uses only the first 1000 records (as required)")
        print("="*50)


if __name__ == '__main__':
    import argparse
    
    # Add command-line argument parsing for individual test execution
    parser = argparse.ArgumentParser(
        description='Run Dream Book Shop comprehensive tests',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python test_comprehensive_analysis.py                           # Run all tests
  python test_comprehensive_analysis.py -v                        # Run all tests verbose
  python test_comprehensive_analysis.py --test T001               # Run T001 only
  python test_comprehensive_analysis.py --test publication        # Run publication test
  python test_comprehensive_analysis.py --method test_T001_publication_trends_correct_count

Available Tests:
  T001 - Publication trends analysis
  T002 - Top authors identification  
  T003 - Language distribution
  T004 - Publisher analysis
  T005 - Missing ISBN detection
  T006 - Books per year by language
        '''
    )
    
    parser.add_argument(
        '--test', '-t',
        type=str,
        help='Run specific test by ID (T001-T006) or keyword'
    )
    
    parser.add_argument(
        '--method', '-m',
        type=str,
        help='Run specific test method by exact name'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Test mapping for easy access
    TEST_MAPPING = {
        'T001': 'test_T001_publication_trends_correct_count',
        'T002': 'test_T002_top_authors_identification',
        'T003': 'test_T003_language_distribution_counts',
        'T004': 'test_T004_publisher_book_counts',
        'T005': 'test_T005_missing_isbn_detection',
        'T006': 'test_T006_books_per_year_by_language_grouping',
        'publication': 'test_T001_publication_trends_correct_count',
        'trends': 'test_T001_publication_trends_correct_count',
        'author': 'test_T002_top_authors_identification',
        'authors': 'test_T002_top_authors_identification',
        'language': 'test_T003_language_distribution_counts',
        'languages': 'test_T003_language_distribution_counts',
        'publisher': 'test_T004_publisher_book_counts',
        'publishers': 'test_T004_publisher_book_counts',
        'isbn': 'test_T005_missing_isbn_detection',
        'year-language': 'test_T006_books_per_year_by_language_grouping',
        'grouping': 'test_T006_books_per_year_by_language_grouping'
    }
    
    if args.test:
        # Run specific test by ID or keyword
        test_key = args.test.upper() if args.test.startswith('T') else args.test.lower()
        if test_key in TEST_MAPPING:
            test_method = TEST_MAPPING[test_key]
            suite = unittest.TestSuite()
            suite.addTest(TestComprehensiveAnalysis(test_method))
            
            verbosity = 2 if args.verbose else 1
            runner = unittest.TextTestRunner(verbosity=verbosity, descriptions=True)
            result = runner.run(suite)
            
            print(f"\n{'='*50}")
            if result.wasSuccessful():
                print(f"✅ Test {args.test.upper()} PASSED!")
            else:
                print(f"❌ Test {args.test.upper()} FAILED!")
            print(f"{'='*50}")
        else:
            print(f"Error: Test '{args.test}' not found!")
            print("Available tests:", ', '.join(TEST_MAPPING.keys()))
    
    elif args.method:
        # Run specific test method by exact name
        if hasattr(TestComprehensiveAnalysis, args.method):
            suite = unittest.TestSuite()
            suite.addTest(TestComprehensiveAnalysis(args.method))
            
            verbosity = 2 if args.verbose else 1
            runner = unittest.TextTestRunner(verbosity=verbosity, descriptions=True)
            result = runner.run(suite)
        else:
            print(f"Error: Method '{args.method}' not found!")
            print("Available methods:")
            for method in dir(TestComprehensiveAnalysis):
                if method.startswith('test_'):
                    print(f"  {method}")
    
    else:
        # Run all tests
        verbosity = 2 if args.verbose else 1
        unittest.main(verbosity=verbosity, argv=[''])
