import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '0-5/1'
        str_1 = [str_0, str_0]
        var_0 = {}
        lookup_module_0 = module_0.LookupModule()
        str_2 = '2'
        var_1 = lookup_module_0.run(str_1, str_2, **var_0)

if __name__ == "__main__":
    unittest.main()
