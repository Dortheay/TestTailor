import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_finder as module_0

class Test__collection_finder_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
            str_0 = ''
            var_0 = ansible_collection_finder_0.find_module(str_0)
            str_1 = '/N'
            float_0 = -2864.0
            tuple_0 = (float_0,)
            dict_0 = {}
            ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(tuple_0, dict_0)
            var_1 = ansible_path_hook_finder_0.iter_modules(str_1)
            str_2 = '%s adv --no-tty --keyserver %s'
            set_0 = set()
            ansible_path_hook_finder_1 = module_0._AnsiblePathHookFinder(str_2, set_0)
            var_2 = ansible_collection_finder_0.find_module(ansible_path_hook_finder_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
