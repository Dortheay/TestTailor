import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_75(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        dict_0 = {}
        str_0 = ''
        var_0 = module_0.check_required_arguments(dict_0, str_0)

if __name__ == "__main__":
    unittest.main()
