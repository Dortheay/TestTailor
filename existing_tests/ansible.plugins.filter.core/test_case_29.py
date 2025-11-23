import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            str_0 = 'W,YT^&CAvkAN@/'
            dict_0 = {str_0: str_0, str_0: str_0}
            bytes_0 = b'\xb2(\xdfb\x0f\x8e\xd9\x15I\xd4\xc2\xc3\xa0\x9d\xb9x\t\xcc'
            complex_0 = None
            filter_module_0 = module_0.FilterModule()
            dict_1 = {complex_0: filter_module_0, str_0: str_0, complex_0: str_0}
            bool_0 = False
            var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0, bool_0)
            int_0 = 1
            var_1 = module_0.extract(bytes_0, complex_0, dict_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
