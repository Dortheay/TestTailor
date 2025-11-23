import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'max_length'
        int_0 = 1731
        int_1 = 4739
        int_2 = -186
        position_0 = module_0.Position(int_0, int_1, int_2)
        base_error_0 = module_0.BaseError(text=str_0, code=str_0, key=str_0, position=position_0)
        bool_0 = base_error_0.__eq__(int_2)

if __name__ == "__main__":
    unittest.main()
