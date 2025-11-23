import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        validation_result_0 = module_0.ValidationResult()

if __name__ == "__main__":
    unittest.main()
