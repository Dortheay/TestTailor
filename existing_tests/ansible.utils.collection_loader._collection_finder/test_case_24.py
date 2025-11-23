import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'ansible_collections'
            ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_0, str_0)
            var_0 = [os.path.join(p, str_0) for p in str_0]
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
