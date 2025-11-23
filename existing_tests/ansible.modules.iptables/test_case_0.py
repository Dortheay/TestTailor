import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = None
        str_0 = '6'
        float_0 = -544.0
        dict_0 = {int_0: float_0}
        var_0 = module_0.append_match_flag(float_0, str_0, str_0, dict_0)
        var_1 = module_0.main()

if __name__ == "__main__":
    unittest.main()
