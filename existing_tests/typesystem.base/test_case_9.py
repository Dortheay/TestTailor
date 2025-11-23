import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'Single error message'
        str_1 = 'error_code'
        message_0 = module_0.Message(text=str_0, code=str_1)
        message_1 = [message_0]
        base_error_0 = module_0.BaseError(messages=message_1)
        var_0 = str(base_error_0)
        str_2 = 'Error 1'
        str_3 = 'code1'
        str_4 = 'field1'
        str_5 = [str_4]
        message_2 = module_0.Message(text=str_2, code=str_3, index=str_5)
        str_6 = 'Error 2'
        str_7 = 'code2'
        str_8 = 'field2'
        str_9 = [str_8]
        message_3 = module_0.Message(text=str_6, code=str_7, index=str_9)
        message_4 = [message_2, message_3]
        base_error_1 = module_0.BaseError(messages=message_4)
        str_10 = {str_4: str_2, str_8: str_6}
        var_1 = str(str_10)
        var_2 = str(base_error_1)
        str_11 = 'Nested error 1'
        str_12 = 'parent'
        str_13 = 'child1'
        str_14 = [str_12, str_13]
        message_5 = module_0.Message(text=str_11, code=str_3, index=str_14)
        str_15 = 'Nested error 2'
        str_16 = 'child2'
        str_17 = [str_12, str_16]
        message_6 = module_0.Message(text=str_15, code=str_7, index=str_17)
        message_7 = [message_5, message_6]
        base_error_2 = module_0.BaseError(messages=message_7)
        str_18 = {str_13: str_11, str_16: str_15}
        str_19 = {str_12: str_18}
        var_3 = str(str_19)
        var_4 = str(base_error_2)

if __name__ == "__main__":
    unittest.main()
