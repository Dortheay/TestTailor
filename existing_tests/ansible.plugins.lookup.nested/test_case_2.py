import unittest
import timeout_decorator
import ansible.plugins.lookup.nested as module_0

class Test_Nested_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            list_0 = []
            var_0 = lookup_module_0.run(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
