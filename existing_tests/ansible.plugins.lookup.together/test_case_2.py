import unittest
import timeout_decorator
import ansible.plugins.lookup.together as module_0

class Test_Together_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            set_0 = set()
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
