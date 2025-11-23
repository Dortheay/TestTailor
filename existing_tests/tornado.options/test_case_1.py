import unittest
import timeout_decorator
import tornado.options as module_0

class Test_Options_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        option_parser_0 = module_0.OptionParser()
        iterable_0 = option_parser_0.items()

if __name__ == "__main__":
    unittest.main()
