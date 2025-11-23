import unittest
import timeout_decorator
import ansible.plugins.lookup.fileglob as module_0

class Test_Fileglob_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'ansible_search_path'
        str_1 = {str_0: str_0}
        lookup_module_0 = module_0.LookupModule()
        str_2 = '|\t'
        var_0 = lookup_module_0.run(str_2, str_1)

if __name__ == "__main__":
    unittest.main()
