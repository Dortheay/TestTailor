import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'zK?Fez8z\\f_K'
        tuple_0 = (str_0,)
        dict_0 = {str_0: str_0, tuple_0: tuple_0}
        list_0 = [dict_0, tuple_0, str_0, tuple_0]
        list_1 = [list_0, tuple_0, list_0, list_0]
        var_0 = module_0.safe_eval(dict_0, list_0, list_1)
        dict_1 = None
        var_1 = module_0.safe_eval(dict_1, dict_1)
        var_2 = module_0.safe_eval(tuple_0)
        bool_0 = True
        int_0 = 179
        var_3 = module_0.safe_eval(bool_0, int_0)
        str_1 = 'nK>CYO?'
        bool_1 = False
        tuple_1 = (str_1, bool_1)
        complex_0 = None
        var_4 = module_0.safe_eval(complex_0)
        var_5 = module_0.safe_eval(tuple_1)

if __name__ == "__main__":
    unittest.main()
