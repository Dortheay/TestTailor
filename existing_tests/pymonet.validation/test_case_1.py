import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -2577
            list_0 = [int_0, int_0, int_0, int_0]
            int_1 = 1122
            bool_0 = False
            validation_0 = module_0.Validation(int_1, bool_0)
            var_0 = validation_0.map(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
