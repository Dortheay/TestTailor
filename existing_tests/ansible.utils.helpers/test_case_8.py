import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '50%'
        int_0 = 100
        var_0 = module_0.pct_to_int(str_0, int_0)
        str_1 = '33%'
        var_1 = module_0.pct_to_int(str_1, int_0)
        str_2 = '0%'
        int_1 = 5
        var_2 = module_0.pct_to_int(str_2, int_0, int_1)
        str_3 = '25'
        var_3 = module_0.pct_to_int(str_3, int_0)
        int_2 = 10
        var_4 = module_0.pct_to_int(str_2, int_0, int_2)

if __name__ == "__main__":
    unittest.main()
