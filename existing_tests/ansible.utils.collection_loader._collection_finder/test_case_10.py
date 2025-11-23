import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
            str_0 = 'n-{/D]fmQLBHU'
            ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
