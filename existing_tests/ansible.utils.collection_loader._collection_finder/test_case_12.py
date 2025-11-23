import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'W'
            list_0 = []
            int_0 = -2415
            tuple_0 = ()
            ansible_collection_ref_0 = module_0.AnsibleCollectionRef(str_0, list_0, int_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
