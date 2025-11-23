import unittest
import timeout_decorator
import ansible.playbook.collectionsearch as module_0

class Test_Collectionsearch_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        collection_search_0 = module_0.CollectionSearch()

if __name__ == "__main__":
    unittest.main()
