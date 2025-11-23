import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'sdF=4p&Irc37ihh?)'
            validation_result_0 = module_0.ValidationResult()
            bool_0 = validation_result_0.__bool__()
            message_0 = module_0.Message(text=str_0, key=str_0)
            int_0 = -2940
            position_0 = module_0.Position(int_0, int_0, int_0)
            str_1 = validation_result_0.__repr__()
            list_0 = [message_0, message_0, message_0]
            base_error_0 = module_0.BaseError(text=str_0)
            str_2 = base_error_0.__str__()
            str_3 = position_0.__repr__()
            validation_error_0 = module_0.ValidationError(text=message_0, key=str_0, position=position_0, messages=list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
