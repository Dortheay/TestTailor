import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        expr_0 = module_1.expr()
        str_0 = module_0.const_type(expr_0)

if __name__ == "__main__":
    unittest.main()
