import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            bool_0 = True
            rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
            str_0 = ''
            var_0 = rough_parser_0.set_str(str_0)
            var_1 = rough_parser_0.is_block_opener()
            var_2 = rough_parser_0.compute_bracket_indent()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
