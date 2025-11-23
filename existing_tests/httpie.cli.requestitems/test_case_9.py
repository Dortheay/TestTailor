import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = None
            str_1 = '^-A'
            str_2 = "(ES\\Q/'s}G"
            key_value_arg_0 = module_0.KeyValueArg(str_1, str_0, str_2, str_2)
            var_0 = key_value_arg_0.__repr__()
            var_1 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
