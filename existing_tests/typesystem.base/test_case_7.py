import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'sdF=4p&Irc37ihh?)'
        validation_result_0 = module_0.ValidationResult()
        bool_0 = validation_result_0.__bool__()
        int_0 = -2940
        position_0 = module_0.Position(int_0, int_0, int_0)
        str_1 = validation_result_0.__repr__()
        base_error_0 = module_0.BaseError(text=str_0)
        str_2 = base_error_0.__str__()
        str_3 = position_0.__repr__()

if __name__ == "__main__":
    unittest.main()
