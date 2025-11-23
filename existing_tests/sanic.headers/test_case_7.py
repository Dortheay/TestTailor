import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '; '
            tuple_0 = module_0.parse_content_header(str_0)
            str_1 = 'H0so'
            str_2 = module_0.fwd_normalize_address(str_1)
            tuple_1 = ()
            dict_0 = module_0.fwd_normalize(tuple_1)
            tuple_2 = module_0.parse_host(str_1)
            dict_1 = module_0.fwd_normalize(tuple_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
