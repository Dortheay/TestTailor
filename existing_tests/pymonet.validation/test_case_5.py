import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            dict_0 = {}
            validation_0 = module_0.Validation(dict_0, dict_0)
            var_0 = validation_0.to_either()
            int_0 = False
            set_0 = {int_0, int_0}
            validation_1 = module_0.Validation(int_0, set_0)
            str_0 = '7#AgJ3+\\Q5I@|>GM'
            var_1 = validation_1.bind(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
