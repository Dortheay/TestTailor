import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = 'ansible_collections.example.submodule'
            str_1 = '/path/to/collection'
            str_2 = [str_1]
            ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_2)
            var_0 = ansible_collection_pkg_loader_base_0.is_package(str_0)
            bool_0 = True
            var_1 = ansible_collection_pkg_loader_base_0.get_filename(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
