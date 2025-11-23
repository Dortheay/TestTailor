import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'W,YT^&CAvZAN@/'
            dict_0 = {str_0: str_0, str_0: str_0}
            list_0 = [dict_0, dict_0, str_0]
            dict_1 = {str_0: str_0, str_0: str_0}
            bool_0 = False
            var_0 = module_0.to_uuid(bool_0)
            list_1 = [str_0, str_0, list_0, dict_1]
            int_0 = 811
            var_1 = module_0.regex_search(int_0, list_1, *list_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
