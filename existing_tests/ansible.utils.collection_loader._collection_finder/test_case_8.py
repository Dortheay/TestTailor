import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            set_0 = None
            set_1 = {set_0, set_0, set_0}
            ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
