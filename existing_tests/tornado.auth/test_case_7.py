import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            open_id_mixin_0 = module_0.OpenIdMixin()
            dict_0 = {}
            list_0 = []
            o_auth2_mixin_0 = module_0.OAuth2Mixin(*list_0, **dict_0)
            o_auth2_mixin_0.authorize_redirect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
