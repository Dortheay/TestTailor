import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            dict_0 = {}
            list_0 = [dict_0]
            str_0 = None
            var_0 = module_1.rekey_on_member(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
