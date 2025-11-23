import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_54(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_43(self):
        str_0 = '{"name": "Peter"}'
        bool_0 = module_0.is_json(str_0)
        str_1 = '[1, 2, 3]'
        bool_1 = module_0.is_json(str_1)
        str_2 = '{nope}'
        bool_2 = module_0.is_json(str_2)
        str_3 = 'Hello World'
        bool_3 = module_0.is_json(str_3)
        str_4 = ''
        bool_4 = module_0.is_json(str_4)
        var_0 = None
        bool_5 = module_0.is_json(var_0)
        str_5 = ' '
        bool_6 = module_0.is_json(str_5)
        str_6 = '{"level1": {"level2": {"level3": "value"}}}'
        bool_7 = module_0.is_json(str_6)
        str_7 = '[{"key1": "value1"}, {"key2": "value2"}]'
        bool_8 = module_0.is_json(str_7)
        str_8 = ' {"key": "value"} '
        bool_9 = module_0.is_json(str_8)

if __name__ == "__main__":
    unittest.main()
