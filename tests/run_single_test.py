#!/usr/bin/env python3
"""
Individual Test Runner - Dream Book Shop Analysis
================================================

Quick access script for running individual comprehensive tests.
This script provides the simplest way to run one test at a time.

Usage:
    python run_single_test.py                  # Interactive menu
    python run_single_test.py T001             # Run T001
    python run_single_test.py author           # Run author test
    python run_single_test.py 3                # Run test #3
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append('..')
sys.path.append('.')

def show_test_menu():
    """Display available tests in a simple menu"""
    tests = [
        ("T001", "Publication Trends Analysis", "Verify correct count of books per year"),
        ("T002", "Top Authors Analysis", "Identify top 5 most prolific authors"),
        ("T003", "Language Distribution", "Count books by language correctly"),
        ("T004", "Publisher Analysis", "Count books grouped by publisher"),
        ("T005", "Missing ISBN Analysis", "Detect missing ISBN fields"),
        ("T006", "Year-Language Grouping", "Books per year by language (1000 records)")
    ]
    
    print("\n" + "="*70)
    print("DREAM BOOK SHOP - INDIVIDUAL TEST RUNNER")
    print("="*70)
    print("Select a test to run:")
    print()
    
    for i, (test_id, name, desc) in enumerate(tests, 1):
        print(f"{i}. {test_id}: {name}")
        print(f"   {desc}")
        print()
    
    print("7. Run ALL tests")
    print("8. Exit")
    print("="*70)
    
    return tests

def run_single_test_by_id(test_identifier):
    """Run a single test by identifier"""
    import subprocess
    
    # Map common identifiers to test IDs
    id_mapping = {
        '1': 'T001', 'T001': 'T001', 'publication': 'T001', 'trends': 'T001',
        '2': 'T002', 'T002': 'T002', 'author': 'T002', 'authors': 'T002',
        '3': 'T003', 'T003': 'T003', 'language': 'T003', 'languages': 'T003',
        '4': 'T004', 'T004': 'T004', 'publisher': 'T004', 'publishers': 'T004',
        '5': 'T005', 'T005': 'T005', 'isbn': 'T005',
        '6': 'T006', 'T006': 'T006', 'year-language': 'T006', 'grouping': 'T006'
    }
    
    test_id = id_mapping.get(test_identifier.lower(), test_identifier.upper())
    
    if test_id in ['T001', 'T002', 'T003', 'T004', 'T005', 'T006']:
        print(f"\n🔄 Running test {test_id}...")
        print("-" * 50)
        
        try:
            # Run the test using the comprehensive test runner
            result = subprocess.run([
                sys.executable, 'run_comprehensive_tests.py', 
                '--test', test_id, '--verbose'
            ], check=False, capture_output=False)
            
            return result.returncode == 0
        except FileNotFoundError:
            # Fallback to direct test execution
            try:
                result = subprocess.run([
                    sys.executable, 'test_comprehensive_analysis.py',
                    '--test', test_id, '--verbose'
                ], check=False, capture_output=False)
                
                return result.returncode == 0
            except Exception as e:
                print(f"Error running test: {e}")
                return False
    else:
        print(f"❌ Invalid test identifier: {test_identifier}")
        print("Valid identifiers: T001-T006, 1-6, publication, author, language, publisher, isbn, year-language")
        return False

def interactive_mode():
    """Run in interactive mode"""
    while True:
        tests = show_test_menu()
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '8':
                print("👋 Goodbye!")
                break
            elif choice == '7':
                print("\n🔄 Running ALL comprehensive tests...")
                print("-" * 50)
                import subprocess
                try:
                    result = subprocess.run([
                        sys.executable, 'run_comprehensive_tests.py', '--verbose'
                    ], check=False)
                    print("\n✅ All tests completed!")
                except Exception as e:
                    print(f"Error running tests: {e}")
            elif choice in ['1', '2', '3', '4', '5', '6']:
                test_id = f"T{choice.zfill(3)}"
                success = run_single_test_by_id(test_id)
                if success:
                    print(f"\n✅ Test {test_id} completed successfully!")
                else:
                    print(f"\n❌ Test {test_id} failed or had errors!")
            else:
                print("❌ Invalid choice! Please enter 1-8.")
            
            if choice != '8':
                input("\nPress Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Main execution function"""
    if len(sys.argv) == 1:
        # No arguments - run interactive mode
        interactive_mode()
    elif len(sys.argv) == 2:
        # One argument - run specific test
        test_identifier = sys.argv[1]
        success = run_single_test_by_id(test_identifier)
        sys.exit(0 if success else 1)
    else:
        print("Usage:")
        print("  python run_single_test.py           # Interactive mode")
        print("  python run_single_test.py T001      # Run specific test")
        print("  python run_single_test.py author    # Run by keyword")
        print("  python run_single_test.py 3         # Run by number")
        sys.exit(1)

if __name__ == '__main__':
    main()
