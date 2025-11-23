import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            open_id_mixin_0 = module_0.OpenIdMixin()
            str_0 = 'V;+QRbF`\t/%S}fr]u9b]'
            dict_0 = {}
            o_auth2_mixin_0 = module_0.OAuth2Mixin(**dict_0)
            async_h_t_t_p_client_0 = None
            o_auth_mixin_0 = module_0.OAuthMixin()
            dict_1 = o_auth_mixin_0.get_authenticated_user(async_h_t_t_p_client_0)
            o_auth2_mixin_1 = module_0.OAuth2Mixin()
            o_auth2_mixin_0.authorize_redirect(str_0, str_0, dict_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
