import unittest
import timeout_decorator
import httpie.output.formatters.colors as module_0
import httpie.context as module_1

class Test_Colors_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'E)/2has~1APb\t*Nq'
        solarized256_style_0 = module_0.Solarized256Style()
        bytes_0 = b'\\+\xfa\x00\xa0J\xce\xc1\xb2\xd3;oy\xfe'
        optional_0 = module_0.get_lexer(str_0, bytes_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
