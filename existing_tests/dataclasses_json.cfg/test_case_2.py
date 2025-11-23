import unittest
import timeout_decorator
import dataclasses_json.cfg as module_0

class Test_Cfg_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'Yq0|&( O3kjNH'
        bool_0 = False
        dict_0 = module_0.config(field_name=str_0, exclude=bool_0)
        exclude_0 = module_0.Exclude()

if __name__ == "__main__":
    unittest.main()
