import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'DH-'
            message_0 = module_0.Message(text=str_0, code=str_0)
            int_0 = 1458
            str_1 = message_0.__repr__()
            int_1 = -1283
            int_2 = 42
            position_0 = module_0.Position(int_1, int_2, int_0)
            bool_0 = position_0.__eq__(str_0)
            base_error_0 = module_0.BaseError(text=str_1, position=position_0)
            str_2 = base_error_0.__repr__()
            bool_1 = message_0.__eq__(message_0)
            int_3 = message_0.__hash__()
            list_0 = [message_0, message_0, message_0, message_0]
            base_error_1 = module_0.BaseError(code=str_2, position=position_0, messages=list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
