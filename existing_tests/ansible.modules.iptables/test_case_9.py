import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'Q~Lwm'
            var_0 = module_0.construct_rule(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
