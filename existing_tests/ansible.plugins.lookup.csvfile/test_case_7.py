import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = None
            float_0 = None
            list_0 = []
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.read_csv(str_0, float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
