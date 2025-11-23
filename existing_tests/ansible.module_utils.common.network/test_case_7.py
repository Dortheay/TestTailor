import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bool_0 = True
            var_0 = module_0.is_mac(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
