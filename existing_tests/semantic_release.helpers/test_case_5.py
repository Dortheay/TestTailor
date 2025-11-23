import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = None
        int_0 = 3649
        bool_0 = False
        bytes_0 = b'\x15\xe6\xa6\rq{Jp\xc7\xae\xe9\xf1\xd8'
        logged_function_0 = module_0.LoggedFunction(bytes_0)
        retry_0 = module_1.Retry(int_0, bool_0, logged_function_0, bytes_0, bytes_0, str_0)
        session_0 = module_0.build_requests_session(str_0, retry_0)
        int_1 = 1287
        session_1 = module_0.build_requests_session(int_1)
        int_2 = 404
        bool_1 = True
        str_1 = '\nW+Zb-6*7u['
        var_0 = module_0.format_arg(str_1)
        logged_function_1 = module_0.LoggedFunction(bool_1)
        var_1 = logged_function_1.__call__(int_2)
        logged_function_2 = module_0.LoggedFunction(int_1)
        str_2 = ';fTzB>Mk?A:(3C'
        logged_function_3 = module_0.LoggedFunction(str_2)
        bool_2 = False
        dict_0 = {}
        tuple_0 = (bool_2, dict_0, logged_function_2)
        var_2 = logged_function_2.__call__(tuple_0)
        bytes_1 = b'tk\xf8x\xaev*\x9a\x1d\xa8\x9ed'
        var_3 = module_0.format_arg(bytes_1)
        complex_0 = None
        var_4 = module_0.format_arg(complex_0)

if __name__ == "__main__":
    unittest.main()
