import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\r\xd1\xa7\x9f'
            dict_0 = module_0.parse_qs_bytes(bytes_0)
            bytes_1 = b'\xac\x13\x17Y\xb3\xefZ\xa2\x94'
            str_0 = ')$%C*?\x0cXyP~.>VQ\x0b#-'
            str_1 = module_0.squeeze(str_0)
            str_2 = module_0.xhtml_escape(bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
