import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = '192.168.1.1'
            str_1 = '24'
            var_0 = module_0.to_subnet(str_0, str_1)
            bool_0 = True
            var_1 = module_0.to_subnet(str_0, str_1, bool_0)
            var_2 = module_0.to_subnet(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
