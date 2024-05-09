import unittest
import os

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for filename in os.listdir(os.path.dirname(__file__)):
        if filename.startswith('test_') and filename.endswith('.py') and filename != 'test_all.py':
            module_name = os.path.splitext(filename)[0]
            module = __import__(module_name)
            suite.addTests(loader.loadTestsFromModule(module))
    return suite

if __name__ == '__main__':
    unittest.main()
