import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            bool_0 = None
            str_0 = 'RI%*Z=@vW>"9h[4p'
            var_0 = module_0.get_iptables_version(bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
