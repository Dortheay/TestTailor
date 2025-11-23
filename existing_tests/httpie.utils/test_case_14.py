import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = 0.1
            var_0 = module_0.humanize_bytes(float_0)
            float_1 = -689.3147
            str_0 = '[WY|@'
            tuple_0 = (str_0, str_0)
            list_0 = [tuple_0]
            list_1 = module_0.get_expired_cookies(list_0, float_1)
            int_0 = 262
            var_1 = module_0.load_json_preserve_order(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
