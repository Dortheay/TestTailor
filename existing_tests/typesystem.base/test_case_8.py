import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'q)B~G>"p<p'
        base_error_0 = module_0.BaseError(text=str_0, key=str_0)
        iterator_0 = base_error_0.__iter__()
        validation_result_0 = module_0.ValidationResult()
        str_1 = '$m <"!F'
        int_0 = 630
        int_1 = 6
        int_2 = 2493
        position_0 = module_0.Position(int_0, int_1, int_2)
        message_0 = module_0.Message(text=str_1, position=position_0)
        iterator_1 = validation_result_0.__iter__()
        int_3 = base_error_0.__hash__()

if __name__ == "__main__":
    unittest.main()
