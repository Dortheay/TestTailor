import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '$R][aYKo'
            var_0 = module_0.to_ipv6_subnet(str_0)
            bool_0 = True
            float_0 = -129.9316
            bytes_0 = b'\xe6'
            var_1 = module_0.to_subnet(bool_0, float_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
