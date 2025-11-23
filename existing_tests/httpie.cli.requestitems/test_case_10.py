import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'EPRe\x0b*xvWI)HsK'
            str_1 = '"8\nfW!_(&]Wr'
            str_2 = None
            str_3 = '|3'
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_2, str_1, str_3)
            str_4 = module_1.process_empty_header_arg(key_value_arg_0)
            optional_0 = module_1.process_header_arg(key_value_arg_0)
            str_5 = 'Ou('
            str_6 = None
            str_7 = '2H5a9aCi;'
            key_value_arg_1 = module_0.KeyValueArg(str_5, str_1, str_6, str_7)
            tuple_0 = module_1.process_file_upload_arg(key_value_arg_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
