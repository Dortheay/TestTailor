import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'key'
        str_1 = 'value'
        str_2 = {str_0: str_1}
        validation_result_0 = module_0.ValidationResult(value=str_2)
        var_0 = list(validation_result_0)
        str_3 = 'An error occurred'
        validation_error_0 = module_0.ValidationError(text=str_3)
        validation_result_1 = module_0.ValidationResult(error=validation_error_0)
        var_1 = list(validation_result_1)

if __name__ == "__main__":
    unittest.main()
