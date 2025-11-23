import unittest
import timeout_decorator
import ansible.collections.list as module_0

class Test_List_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '/valid/path1'
            bool_0 = True
            var_0 = module_0.list_valid_collection_paths(str_0, bool_0)
            var_1 = list(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
