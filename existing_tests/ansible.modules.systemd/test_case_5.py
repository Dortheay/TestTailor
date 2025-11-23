import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '__main__'
        dict_0 = {}
        float_0 = 0.0
        set_0 = {float_0}
        tuple_0 = (float_0, set_0, float_0, float_0)
        tuple_1 = (str_0, dict_0, tuple_0)
        var_0 = module_0.parse_systemctl_show(tuple_1)

if __name__ == "__main__":
    unittest.main()
