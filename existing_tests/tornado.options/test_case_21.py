import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            option_parser_0 = module_0.OptionParser()
            mockable_0 = module_0._Mockable(option_parser_0)
            module_0.print_help(mockable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
