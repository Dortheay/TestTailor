import unittest
import timeout_decorator
import dataclasses_json.cfg as module_0

class Test_Cfg_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        optional_0 = None
        dict_0 = module_0.config(letter_case=optional_0)

if __name__ == "__main__":
    unittest.main()
