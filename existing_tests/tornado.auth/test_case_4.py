import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'V;+QR@F`\t/%S}f|_u9bS'
            dict_0 = {}
            o_auth2_mixin_0 = module_0.OAuth2Mixin(**dict_0)
            o_auth2_mixin_0.authorize_redirect(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
