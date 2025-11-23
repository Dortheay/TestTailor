import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        explicit_null_auth_0 = module_0.ExplicitNullAuth()

if __name__ == "__main__":
    unittest.main()
