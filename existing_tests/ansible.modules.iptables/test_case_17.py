import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = 54
            int_1 = 1089
            dict_0 = {}
            var_0 = module_0.append_wait(int_0, int_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
