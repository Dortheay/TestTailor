import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 1570.15
            str_0 = 'unsafe'
            str_1 = None
            var_0 = module_0.append_param(str_0, float_0, str_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
