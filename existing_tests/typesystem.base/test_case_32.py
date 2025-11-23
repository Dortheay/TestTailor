import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            str_0 = 'D-'
            message_0 = module_0.Message(text=str_0)
            bool_0 = message_0.__eq__(str_0)
            bool_1 = message_0.__eq__(message_0)
            str_1 = message_0.__repr__()
            message_1 = module_0.Message(text=str_1, key=str_0)
            bool_2 = message_1.__eq__(message_0)
            int_0 = message_1.__hash__()
            int_1 = 1755
            int_2 = None
            int_3 = 1900
            position_0 = module_0.Position(int_1, int_2, int_3)
            parse_error_0 = module_0.ParseError(key=str_1, position=position_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
