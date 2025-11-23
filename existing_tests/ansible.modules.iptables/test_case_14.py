import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            set_0 = set()
            str_0 = 'EtT%)'
            bool_0 = False
            var_0 = module_0.append_csv(set_0, str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
