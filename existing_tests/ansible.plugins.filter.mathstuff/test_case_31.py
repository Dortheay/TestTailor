import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            bool_0 = False
            dict_0 = {}
            var_0 = module_1.rekey_on_member(bool_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
