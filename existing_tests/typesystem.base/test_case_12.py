import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 4
            int_1 = -3034
            position_0 = module_0.Position(int_0, int_1, int_0)
            base_error_0 = module_0.BaseError(text=position_0)
            str_0 = base_error_0.__repr__()
            str_1 = 'vdFwg'
            base_error_1 = module_0.BaseError(position=str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
