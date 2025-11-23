import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        try:
            float_0 = 0.001
            str_0 = ''
            dict_0 = {str_0: float_0}
            str_1 = '[}'
            bool_0 = False
            var_0 = module_0.to_bool(bool_0)
            var_1 = module_0.get_encrypted_password(dict_0, dict_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
