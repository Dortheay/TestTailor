import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -912
        int_1 = -33
        position_0 = module_0.Position(int_0, int_1, int_0)
        bool_0 = position_0.__eq__(position_0)
        validation_result_0 = module_0.ValidationResult()
        iterator_0 = validation_result_0.__iter__()

if __name__ == "__main__":
    unittest.main()
