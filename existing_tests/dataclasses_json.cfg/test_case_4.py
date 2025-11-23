import unittest
import timeout_decorator
import dataclasses_json.cfg as module_0
import marshmallow.fields as module_1
import dataclasses_json.undefined as module_2

class Test_Cfg_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'Missng n='
            dict_0 = module_0.config(decoder=str_0, undefined=str_0, field_name=str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
