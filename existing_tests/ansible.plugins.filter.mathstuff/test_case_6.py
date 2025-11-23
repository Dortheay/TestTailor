import unittest
import timeout_decorator
import ansible.plugins.filter.mathstuff as module_0

class Test_Mathstuff_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        dict_0 = {}
        complex_0 = None
        str_0 = '!"ww)MPy<^(m-\'}/'
        str_1 = ',7'
        dict_1 = {str_0: str_0, str_1: dict_0, str_1: complex_0}
        str_2 = 'FAILED_TASKS'
        int_0 = 774
        list_0 = [str_1]
        dict_2 = {str_2: complex_0, int_0: dict_1}
        int_1 = None
        tuple_0 = (dict_2, list_0, int_1)
        var_0 = module_0.intersect(list_0, dict_1, tuple_0)

if __name__ == "__main__":
    unittest.main()
