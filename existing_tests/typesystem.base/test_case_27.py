import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            int_0 = -1222
            int_1 = 1000
            int_2 = -494
            int_3 = -3409
            position_0 = module_0.Position(int_2, int_1, int_3)
            int_4 = 544
            position_1 = module_0.Position(int_1, int_1, int_4)
            int_5 = -28
            int_6 = -1914
            position_2 = module_0.Position(int_5, int_0, int_6)
            str_0 = 'label'
            bool_0 = position_2.__eq__(position_1)
            validation_error_0 = module_0.ValidationError(text=str_0)
            validation_result_0 = module_0.ValidationResult(error=validation_error_0)
            str_1 = validation_result_0.__repr__()
            validation_error_1 = module_0.ValidationError(code=str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
