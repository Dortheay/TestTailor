import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
            str_0 = 'ansible_collections.my_collection'
            ansible_collection_finder_1 = module_0._AnsibleCollectionFinder()
            ansible_path_hook_finder_0 = None
            float_0 = 100.0
            ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, ansible_collection_finder_1, ansible_path_hook_finder_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
