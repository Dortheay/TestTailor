import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            str_0 = 'vRx'
            bytes_0 = None
            str_1 = '4pvpJ_a<'
            set_0 = {bytes_0, str_0, str_0, bytes_0}
            var_0 = module_0.append_param(bytes_0, str_1, set_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
