import unittest
import timeout_decorator
import ansible.modules.expect as module_0

class Test_Expect_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 3184.5835
        int_0 = -815
        str_0 = 'ansible.modules.expect'
        var_0 = module_0.response_closure(float_0, int_0, str_0)

if __name__ == "__main__":
    unittest.main()
