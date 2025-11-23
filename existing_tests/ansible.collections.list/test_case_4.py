import unittest
import timeout_decorator
import ansible.collections.list as module_0

class Test_List_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'namespace.collection'
            var_0 = module_0.list_collection_dirs(str_0, str_0)
            var_1 = list(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
