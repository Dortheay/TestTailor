import unittest
import timeout_decorator
import ansible.template.safe_eval as module_0

class Test_Safe_eval_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'r<ZXq#s'
        var_0 = module_0.safe_eval(str_0)

if __name__ == "__main__":
    unittest.main()
