import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = None
            bytes_0 = b'\xc2'
            bool_0 = False
            list_0 = [float_0, float_0, bool_0, bytes_0]
            bytes_1 = b'\x99t\xce|\x1d\xd2~\xb9\x07\xa31\x95\x9f\xea\xd2c'
            var_0 = module_0.check_required_one_of(bytes_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
