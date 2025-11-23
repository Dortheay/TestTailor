import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            option_parser_0 = module_0.OptionParser()
            iterable_0 = option_parser_0.items()
            str_0 = 'Finnish'
            dict_0 = option_parser_0.group_dict(str_0)
            str_1 = 'CZb\nE\\UwmU6]p3uxgk'
            option_parser_1 = module_0.OptionParser()
            bool_0 = True
            str_2 = None
            str_3 = 'E)Op0Djb$t'
            optional_0 = None
            option_0 = module_0._Option(str_3, optional_0, str_3, str_0, bool_0, str_0, str_2)
            any_0 = option_0.parse(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
