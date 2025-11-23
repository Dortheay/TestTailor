import unittest
import timeout_decorator
import ansible.plugins.lookup.template as module_0

class Test_Template_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        lookup_module_0 = module_0.LookupModule()

if __name__ == "__main__":
    unittest.main()
