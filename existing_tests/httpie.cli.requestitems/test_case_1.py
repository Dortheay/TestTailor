import unittest
import timeout_decorator
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

class Test_Requestitems_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            key_value_arg_0 = None
            str_0 = module_1.process_query_param_arg(key_value_arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
