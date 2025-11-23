import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            dict_0 = {}
            complex_0 = None
            str_0 = 'yzA24[ZVhJ-t_e9AatdT'
            str_1 = '!"ww)MPy<^(m-\'}/'
            str_2 = 'k)MTL`"$W7:4IWNbJZ'
            dict_1 = {str_0: str_1, str_2: dict_0, str_2: complex_0}
            var_0 = module_1.difference(dict_0, complex_0, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
