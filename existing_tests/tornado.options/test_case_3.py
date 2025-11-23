import unittest
import timeout_decorator
import tornado.options as module_0

class Test_Options_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        option_parser_0 = module_0.OptionParser()
        dict_0 = option_parser_0.as_dict()

if __name__ == "__main__":
    unittest.main()
