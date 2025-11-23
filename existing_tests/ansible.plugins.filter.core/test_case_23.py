import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            float_0 = 0.001
            str_0 = ''
            var_0 = module_0.regex_search(float_0, str_0)
            bool_0 = False
            str_1 = 'Q8r!oo!P;A.'
            var_1 = module_0.from_yaml_all(str_1)
            int_0 = 4095
            list_0 = [str_0, str_1, int_0]
            var_2 = module_0.get_encrypted_password(bool_0, int_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
