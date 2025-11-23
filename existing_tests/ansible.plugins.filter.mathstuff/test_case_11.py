import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = {}
            int_0 = 774
            set_0 = set()
            var_0 = module_1.symmetric_difference(int_0, set_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
