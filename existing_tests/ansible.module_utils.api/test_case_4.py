import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = 230.0
            bytes_0 = b'\xa3\x9b\xaf*5\x99\xf8h\xed>s\x95KZ\xa0\x1e\xf8\x7f'
            var_0 = module_0.rate_limit(bytes_0)
            var_1 = module_0.rate_limit_argument_spec(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
