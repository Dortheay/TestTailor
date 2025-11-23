import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = 415
            bool_0 = None
            bytes_0 = b'\xe5'
            set_0 = {int_0, bool_0}
            float_0 = 773.3235
            bytes_1 = b'f\x8cE\x8e\xa8$}\xc03\xd2>\x03N2\xeb'
            var_0 = module_0.check_type_raw(bytes_1)
            var_1 = module_0.check_type_raw(float_0)
            var_2 = module_0.count_terms(bytes_0, set_0)
            bytes_2 = b'\xf8-2\x9e\xec\xdb'
            var_3 = module_0.check_type_raw(bytes_2)
            bytes_3 = b''
            var_4 = module_0.check_type_str(bytes_3, bytes_3, bytes_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
