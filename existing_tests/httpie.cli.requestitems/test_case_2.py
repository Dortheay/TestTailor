import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "c7&%R~r$**ED'Dcm!)"
            key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
            tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
