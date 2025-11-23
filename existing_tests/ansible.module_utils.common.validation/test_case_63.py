import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_64(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        str_0 = "o>'`JtJ{=i\x0c!sU"
        float_0 = 2452.0
        bytes_0 = b'qW#|\x88%\xd1B\xe0w\x87\xc9\xb2\xa40\xb9XM\xc2\xa5'
        tuple_0 = (bytes_0,)
        var_0 = module_0.check_type_path(tuple_0)
        var_1 = module_0.check_type_float(float_0)
        var_2 = module_0.check_type_dict(str_0)

if __name__ == "__main__":
    unittest.main()
