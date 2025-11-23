import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            option_parser_0 = module_0.OptionParser()
            mockable_0 = option_parser_0.mockable()
            option_parser_1 = module_0.OptionParser()
            option_parser_2 = module_0.OptionParser()
            option_parser_2.print_help()
            str_0 = 'define'
            dict_0 = option_parser_2.group_dict(str_0)
            str_1 = None
            any_0 = option_parser_1.__getitem__(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
