import unittest
import timeout_decorator
import tornado.options as module_0

class Test_Options_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '\\nL.45\\VK#1`AnjU6\\ '
        option_parser_0 = module_0.OptionParser()
        dict_0 = option_parser_0.group_dict(str_0)
        option_parser_1 = module_0.OptionParser()
        iterable_0 = option_parser_1.items()

if __name__ == "__main__":
    unittest.main()
