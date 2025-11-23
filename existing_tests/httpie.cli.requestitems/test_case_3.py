import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'solarized'
            str_1 = ''
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
            str_2 = module_1.process_data_item_arg(key_value_arg_0)
            var_0 = key_value_arg_0.__repr__()
            tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
