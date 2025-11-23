import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 2426
            position_0 = module_0.Position(int_0, int_0, int_0)
            base_error_0 = module_0.BaseError(position=position_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
