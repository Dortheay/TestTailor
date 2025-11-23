import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = None
            bool_1 = True
            var_0 = module_0.to_subnet(bool_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
