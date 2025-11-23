import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            option_parser_0 = module_0.OptionParser()
            dict_0 = option_parser_0.as_dict()
            str_0 = None
            dict_1 = option_parser_0.group_dict(str_0)
            option_parser_1 = module_0.OptionParser()
            option_parser_1.run_parse_callbacks()
            bool_0 = option_parser_1.__contains__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
