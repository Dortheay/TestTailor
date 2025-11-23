import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '^eYMO!r+h'
            bool_0 = True
            option_parser_0 = module_0.OptionParser()
            option_parser_0.__setitem__(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
