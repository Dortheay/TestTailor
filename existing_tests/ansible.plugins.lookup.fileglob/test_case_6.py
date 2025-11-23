import unittest
import timeout_decorator
import ansible.plugins.lookup.fileglob as module_0

class Test_Fileglob_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'ansible_search_path'
        str_1 = '/mock/path1'
        str_2 = {str_0: str_1}
        lookup_module_0 = module_0.LookupModule()
        str_3 = '|.'
        var_0 = lookup_module_0.run(str_3, str_2)

if __name__ == "__main__":
    unittest.main()
