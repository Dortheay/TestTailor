import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '\\r\x0babzU'
            str_1 = '__init__'
            option_parser_0 = module_0.OptionParser()
            bool_0 = option_parser_0.__contains__(str_1)
            module_0.print_help()
            option_parser_1 = module_0.OptionParser()
            option_parser_1.__setattr__(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
