import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()
        bool_0 = validation_result_0.__bool__()

if __name__ == "__main__":
    unittest.main()
