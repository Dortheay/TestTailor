import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            list_0 = []
            bytes_0 = b'X'
            catch_all_undefined_parameters_0 = module_0._CatchAllUndefinedParameters(*list_0)
            dict_0 = catch_all_undefined_parameters_0.handle_dump(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
