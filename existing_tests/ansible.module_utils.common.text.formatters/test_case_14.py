import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 1048576
        var_0 = module_0.bytes_to_human(int_0)
        bool_0 = True
        var_1 = module_0.bytes_to_human(int_0, bool_0)
        int_1 = 1536
        str_0 = 'K'
        var_2 = module_0.bytes_to_human(int_1, str_0)
        int_2 = 1600
        var_3 = module_0.bytes_to_human(int_2, bool_0, str_0)
        int_3 = 512
        var_4 = module_0.bytes_to_human(int_3)
        int_4 = 20
        var_5 = bool_0 << int_4
        var_6 = module_0.bytes_to_human(var_5)
        int_5 = 40
        var_7 = bool_0 << int_5
        str_1 = 'T'
        var_8 = module_0.bytes_to_human(var_7, str_1)
        int_6 = 0
        var_9 = module_0.bytes_to_human(int_6)

if __name__ == "__main__":
    unittest.main()
