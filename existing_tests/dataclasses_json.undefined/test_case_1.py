import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'?37'
            dict_0 = None
            catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters()
            dict_1 = catch_all_undefined_parameters_0.handle_from_dict(bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
