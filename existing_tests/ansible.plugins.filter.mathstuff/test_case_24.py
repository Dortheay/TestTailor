import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            float_0 = None
            str_0 = 'Ph'
            int_0 = -2223
            str_1 = 'IB%C?|Z>vP'
            str_2 = '\tps6Tg^iZ()w|\t'
            dict_0 = {str_0: int_0, str_1: str_0, str_2: int_0, str_1: str_2}
            var_0 = module_1.symmetric_difference(float_0, str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
