import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        dict_0 = None
        str_0 = 'LT)Rygf'
        dict_1 = {str_0: dict_0, dict_0: dict_0}
        set_0 = None
        retry_0 = module_1.Retry(dict_0, str_0, dict_1, set_0, set_0)
        int_0 = 494
        logged_function_0 = module_0.LoggedFunction(int_0)
        var_0 = logged_function_0.__call__(retry_0)
        int_1 = None
        var_1 = module_0.format_arg(int_1)
        tuple_0 = ()
        var_2 = module_0.format_arg(tuple_0)

if __name__ == "__main__":
    unittest.main()
