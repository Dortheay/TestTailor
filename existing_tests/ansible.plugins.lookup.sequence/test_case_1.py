import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        lookup_module_0 = module_0.LookupModule()
        tuple_0 = ()
        str_0 = '0e&ePRP.LED=[3AV&6X'
        var_0 = lookup_module_0.run(tuple_0, str_0)
        var_1 = lookup_module_0.generate_sequence()

if __name__ == "__main__":
    unittest.main()
