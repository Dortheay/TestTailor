import unittest
import timeout_decorator
import ansible.plugins.lookup.ini as module_0

class Test_Ini_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '9bG*R^X0_'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            dict_1 = {}
            lookup_module_0 = module_0.LookupModule(**dict_1)
            var_0 = lookup_module_0.run(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
