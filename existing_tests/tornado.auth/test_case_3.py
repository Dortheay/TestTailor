import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            open_id_mixin_0 = module_0.OpenIdMixin()
            str_0 = 'V;+QR@F`\t/%S}fr_u9bS'
            o_auth2_mixin_0 = module_0.OAuth2Mixin()
            o_auth2_mixin_0.authorize_redirect(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
