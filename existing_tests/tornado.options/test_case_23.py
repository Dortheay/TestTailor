import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = '\x0bhP2%mq9j'
            option_parser_0 = module_0.OptionParser()
            float_0 = 0.3
            module_0.define(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
