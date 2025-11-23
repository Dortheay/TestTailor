import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            var_0 = module_0.combine()
            str_0 = 'Atww`L}gwz-V|FLo'
            str_1 = 'QEr2eFc7\x0bYQG\x0bl7*J('
            dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
            float_0 = 2.0
            var_1 = module_0.from_yaml(float_0)
            var_2 = module_0.get_hash(dict_0)
            int_0 = -2903
            var_3 = module_0.get_encrypted_password(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
