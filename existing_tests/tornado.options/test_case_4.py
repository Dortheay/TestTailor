import unittest
import timeout_decorator
import tornado.options as module_0

class Test_Options_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        module_0.print_help()

if __name__ == "__main__":
    unittest.main()
