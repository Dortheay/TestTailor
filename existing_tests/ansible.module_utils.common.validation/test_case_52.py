import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '|:Y1Y|a(mxwodj2aR'
        var_0 = module_0.safe_eval(str_0)

if __name__ == "__main__":
    unittest.main()
