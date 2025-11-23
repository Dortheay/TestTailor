import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()

if __name__ == "__main__":
    unittest.main()
