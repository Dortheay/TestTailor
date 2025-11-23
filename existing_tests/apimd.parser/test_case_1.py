import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'Constants'
        int_0 = -3461
        str_1 = 'uRD,Q"{g;c5hsQL\x0b2%K]'
        str_2 = module_0.parent(str_1, level=int_0)
        int_1 = 1954
        str_3 = module_0.parent(str_0, level=int_1)
        str_4 = '.BU)4.\t>ygA-lhj\\2|'
        str_5 = module_0.code(str_4)
        str_6 = module_0.code(str_0)

if __name__ == "__main__":
    unittest.main()
