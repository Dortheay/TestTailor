import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 1280
            bytes_0 = b'SU\xc9 \xa5\xef\xdb\x8b3'
            rough_parser_0 = module_0.RoughParser(int_0, bytes_0)
            var_0 = rough_parser_0.get_num_lines_in_stmt()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
