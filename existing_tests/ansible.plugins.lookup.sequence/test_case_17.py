import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = '0-5/E1'
            str_1 = 'start=5 end=10'
            str_2 = [str_0, str_1]
            str_3 = 'dummy_var'
            str_4 = 'test_value'
            str_5 = {str_3: str_4}
            var_0 = {}
            lookup_module_0 = module_0.LookupModule()
            var_1 = lookup_module_0.run(str_2, str_5, **var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
