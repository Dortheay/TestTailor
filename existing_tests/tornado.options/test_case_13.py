import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '\\nL.45\\VK#1`AnjU\\ '
            module_0.define(str_0, str_0)
            option_parser_0 = module_0.OptionParser()
            dict_0 = option_parser_0.group_dict(str_0)
            option_parser_1 = module_0.OptionParser()
            option_parser_1.run_parse_callbacks()
            iterable_0 = option_parser_1.items()
            option_parser_2 = module_0.OptionParser()
            list_0 = module_0.parse_command_line()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
