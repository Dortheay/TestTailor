import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = 'D-'
            message_0 = module_0.Message(text=str_0)
            bool_0 = message_0.__eq__(message_0)
            str_1 = message_0.__repr__()
            int_0 = message_0.__hash__()
            validation_result_0 = module_0.ValidationResult()
            iterator_0 = validation_result_0.__iter__()
            int_1 = 1
            int_2 = 1019
            int_3 = -1067
            position_0 = module_0.Position(int_1, int_2, int_3)
            str_2 = 'r\tL}o.=5'
            message_1 = module_0.Message(text=str_2, code=str_2, key=int_2, position=position_0, end_position=position_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
