import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            bool_0 = False
            rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
            list_0 = []
            var_0 = rough_parser_0.set_str(list_0)
            var_1 = rough_parser_0.find_good_parse_start(rough_parser_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
