import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            bool_0 = True
            float_0 = 2174.0
            list_0 = [bool_0, bool_0, float_0]
            set_0 = set()
            str_0 = '"'
            ansible_collection_ref_0 = module_0.AnsibleCollectionRef(list_0, set_0, list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
