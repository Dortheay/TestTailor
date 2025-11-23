import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        var_0 = module_0.main()

if __name__ == "__main__":
    unittest.main()
