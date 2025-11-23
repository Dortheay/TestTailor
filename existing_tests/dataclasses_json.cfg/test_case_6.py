import unittest
import timeout_decorator
import dataclasses_json.cfg as module_0
import marshmallow.fields as module_1
import dataclasses_json.undefined as module_2

class Test_Cfg_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            field_0 = module_1.Field(dump_only=bool_0)
            dict_0 = {field_0: field_0, field_0: bool_0, bool_0: field_0}
            undefined_0 = module_2.Undefined.INCLUDE
            str_0 = 'Missing '
            var_0 = field_0.get_value(undefined_0, str_0)
            dict_1 = module_0.config(dict_0, encoder=var_0, undefined=str_0, field_name=str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
