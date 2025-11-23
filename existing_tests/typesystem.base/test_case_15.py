import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -35
            str_0 = 'invalgd_\x0cd=\ruey'
            list_0 = []
            message_0 = module_0.Message(text=str_0, key=int_0, start_position=list_0)
            list_1 = [message_0]
            base_error_0 = module_0.BaseError(messages=list_1)
            str_1 = base_error_0.__repr__()
            int_1 = -2346
            position_0 = module_0.Position(int_1, int_0, int_1)
            str_2 = '.'
            message_1 = module_0.Message(text=str_2, start_position=position_0)
            list_2 = [message_1, message_1]
            base_error_1 = module_0.BaseError(position=position_0, messages=list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
