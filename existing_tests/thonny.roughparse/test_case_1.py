import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = True
        rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
        str_0 = ''
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.find_good_parse_start()
        var_2 = rough_parser_0.get_base_indent_string()

if __name__ == "__main__":
    unittest.main()
