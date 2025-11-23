import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '^'
            set_0 = {str_0, str_0}
            list_0 = [set_0]
            dict_0 = {}
            str_1 = ''
            validation_0 = module_0.Validation(dict_0, str_1)
            var_0 = validation_0.bind(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
