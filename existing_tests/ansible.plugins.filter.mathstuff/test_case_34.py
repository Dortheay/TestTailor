import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            str_0 = 'Ii'
            list_0 = []
            var_0 = module_1.rekey_on_member(list_0, str_0)
            str_1 = 'nj\rR= \n\x0bb;l>'
            float_0 = None
            list_1 = [str_1, str_1, str_0]
            var_1 = module_1.unique(str_0, str_1, float_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
