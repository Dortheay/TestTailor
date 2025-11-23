import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '`&?\x0b99b"cSW$L'
            tuple_0 = module_0.parse_host(str_0)
            str_1 = '7mj,:@J[|A'
            str_2 = module_0.fwd_normalize_address(str_1)
            int_0 = 25
            tuple_1 = module_0.parse_host(str_1)
            set_0 = {str_2, int_0, str_1}
            bytes_0 = module_0.format_http1_response(int_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
