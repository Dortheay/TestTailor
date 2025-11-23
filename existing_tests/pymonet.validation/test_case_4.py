import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = True
            tuple_0 = ()
            set_0 = {bool_0, tuple_0}
            str_0 = '3$^yA'
            validation_0 = module_0.Validation(set_0, str_0)
            var_0 = validation_0.to_either()
            str_1 = "=%)&StpU[x</:<['[NA"
            str_2 = 'All[value={}]'
            bool_1 = False
            validation_1 = module_0.Validation(str_2, bool_1)
            var_1 = validation_1.bind(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
