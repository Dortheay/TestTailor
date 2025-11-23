import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = 'q)B~G>"p<p'
            base_error_0 = module_0.BaseError(text=str_0, key=str_0)
            iterator_0 = base_error_0.__iter__()
            validation_result_0 = module_0.ValidationResult()
            int_0 = 0
            int_1 = 1353
            position_0 = module_0.Position(int_0, int_1, int_1)
            message_0 = module_0.Message(text=str_0, position=position_0, start_position=position_0, end_position=position_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
