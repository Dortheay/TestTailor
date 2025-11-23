import unittest
import timeout_decorator
import ansible.plugins.lookup.fileglob as module_0

class Test_Fileglob_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            lookup_module_0 = module_0.LookupModule(dict_0, **dict_0)
            str_0 = 'H!VY\'S3"jEo$2+n7v2'
            var_0 = lookup_module_0.run(str_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
