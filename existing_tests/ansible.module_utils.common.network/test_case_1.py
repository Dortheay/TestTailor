import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 1628
            var_0 = module_0.to_netmask(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
