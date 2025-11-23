import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        set_0 = set()
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
        var_0 = ansible_collection_finder_0.set_playbook_paths(set_0)
        str_0 = []
        str_1 = 'ansible_collections.my_collection'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_1, str_0)
        var_1 = ansible_collection_pkg_loader_base_0.get_filename(str_1)
        var_2 = ansible_collection_pkg_loader_base_0.get_filename(str_1)

if __name__ == "__main__":
    unittest.main()
