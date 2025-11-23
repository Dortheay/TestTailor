import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'W,YT^&CAvZAN@/'
            dict_0 = {str_0: str_0, str_0: str_0}
            list_0 = [dict_0, dict_0, str_0]
            dict_1 = {str_0: str_0, str_0: str_0}
            var_0 = module_0.combine()
            list_1 = [str_0, str_0, list_0, dict_1]
            str_1 = 'python'
            var_1 = module_0.strftime(str_1)
            int_0 = 811
            var_2 = module_0.regex_search(int_0, list_1, *list_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
