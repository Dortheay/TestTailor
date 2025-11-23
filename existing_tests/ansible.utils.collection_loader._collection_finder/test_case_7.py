import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'ansible_collections.my_collection'
        ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
        var_0 = ansible_collection_pkg_loader_base_0.get_filename(str_0)
        var_1 = ansible_collection_pkg_loader_base_0.get_filename(str_0)
        var_2 = ansible_collection_pkg_loader_base_0.get_filename(str_0)
        complex_0 = None
        var_3 = ansible_collection_pkg_loader_base_0.iter_modules(complex_0)

if __name__ == "__main__":
    unittest.main()
