import unittest
import timeout_decorator
import ansible.plugins.lookup.url as module_0

class Test_Url_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '|fL#m'
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
