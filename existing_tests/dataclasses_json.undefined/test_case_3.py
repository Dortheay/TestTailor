import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
            bool_0 = True
            dict_0 = None
            str_0 = '<\\38^\x0c%bpZ}s>'
            str_1 = 'p~'
            dict_1 = {str_0: dict_0, str_1: ignore_undefined_parameters_0}
            dict_2 = {bool_0: dict_1}
            dict_3 = ignore_undefined_parameters_0.handle_from_dict(dict_0, dict_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
