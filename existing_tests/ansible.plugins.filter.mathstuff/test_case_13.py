import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            dict_0 = None
            float_0 = 316.20055
            str_0 = 'srVg!'
            var_0 = module_1.symmetric_difference(dict_0, float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
