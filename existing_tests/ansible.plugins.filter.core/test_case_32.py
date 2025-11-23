import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            str_0 = 'W,YT^&CAvZAN@/'
            float_0 = 0.5
            list_0 = [float_0, str_0]
            str_1 = 'r"&+Y]+X4\x0c'
            bool_0 = True
            tuple_0 = (list_0, str_1, bool_0)
            filter_module_0 = module_0.FilterModule()
            var_0 = module_0.randomize_list(tuple_0, filter_module_0)
            var_1 = module_0.to_bool(float_0)
            var_2 = module_0.regex_replace()
            dict_0 = {str_0: str_0, str_0: var_1, str_0: str_0, str_0: var_2}
            list_1 = [dict_0, dict_0, str_0, str_0]
            list_2 = [str_0, str_0, list_1, dict_0]
            var_3 = module_0.subelements(dict_0, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
