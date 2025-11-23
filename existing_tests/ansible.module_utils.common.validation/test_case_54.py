import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_55(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '||%\x0bC&\rmG'
        var_0 = module_0.check_mutually_exclusive(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
