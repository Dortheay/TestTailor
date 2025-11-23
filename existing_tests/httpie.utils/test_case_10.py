import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            explicit_null_auth_0 = module_0.ExplicitNullAuth()
            var_0 = module_0.humanize_bytes(explicit_null_auth_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
