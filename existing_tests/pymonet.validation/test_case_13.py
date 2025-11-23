import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 2839
        bool_0 = False
        validation_0 = module_0.Validation(int_0, bool_0)
        var_0 = validation_0.to_box()

if __name__ == "__main__":
    unittest.main()
