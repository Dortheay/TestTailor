import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = '192.168.1.1'
            bool_0 = True
            var_0 = module_0.to_subnet(str_0, str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
