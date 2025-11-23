import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            open_id_mixin_0 = module_0.OpenIdMixin()
            open_id_mixin_0.authenticate_redirect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
