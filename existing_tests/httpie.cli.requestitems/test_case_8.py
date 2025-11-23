import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '\n    The desired protocol version to use. This will default to\n    SSL v2.3 which will negotiate the highest protocol that both\n    the server and your installation of OpenSSL support. Available protocols\n    may vary depending on OpenSSL installation (only the supported ones\n    are shown here).\n\n    '
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
            bool_0 = True
            request_items_0 = module_1.RequestItems(bool_0)
            str_1 = 'Ou('
            key_value_arg_1 = module_0.KeyValueArg(str_1, str_1, str_1, str_1)
            tuple_0 = module_1.process_file_upload_arg(key_value_arg_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
