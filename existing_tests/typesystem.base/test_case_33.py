import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = '[t"!x[TcKLI[\x0b/;ri'
            list_0 = [str_0, str_0, str_0]
            position_0 = None
            message_0 = module_0.Message(text=str_0, index=list_0, start_position=position_0)
            position_1 = None
            str_1 = 'tzinfo'
            message_1 = module_0.Message(text=str_1, key=str_1, start_position=position_1, end_position=position_0)
            list_1 = [message_1, message_1, message_0]
            base_error_0 = module_0.BaseError(position=position_1, messages=list_1)
            parse_error_0 = None
            bool_0 = message_1.__eq__(parse_error_0)
            int_0 = 1742
            position_2 = module_0.Position(int_0, int_0, int_0)
            bool_1 = position_2.__eq__(base_error_0)
            str_2 = 'Q-hZ}>]6DS68a}D'
            int_1 = message_0.__hash__()
            float_0 = -1077.0807
            message_2 = module_0.Message(text=str_2, key=str_2)
            list_2 = [message_2]
            base_error_1 = module_0.BaseError(key=str_2, position=float_0, messages=list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
