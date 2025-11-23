import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            raise_undefined_parameters_0 = module_0._RaiseUndefinedParameters()
            str_0 = 'FS@'
            dict_0 = {str_0: raise_undefined_parameters_0}
            str_1 = 'V\t O0q+4o[*\t&7us[ncP'
            dict_1 = raise_undefined_parameters_0.handle_from_dict(str_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
