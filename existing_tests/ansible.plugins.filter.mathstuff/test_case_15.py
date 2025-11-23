import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            dict_0 = None
            float_0 = 1.0
            var_0 = module_1.min(dict_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
