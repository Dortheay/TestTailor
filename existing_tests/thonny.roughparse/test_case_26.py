import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            bool_0 = True
            rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
            str_0 = ''
            var_0 = rough_parser_0.set_str(str_0)
            var_1 = rough_parser_0.find_good_parse_start()
            bytes_0 = b'I\xf2\xd9\xff)\xc5n\xd0\x0c\x9cA\x0c8\xd6\x90\xa2'
            var_2 = rough_parser_0.find_good_parse_start(bytes_0)
            var_3 = rough_parser_0.compute_bracket_indent()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
