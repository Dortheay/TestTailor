import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = '5+\nw7n.fAF`*B\\b>{LC'
            validation_error_0 = module_0.ValidationError(text=str_0, code=str_0)
            validation_result_0 = module_0.ValidationResult(value=validation_error_0)
            str_1 = 'hG0a"PY,%'
            validation_error_1 = module_0.ValidationError(text=validation_result_0, code=str_0, key=str_1)
            int_0 = 234
            list_0 = []
            base_error_0 = module_0.BaseError(key=int_0, position=list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
