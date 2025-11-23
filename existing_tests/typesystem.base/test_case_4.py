import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '%?!9P\\L=+'
        parse_error_0 = module_0.ParseError(text=str_0)
        str_1 = 'gQj0_\rOCmM.\r%Ys'
        list_0 = [str_1, str_0]
        message_0 = module_0.Message(text=str_0, index=list_0, position=str_1)
        dict_0 = {str_1: str_0, str_1: parse_error_0, parse_error_0: str_0, parse_error_0: str_0}
        message_1 = module_0.Message(text=str_1, start_position=dict_0)

if __name__ == "__main__":
    unittest.main()
