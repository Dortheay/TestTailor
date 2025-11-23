import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = ';|5'
        var_0 = module_0.to_ipv6_subnet(str_0)

if __name__ == "__main__":
    unittest.main()
