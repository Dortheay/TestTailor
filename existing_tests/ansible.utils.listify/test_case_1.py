import unittest
import timeout_decorator
import ansible.utils.listify as module_0

class Test_Listify_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 99
            list_0 = [int_0, int_0]
            str_0 = 'hoK"0ZjwhGBKoL:{^'
            float_0 = 2153.0
            str_1 = '`T'
            var_0 = module_0.listify_lookup_plugin_terms(str_0, list_0, float_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
