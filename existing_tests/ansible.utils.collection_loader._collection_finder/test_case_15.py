import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bool_0 = None
            str_0 = 'LQgj6i:[pQ=F '
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_0)
            str_1 = '@=f$s?8IKwu4\r>0/*f'
            set_0 = {str_0, str_1, bool_0, str_0}
            float_0 = 347.3286
            ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(set_0, float_0)
            ansible_collection_loader_0 = module_0._AnsibleCollectionLoader(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
