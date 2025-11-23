import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
            list_0 = []
            var_0 = rough_parser_0.set_str(list_0)
            var_1 = rough_parser_0.get_last_open_bracket_pos()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
