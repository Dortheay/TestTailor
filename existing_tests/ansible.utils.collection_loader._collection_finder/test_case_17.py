import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'ansible_collections.some_namespace'
            str_1 = '/path/to/collections'
            str_2 = [str_1]
            ansible_collection_n_s_pkg_loader_0 = module_0._AnsibleCollectionNSPkgLoader(str_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
