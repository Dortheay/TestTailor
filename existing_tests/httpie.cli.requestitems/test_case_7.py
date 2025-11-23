import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '\x0bWwV-rPF-$'
            str_1 = '@'
            str_2 = 'format'
            key_value_arg_0 = module_0.KeyValueArg(str_1, str_1, str_2, str_0)
            str_3 = module_1.process_data_item_arg(key_value_arg_0)
            request_items_0 = module_1.RequestItems()
            str_4 = 'Tz?O('
            str_5 = None
            str_6 = 'g"KTFAe'
            key_value_arg_1 = module_0.KeyValueArg(str_0, str_3, str_4, str_6)
            str_7 = '0x0<%lZ?\x0c_7y9qonU'
            key_value_arg_2 = module_0.KeyValueArg(str_7, str_7, str_6, str_1)
            str_8 = '+6;/'
            key_value_arg_3 = module_0.KeyValueArg(str_7, str_5, str_4, str_8)
            str_9 = module_1.process_data_embed_file_contents_arg(key_value_arg_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
