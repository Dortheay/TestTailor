import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            validation_result_0 = module_0.ValidationResult()
            str_0 = validation_result_0.__repr__()
            int_0 = 1731
            int_1 = 4739
            bool_0 = validation_result_0.__bool__()
            str_1 = validation_result_0.__repr__()
            position_0 = module_0.Position(int_0, int_1, int_0)
            base_error_0 = module_0.BaseError(text=str_0, code=str_0, key=str_0, position=position_0)
            bool_1 = position_0.__eq__(bool_0)
            bool_2 = base_error_0.__eq__(int_0)
            var_0 = base_error_0.__getitem__(validation_result_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
