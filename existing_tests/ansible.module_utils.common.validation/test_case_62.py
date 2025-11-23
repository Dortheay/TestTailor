import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_63(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        str_0 = "o>'`JtJ{=i\x0c!sU"
        float_0 = 2452.0
        var_0 = module_0.check_type_float(float_0)
        var_1 = module_0.check_type_dict(str_0)

if __name__ == "__main__":
    unittest.main()
