import unittest
import timeout_decorator
import ansible.collections.list as module_0

class Test_List_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '/test_path/ansible_collections'
            str_1 = '/test_path/ansible_collections/namespace1'
            str_2 = '/test_path/ansible_collections/namespace1/collection1'
            str_3 = '/test_path/ansible_collections/namespace2'
            str_4 = '/test_path/ansible_collections/namespace2/collection2'
            var_0 = lambda x: x in str_2
            str_5 = [str_0, str_1, str_2, str_3, str_4]
            var_1 = lambda x: x in str_5
            var_2 = []
            var_3 = lambda x: var_21.get(x, var_2)
            var_4 = module_0.list_collection_dirs()
            var_5 = list(var_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
