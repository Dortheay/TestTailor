import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = 0.5
        var_0 = module_0.safe_eval(float_0)

if __name__ == "__main__":
    unittest.main()
