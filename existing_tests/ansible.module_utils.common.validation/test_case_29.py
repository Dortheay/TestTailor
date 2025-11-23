import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            dict_0 = {}
            str_0 = None
            var_0 = module_0.check_required_by(dict_0, str_0)
            str_1 = 'www-authenticate'
            var_1 = module_0.check_type_bool(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
