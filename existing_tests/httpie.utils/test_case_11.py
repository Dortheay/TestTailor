import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = None
            str_1 = '%9-<A/^zvh_k5\n'
            list_0 = []
            list_1 = module_0.get_expired_cookies(list_0)
            dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1}
            list_2 = None
            list_3 = []
            explicit_null_auth_0 = module_0.ExplicitNullAuth(*list_3)
            var_0 = explicit_null_auth_0.__call__(dict_0)
            var_1 = module_0.humanize_bytes(list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
