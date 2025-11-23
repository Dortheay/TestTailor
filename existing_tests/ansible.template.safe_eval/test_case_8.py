import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '1 + 2'
        var_0 = module_0.safe_eval(str_0)
        var_1 = module_0.safe_eval(str_0)
        bool_0 = False
        var_2 = module_0.safe_eval(bool_0)

if __name__ == "__main__":
    unittest.main()
