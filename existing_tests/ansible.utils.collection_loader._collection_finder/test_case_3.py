import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        str_0 = 'sl'
        var_0 = ansible_collection_finder_0.find_module(str_0)
        ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(ansible_collection_finder_0, ansible_collection_finder_0)
        var_1 = ansible_path_hook_finder_0.__repr__()

if __name__ == "__main__":
    unittest.main()
