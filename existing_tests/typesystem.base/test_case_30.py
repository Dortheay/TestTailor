import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            str_0 = 'q)B~G>"p<p'
            base_error_0 = module_0.BaseError(text=str_0, key=str_0)
            iterator_0 = base_error_0.__iter__()
            str_1 = 'sFe3R0R{u'
            list_0 = []
            int_0 = 1639
            int_1 = -1401
            int_2 = 4
            position_0 = module_0.Position(int_0, int_1, int_2)
            message_0 = module_0.Message(text=str_1, key=str_0, index=list_0, position=position_0, start_position=position_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
