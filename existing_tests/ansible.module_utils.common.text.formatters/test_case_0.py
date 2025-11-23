import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 1000.0
            var_0 = module_0.lenient_lowercase(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
