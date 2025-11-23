import unittest
import timeout_decorator
import dataclasses_json.mm as module_0

class Test_Mm_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'Sfb3\x0b'
            dict_0 = {str_0: str_0}
            dict_1 = {str_0: str_0, str_0: str_0}
            float_0 = 1464.4448830959911
            var_0 = module_0.build_type(str_0, dict_0, dict_1, str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
