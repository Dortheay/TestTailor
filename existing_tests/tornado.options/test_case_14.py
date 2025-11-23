import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            option_parser_0 = module_0.OptionParser()
            mockable_0 = option_parser_0.mockable()
            option_parser_0.run_parse_callbacks()
            str_0 = '^eYMO!r+h'
            bool_0 = False
            option_parser_0.__setitem__(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
