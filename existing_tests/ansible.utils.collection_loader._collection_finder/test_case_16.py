import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
            bool_0 = False
            int_0 = -1361
            str_0 = '#pj<yNN'
            bytes_0 = None
            list_0 = [bool_0, bytes_0, int_0, bool_0]
            ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, bytes_0, str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
