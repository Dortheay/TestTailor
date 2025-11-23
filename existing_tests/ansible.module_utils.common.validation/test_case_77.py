import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_78(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        str_0 = "{'key': 'value'}"
        var_0 = module_0.safe_eval(str_0)
        var_1 = module_0.safe_eval(var_0)
        str_1 = "=rmhC'eB,X)ZL"
        var_2 = module_0.safe_eval(str_1)
        str_2 = 'import os'
        var_3 = module_0.safe_eval(str_2)

if __name__ == "__main__":
    unittest.main()
