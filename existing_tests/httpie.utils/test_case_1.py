import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        list_0 = []
        float_0 = None
        list_1 = module_0.get_expired_cookies(list_0)
        list_2 = module_0.get_expired_cookies(list_0, float_0)
        explicit_null_auth_0 = module_0.ExplicitNullAuth()
        dict_0 = {}
        str_0 = module_0.repr_dict(dict_0)

if __name__ == "__main__":
    unittest.main()
