import unittest
import timeout_decorator
import dataclasses_json.cfg as module_0
import marshmallow.fields as module_1
import dataclasses_json.undefined as module_2

class Test_Cfg_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            exclude_0 = module_0.Exclude()
            dict_1 = module_0.config(mm_field=dict_0)
            exclude_1 = module_0.Exclude()
            dict_2 = {}
            var_0 = exclude_1.<lambda>(dict_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
