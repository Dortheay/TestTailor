import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'Hn`$5Gv'
        bool_0 = module_0.is_public_family(str_0)
        assign_0 = module_1.Assign()
        str_1 = module_0.esc_underscore(str_0)
        str_2 = module_0.code(str_0)
        str_3 = 'K>cq^AJ['
        bool_1 = module_0.is_magic(str_3)

if __name__ == "__main__":
    unittest.main()
