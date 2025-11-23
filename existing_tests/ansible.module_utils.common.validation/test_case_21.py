import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            str_0 = 'illegal runlevel specified'
            var_0 = module_0.safe_eval(str_0)
            dict_0 = {}
            var_1 = module_0.check_type_int(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
