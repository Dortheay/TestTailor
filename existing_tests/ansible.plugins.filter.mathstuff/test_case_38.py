import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            str_0 = 'P{vO4'
            dict_0 = {}
            var_0 = module_1.max(str_0, str_0, **dict_0)
            list_0 = []
            str_1 = None
            bool_0 = False
            var_1 = module_1.intersect(bool_0, str_0, dict_0)
            var_2 = module_1.rekey_on_member(list_0, str_1)
            filter_module_0 = module_1.FilterModule()
            bool_1 = False
            int_0 = -746
            var_3 = module_1.unique(bool_0, filter_module_0, bool_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
