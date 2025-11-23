import unittest
import timeout_decorator
import ansible.plugins.lookup.first_found as module_0

class Test_First_found_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'LookupBase'
            str_1 = 'tv\rY'
            str_2 = 'Fabj'
            dict_0 = {str_0: str_0, str_1: str_1, str_2: str_0}
            set_0 = set()
            lookup_module_0 = module_0.LookupModule(set_0)
            var_0 = lookup_module_0.run(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
