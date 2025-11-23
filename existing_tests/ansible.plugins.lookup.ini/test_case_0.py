import unittest
import timeout_decorator
import ansible.plugins.lookup.ini as module_0

class Test_Ini_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'a_m/.?R}!k,0?p6'
            bytes_0 = None
            list_0 = [bytes_0]
            dict_0 = {str_0: str_0}
            str_1 = '\\BSECc"3L_-f^'
            dict_1 = {str_1: str_1}
            lookup_module_0 = module_0.LookupModule(**dict_1)
            var_0 = lookup_module_0.get_value(str_0, bytes_0, list_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
