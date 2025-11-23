import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = ';*I$`-qG'
            tuple_0 = module_0.parse_content_header(str_0)
            bytes_0 = b'\xe3R\xd3\xf9\x84\xa5U\xce\xca\xfb?\xc4\xdcd\x9a\xfa\xfa\x10\x17'
            bool_0 = True
            optional_0 = module_0.parse_forwarded(bytes_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
