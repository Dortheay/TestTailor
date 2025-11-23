import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '>gBm@|!mY&F@Me'
            int_0 = 25
            dict_0 = {str_0: int_0, str_0: str_0, str_0: int_0, int_0: str_0}
            set_0 = set()
            rough_parser_0 = module_0.RoughParser(dict_0, set_0)
            list_0 = [int_0, int_0, int_0, int_0]
            bytes_0 = b'Cn\x00T\x0e\x96|'
            rough_parser_1 = module_0.RoughParser(list_0, bytes_0)
            var_0 = rough_parser_1.set_lo(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
