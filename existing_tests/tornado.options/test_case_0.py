import unittest
import timeout_decorator
import tornado.options as module_0

class Test_Options_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        text_i_o_0 = None
        str_0 = 'CZb\nE\\]wmUr]p3uxgk'
        option_parser_0 = module_0.OptionParser()
        iterator_0 = option_parser_0.__iter__()
        mockable_0 = option_parser_0.mockable()
        option_0 = module_0._Option(str_0, iterator_0, mockable_0, str_0)
        option_0.set(text_i_o_0)

if __name__ == "__main__":
    unittest.main()
