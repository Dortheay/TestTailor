import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'R/k(g[8C+kU\tAAo3Wp`k'
            var_0 = module_0.to_ipv6_network(str_0)
            str_1 = '{6o4'
            var_1 = module_0.to_ipv6_network(str_1)
            bool_0 = False
            set_0 = set()
            var_2 = module_0.to_subnet(bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
