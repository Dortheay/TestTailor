import unittest
import timeout_decorator
import ansible.plugins.lookup.ini as module_0

class Test_Ini_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '*#9H;jE>9v'
            dict_0 = {str_0: str_0}
            bool_0 = False
            set_0 = None
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.get_value(dict_0, str_0, bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
