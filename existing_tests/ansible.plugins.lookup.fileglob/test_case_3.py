import unittest
import timeout_decorator
import ansible.plugins.lookup.fileglob as module_0

class Test_Fileglob_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            str_0 = 'ansible_search_path'
            str_1 = 'testdir'
            str_2 = [str_1]
            str_3 = {str_0: str_2}
            str_4 = 'testdir/sample1.txt'
            var_0 = lookup_module_0.run(str_4, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
