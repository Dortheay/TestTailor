import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_38(self):
        try:
            dict_0 = None
            list_0 = [dict_0, dict_0, dict_0]
            list_1 = [list_0, dict_0, dict_0, list_0, dict_0]
            var_0 = module_0.rand(dict_0, list_1)
            str_0 = 'done checking to see if all hosts have failed'
            var_1 = module_0.from_yaml(str_0)
            bytes_0 = b'\t\x1bQ0V\xe7UxV\xd2_\x93\xa3v^\xb4\xced\xe7'
            list_2 = [dict_0, dict_0, list_0]
            var_2 = module_0.to_json(list_2)
            var_3 = module_0.dict_to_list_of_dict_key_value_elements(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
