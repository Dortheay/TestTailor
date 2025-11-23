import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            float_0 = 273.036
            dict_0 = {float_0: float_0}
            catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
            callable_0 = catch_all_undefined_parameters_0.create_init(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
