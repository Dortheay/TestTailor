import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            option_parser_0 = module_0.OptionParser()
            mockable_0 = option_parser_0.mockable()
            set_0 = option_parser_0.groups()
            str_0 = 'aD85Q?A6W!8$\x0bSd\x0bFm&'
            module_0.parse_config_file(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
