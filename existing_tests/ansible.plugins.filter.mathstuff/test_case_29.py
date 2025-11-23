import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            bool_0 = True
            dict_0 = {}
            var_0 = module_1.rekey_on_member(bool_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
