import unittest
import timeout_decorator
import httpie.cli.requestitems as module_0
import httpie.cli.argtypes as module_1

class Test_Requestitems_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '9j'
        key_value_arg_0 = module_1.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_0.process_header_arg(key_value_arg_0)

if __name__ == "__main__":
    unittest.main()
