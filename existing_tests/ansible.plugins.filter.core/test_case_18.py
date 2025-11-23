import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = '7seF"W])('
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            list_0 = [str_0, dict_0]
            int_0 = 1069
            list_1 = [list_0]
            var_0 = module_0.ternary(int_0, dict_0, list_1)
            var_1 = module_0.get_hash(str_0)
            str_1 = 'posix_extended'
            var_2 = module_0.list_of_dict_key_value_elements_to_dict(list_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
