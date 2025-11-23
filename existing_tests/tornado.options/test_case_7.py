import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'F|'
            option_parser_0 = module_0.OptionParser()
            mockable_0 = option_parser_0.mockable()
            mockable_0.__setattr__(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
