import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'key'
            str_1 = '{"key1": "value1"}'
            str_2 = ':'
            str_3 = 'key:json_data'
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_1, str_2, str_3)
            str_4 = '{invalid_json}'
            str_5 = 'key:invalid_json'
            key_value_arg_1 = module_0.KeyValueArg(str_0, str_4, str_2, str_5)
            var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
            var_1 = module_1.process_data_raw_json_embed_arg(key_value_arg_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
