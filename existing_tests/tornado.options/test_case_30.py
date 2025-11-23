import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            option_parser_0 = module_0.OptionParser()
            iterable_0 = option_parser_0.items()
            str_0 = 'inn'
            dict_0 = option_parser_0.group_dict(str_0)
            text_i_o_0 = None
            str_1 = 'CZb\nE\\UwmU6]p3uxgk'
            option_parser_1 = module_0.OptionParser()
            iterator_0 = option_parser_0.__iter__()
            mockable_0 = option_parser_0.mockable()
            option_0 = module_0._Option(str_1, iterator_0, mockable_0, str_1)
            option_0.set(text_i_o_0)
            any_0 = option_0.value()
            list_0 = module_0.parse_command_line()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
