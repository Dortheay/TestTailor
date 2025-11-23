import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            bool_0 = True
            rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
            list_0 = []
            bool_1 = False
            var_0 = rough_parser_0.set_lo(bool_1)
            var_1 = rough_parser_0.set_str(list_0)
            var_2 = rough_parser_0.is_block_closer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
