import unittest
import timeout_decorator
import tornado.auth as module_0

class Test_Auth_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        open_id_mixin_0 = module_0.OpenIdMixin()

if __name__ == "__main__":
    unittest.main()
