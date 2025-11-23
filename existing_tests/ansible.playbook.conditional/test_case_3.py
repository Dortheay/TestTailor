import unittest
import timeout_decorator
import ansible.playbook.conditional as module_0

class Test_Conditional_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            conditional_0 = module_0.Conditional(bool_0)
            bytes_0 = b'=u\x91\x94\xc7w\xc5$\x81\xcf\x9f\xb0)\x82'
            int_0 = 2472
            var_0 = conditional_0.evaluate_conditional(bytes_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
