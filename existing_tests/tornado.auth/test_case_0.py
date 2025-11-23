import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            open_id_mixin_0 = module_0.OpenIdMixin()
            str_0 = 'V;+QR@F`\t/%S}fr_u9bS'
            open_id_mixin_0.authenticate_redirect(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
