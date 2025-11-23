import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = "z(,qs$R'EAJ\tj"
        var_0 = module_0.is_masklen(str_0)

if __name__ == "__main__":
    unittest.main()
