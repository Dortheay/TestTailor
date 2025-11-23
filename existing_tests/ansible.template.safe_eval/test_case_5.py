import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '_uses_shell'
        int_0 = 76
        str_1 = ''
        var_0 = module_0.safe_eval(str_1, str_0)
        float_0 = 1696.1
        set_0 = {str_0}
        bool_0 = True
        var_1 = module_0.safe_eval(set_0, bool_0)
        var_2 = module_0.safe_eval(str_0, int_0, float_0)

if __name__ == "__main__":
    unittest.main()
