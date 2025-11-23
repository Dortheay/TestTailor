import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            option_parser_0 = module_0.OptionParser()
            iterable_0 = option_parser_0.items()
            text_i_o_0 = None
            str_0 = 'CZb\nE\\UwmU6]p3uxgk'
            option_parser_1 = module_0.OptionParser()
            iterator_0 = option_parser_1.__iter__()
            mockable_0 = option_parser_0.mockable()
            option_0 = module_0._Option(str_0, iterator_0, mockable_0, str_0)
            option_0.set(text_i_o_0)
            option_0.set(mockable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
