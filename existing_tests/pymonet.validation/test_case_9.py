import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = True
        validation_0 = module_0.Validation(bool_0, bool_0)

if __name__ == "__main__":
    unittest.main()
