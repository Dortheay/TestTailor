import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'D-'
            message_0 = module_0.Message(text=str_0)
            bool_0 = message_0.__eq__(message_0)
            str_1 = message_0.__repr__()
            parse_error_0 = module_0.ParseError(text=str_1, code=str_0)
            base_error_0 = module_0.BaseError(key=str_0, messages=str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
