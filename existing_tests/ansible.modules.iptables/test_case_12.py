import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 1570.15
            float_1 = 1000.0
            tuple_0 = (float_1,)
            list_0 = [float_0, float_1]
            int_0 = -1600
            set_0 = None
            var_0 = module_0.append_param(tuple_0, list_0, int_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
