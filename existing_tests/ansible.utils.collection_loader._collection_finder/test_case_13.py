import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = False
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
