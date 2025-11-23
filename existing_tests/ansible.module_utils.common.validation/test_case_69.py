import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_70(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        float_0 = None
        str_0 = '|\x0b&u^m'
        var_0 = module_0.check_mutually_exclusive(str_0, str_0)
        dict_0 = {str_0: float_0}
        set_0 = set()
        var_1 = module_0.check_required_by(dict_0, set_0)

if __name__ == "__main__":
    unittest.main()
