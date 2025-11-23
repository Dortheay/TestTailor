import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'DH-'
            message_0 = module_0.Message(text=str_0)
            int_0 = -912
            int_1 = -33
            position_0 = module_0.Position(int_0, int_1, int_0)
            str_1 = message_0.__repr__()
            bool_0 = message_0.__eq__(message_0)
            str_2 = message_0.__repr__()
            bool_1 = position_0.__eq__(position_0)
            int_2 = message_0.__hash__()
            parse_error_0 = module_0.ParseError(text=str_2, code=str_0)
            validation_result_0 = module_0.ValidationResult()
            iterator_0 = validation_result_0.__iter__()
            list_0 = None
            validation_error_0 = module_0.ValidationError(text=str_1, key=str_2, messages=list_0)
            base_error_0 = module_0.BaseError(position=position_0, messages=validation_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
