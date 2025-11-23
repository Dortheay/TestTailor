import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_57(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 2881
        var_0 = module_0.check_type_bits(int_0)
        float_0 = 2.0
        str_0 = 'y@i)TNz`@\r@\\F'
        complex_0 = None
        bool_0 = True
        var_1 = module_0.check_type_raw(bool_0)
        str_1 = "E\x0bx8bR/#Ei'g[!"
        var_2 = module_0.check_required_one_of(complex_0, float_0)
        var_3 = module_0.check_required_together(str_0, str_1)

if __name__ == "__main__":
    unittest.main()
