import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = "Bnh>Wzc\x0cLJIU'O\x0b' "
            int_0 = 483
            int_1 = -1173
            position_0 = module_0.Position(int_0, int_1, int_0)
            message_0 = module_0.Message(text=str_0, position=position_0)
            bool_0 = message_0.__eq__(position_0)
            int_2 = -912
            int_3 = 4405
            int_4 = -353
            position_1 = module_0.Position(int_3, int_4, int_2)
            str_1 = message_0.__repr__()
            bool_1 = position_0.__eq__(position_1)
            bool_2 = message_0.__eq__(int_0)
            int_5 = message_0.__hash__()
            str_2 = 'e'
            parse_error_0 = module_0.ParseError(text=str_2, code=str_2, position=position_1)
            optional_0 = None
            validation_result_0 = module_0.ValidationResult(value=optional_0)
            iterator_0 = validation_result_0.__iter__()
            validation_error_0 = module_0.ValidationError(text=str_0, key=int_0, position=position_1)
            validation_result_1 = module_0.ValidationResult(value=iterator_0, error=validation_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
