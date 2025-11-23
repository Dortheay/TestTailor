import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            o_auth2_mixin_0 = module_0.OAuth2Mixin()
            google_o_auth2_mixin_0 = module_0.GoogleOAuth2Mixin()
            str_0 = 'otO{>&dL"</S#hepu7Bz'
            str_1 = '\x0c6=IJ2on]f)'
            dict_0 = google_o_auth2_mixin_0.get_authenticated_user(str_0, str_1)
            async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
