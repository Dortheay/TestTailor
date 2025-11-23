import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
            set_0 = {ansible_collection_finder_0}
            list_0 = [set_0, set_0, set_0]
            float_0 = 1826.860452
            ansible_collection_finder_1 = module_0._AnsibleCollectionFinder(list_0, float_0)
            int_0 = 783
            str_0 = 'the specified roles path exists and is not a directory.'
            ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(int_0, str_0)
            ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
