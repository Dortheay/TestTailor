import unittest
import timeout_decorator
import tornado.options as module_0

class Test_Options_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = '\\nL.45\\VK#1`AnjU6\\ '
        option_parser_0 = module_0.OptionParser()
        dict_0 = option_parser_0.group_dict(str_0)
        option_parser_1 = module_0.OptionParser()
        iterable_0 = option_parser_1.items()
        option_parser_2 = module_0.OptionParser()
        str_1 = 'w'
        list_0 = [str_1]
        bool_0 = False
        list_1 = module_0.parse_command_line(list_0, bool_0)

if __name__ == "__main__":
    unittest.main()
