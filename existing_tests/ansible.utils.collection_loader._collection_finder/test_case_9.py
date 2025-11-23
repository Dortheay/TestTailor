import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '.uq(JL<XzCc 2Mx#G N'
            ansible_collection_root_pkg_loader_0 = module_0._AnsibleCollectionRootPkgLoader(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
