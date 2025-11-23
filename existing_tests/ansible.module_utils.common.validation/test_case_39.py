import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_39(self):
        try:
            str_0 = 'YQ\x0b]\tCcaet`\r=,b'
            var_0 = module_0.check_type_dict(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
