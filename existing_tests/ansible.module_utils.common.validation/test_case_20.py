import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = 'YQ]CcaMt`\r=,K'
            list_0 = [str_0, str_0, str_0]
            var_0 = module_0.check_type_jsonarg(list_0)
            var_1 = module_0.check_type_dict(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
