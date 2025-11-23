import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = -2042
            bool_0 = True
            str_0 = '%xB{Ppt'
            validation_0 = module_0.Validation(bool_0, str_0)
            var_0 = validation_0.to_try()
            int_1 = False
            var_1 = validation_0.to_lazy()
            var_2 = validation_0.to_lazy()
            dict_0 = {}
            validation_1 = module_0.Validation(int_0, dict_0)
            var_3 = validation_1.to_maybe()
            str_1 = "'"
            bool_1 = True
            validation_2 = module_0.Validation(int_1, int_1)
            tuple_0 = (bool_1, validation_2, bool_1)
            validation_3 = module_0.Validation(str_1, tuple_0)
            var_4 = validation_3.__str__()
            var_5 = validation_0.map(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
