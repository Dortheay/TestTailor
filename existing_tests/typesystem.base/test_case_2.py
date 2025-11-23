import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'range'
        message_0 = module_0.Message(text=str_0, key=str_0)
        list_0 = [message_0]
        parse_error_0 = module_0.ParseError(messages=list_0)

if __name__ == "__main__":
    unittest.main()
