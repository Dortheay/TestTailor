import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_76(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        int_0 = 2881
        var_0 = module_0.check_type_bits(int_0)
        str_0 = 'y@i)TNz`@\r@\\F'
        bool_0 = True
        var_1 = module_0.check_type_raw(bool_0)
        str_1 = "E\x0bx8bR/#Ei'g[!"
        var_2 = module_0.check_required_together(str_0, str_1)

if __name__ == "__main__":
    unittest.main()
