import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = ''
        var_0 = module_0.safe_eval(str_0)

if __name__ == "__main__":
    unittest.main()
