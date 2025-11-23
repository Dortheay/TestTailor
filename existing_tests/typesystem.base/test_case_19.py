import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'H-'
            message_0 = module_0.Message(text=str_0)
            bool_0 = message_0.__eq__(str_0)
            bool_1 = message_0.__eq__(message_0)
            str_1 = message_0.__repr__()
            parse_error_0 = module_0.ParseError(text=str_1, code=str_0)
            base_error_0 = module_0.BaseError(text=str_1)
            int_0 = base_error_0.__len__()
            validation_result_0 = module_0.ValidationResult()
            iterator_0 = validation_result_0.__iter__()
            tuple_0 = ()
            base_error_1 = module_0.BaseError(text=str_0, code=str_1, key=str_1, messages=tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
