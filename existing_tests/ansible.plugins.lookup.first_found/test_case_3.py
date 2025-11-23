import unittest
import timeout_decorator
import ansible.plugins.lookup.first_found as module_0

class Test_First_found_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = []
            int_0 = -4430
            dict_0 = {}
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(list_0, int_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
