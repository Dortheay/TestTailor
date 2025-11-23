import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            ignore_undefined_parameters_0 = module_0._IgnoreUndefinedParameters()
            bytes_0 = b'\x01\xd0\xf3\x04\xd6\xf1D\xf783\x18'
            callable_0 = ignore_undefined_parameters_0.create_init(bytes_0)
            str_0 = '7Jpu'
            callable_1 = ignore_undefined_parameters_0.create_init(str_0)
            list_0 = [callable_0, callable_1]
            dict_0 = {str_0: list_0}
            undefined_parameter_action_0 = module_0._UndefinedParameterAction(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
