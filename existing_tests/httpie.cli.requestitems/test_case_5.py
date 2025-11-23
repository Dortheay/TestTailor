import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = "KY\rfQSuj+6 _2?JW\x0b'G`"
            str_1 = 'fU=*m~>cW'
            str_2 = 'qxoM.^{\r|Cm &]*t'
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_2)
            var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
