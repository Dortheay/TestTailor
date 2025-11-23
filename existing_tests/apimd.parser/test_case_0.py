import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'KQNt_va\ns='
        str_1 = module_0.esc_underscore(str_0)

if __name__ == "__main__":
    unittest.main()
