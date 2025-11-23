import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_65(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = 'H"&-\x0c($U*u\\hO",9\t\'='
        var_0 = module_0.check_type_raw(str_0)

if __name__ == "__main__":
    unittest.main()
