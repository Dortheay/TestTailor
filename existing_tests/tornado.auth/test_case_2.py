import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            o_auth_mixin_0 = module_0.OAuthMixin()
            async_h_t_t_p_client_0 = o_auth_mixin_0.get_auth_http_client()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
