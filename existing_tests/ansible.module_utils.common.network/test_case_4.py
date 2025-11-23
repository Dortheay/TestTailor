import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = False
            var_0 = module_0.to_ipv6_network(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
