import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 4133
            float_0 = 1000.0
            list_0 = []
            var_0 = module_0.append_tcp_flags(int_0, float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
