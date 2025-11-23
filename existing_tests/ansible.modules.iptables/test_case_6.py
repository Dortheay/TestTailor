import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        int_0 = None
        float_0 = -18.55103704286351
        str_0 = 'gze'
        float_1 = -1991.052247
        dict_0 = {str_0: float_0, int_0: float_1}
        var_0 = module_0.append_match_flag(float_0, str_0, str_0, dict_0)
        set_0 = None
        var_1 = module_0.append_wait(str_0, set_0, int_0)
        var_2 = module_0.main()

if __name__ == "__main__":
    unittest.main()
