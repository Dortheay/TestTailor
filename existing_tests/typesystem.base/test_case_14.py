import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'NS1^'
            str_1 = 'f'
            str_2 = "'\n^}+Q%l]T'Z~*4"
            str_3 = 'Bf\x0cKxKL4\n'
            list_0 = [str_0, str_3]
            int_0 = -657
            position_0 = module_0.Position(int_0, int_0, int_0)
            str_4 = position_0.__repr__()
            int_1 = 4
            message_0 = module_0.Message(text=str_3, index=list_0, position=int_1)
            message_1 = module_0.Message(text=str_2, key=str_0, position=message_0)
            str_5 = message_0.__repr__()
            int_2 = message_0.__hash__()
            int_3 = 2430
            message_2 = module_0.Message(text=str_0, code=str_1, index=message_1, start_position=int_3)
            int_4 = message_2.__hash__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
