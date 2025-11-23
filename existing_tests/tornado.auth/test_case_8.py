import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            open_id_mixin_0 = module_0.OpenIdMixin()
            str_0 = 'V;+QR@F`\t/%S}f|_u9bS'
            list_0 = []
            o_auth2_mixin_0 = module_0.OAuth2Mixin(*list_0)
            str_1 = 'G|+p2J, SRdu6QCfA'
            none_type_0 = None
            str_2 = '%"&il09+iM3O\r\ns'
            o_auth2_mixin_0.authorize_redirect(str_0, str_1, str_0, none_type_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
