import unittest
import timeout_decorator
import ansible.plugins.lookup.random_choice as module_0

class Test_Random_choice_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
