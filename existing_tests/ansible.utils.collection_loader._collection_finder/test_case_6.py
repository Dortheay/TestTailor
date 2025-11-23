import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'ansible_collections.sample_module'
        str_1 = '/path/to/collections'
        str_2 = [str_1]
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_2)
        var_0 = ansible_collection_pkg_loader_base_0.get_filename(str_0)

if __name__ == "__main__":
    unittest.main()
