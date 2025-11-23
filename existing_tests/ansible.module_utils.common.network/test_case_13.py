import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = '255.255.255.0'
            var_0 = module_0.to_subnet(str_0, str_0)
            bool_0 = True
            var_1 = module_0.to_subnet(str_0, str_0, bool_0)
            str_1 = '192.168.1.1'
            str_2 = '33'
            var_2 = module_0.to_subnet(str_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
