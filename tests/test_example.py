import unittest
import sys
sys.path.append('..')

class TestExample(unittest.TestCase):
    def test_example_pass(self):
        """Test that should pass"""
        self.assertEqual(1 + 1, 2)
    
    def test_example_string(self):
        """Test string operations"""
        self.assertEqual("hello".upper(), "HELLO")
    
    def test_example_list(self):
        """Test list operations"""
        test_list = [1, 2, 3]
        self.assertEqual(len(test_list), 3)
        self.assertIn(2, test_list)

def run_single_test():
    """Run this test file individually with detailed output"""
    print("=" * 70)
    print("                TESTING EXAMPLE CLASS")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExample)
    
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