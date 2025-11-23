import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'h4'
        assign_0 = module_1.Assign()
        bool_0 = module_0.is_public_family(str_0)
        bool_1 = module_0.is_magic(str_0)

if __name__ == "__main__":
    unittest.main()
