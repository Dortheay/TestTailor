import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 156
            tuple_0 = ()
            set_0 = None
            bool_0 = True
            list_0 = [tuple_0, int_0, int_0, bool_0]
            validation_0 = module_0.Validation(bool_0, list_0)
            var_0 = validation_0.__eq__(set_0)
            list_1 = []
            validation_1 = module_0.Validation(tuple_0, list_1)
            float_0 = 306.4
            set_1 = {tuple_0, float_0, float_0}
            var_1 = validation_1.ap(set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
