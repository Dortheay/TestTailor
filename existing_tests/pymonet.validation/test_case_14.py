import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bool_0 = False
        validation_0 = module_0.Validation(bool_0, bool_0)
        var_0 = validation_0.to_lazy()

if __name__ == "__main__":
    unittest.main()
