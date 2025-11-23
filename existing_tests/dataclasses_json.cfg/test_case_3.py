import unittest
import timeout_decorator
import dataclasses_json.cfg as module_0

class Test_Cfg_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'Cising '
        callable_0 = None
        int_0 = -1549
        dict_0 = module_0.config(decoder=callable_0, letter_case=int_0, field_name=str_0)

if __name__ == "__main__":
    unittest.main()
