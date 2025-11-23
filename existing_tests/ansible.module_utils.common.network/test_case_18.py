import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'R/k(g[8C+kU\tAAo3Wp`k'
        var_0 = module_0.to_ipv6_network(str_0)
        bytes_0 = None
        var_1 = module_0.is_netmask(bytes_0)

if __name__ == "__main__":
    unittest.main()
