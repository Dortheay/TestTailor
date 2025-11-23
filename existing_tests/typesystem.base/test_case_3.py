import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'gQj0_\rOCmM.\r%Ys'
        list_0 = [str_0, str_0]
        message_0 = module_0.Message(text=str_0, index=list_0, position=str_0)
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()

if __name__ == "__main__":
    unittest.main()
