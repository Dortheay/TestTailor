import unittest
import timeout_decorator
import ansible.plugins.lookup.template as module_0

class Test_Template_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 423
            list_0 = [int_0, int_0, int_0, int_0]
            float_0 = -1053.604819
            set_0 = set()
            lookup_module_0 = module_0.LookupModule(set_0)
            var_0 = lookup_module_0.run(list_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
