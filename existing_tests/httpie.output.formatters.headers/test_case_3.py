import unittest
import timeout_decorator
import httpie.output.formatters.headers as module_0

class Test_Headers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'format_options'
            str_1 = 'headers'
            str_2 = 'sort'
            bool_0 = False
            bool_1 = {str_2: bool_0}
            bool_2 = {str_1: bool_1}
            dict_0 = {str_0: bool_1, str_0: bool_2}
            str_3 = 'G\r7J]fd><\t=)jz'
            headers_formatter_0 = module_0.HeadersFormatter(**dict_0)
            str_4 = headers_formatter_0.format_headers(str_3)
            headers_formatter_1 = module_0.HeadersFormatter()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
