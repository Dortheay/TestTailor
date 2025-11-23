import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x97S'
            bytes_1 = b'\xe4a\xf3^P\x04'
            float_0 = 21.2
            rough_parser_0 = module_0.RoughParser(bytes_1, float_0)
            var_0 = rough_parser_0.find_good_parse_start(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
