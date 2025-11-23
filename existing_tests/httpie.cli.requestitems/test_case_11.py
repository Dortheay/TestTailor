import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = None
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
            optional_0 = module_1.process_header_arg(key_value_arg_0)
            var_0 = key_value_arg_0.__eq__(key_value_arg_0)
            bool_0 = True
            request_items_0 = module_1.RequestItems(bool_0)
            str_1 = 'Ou('
            key_value_arg_1 = module_0.KeyValueArg(str_1, str_1, str_1, str_1)
            tuple_0 = module_1.process_file_upload_arg(key_value_arg_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
