import unittest
import timeout_decorator
import httpie.output.formatters.headers as module_0

class Test_Headers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'format_options'
        str_1 = 'headers'
        str_2 = 'sort'
        bool_0 = True
        bool_1 = {str_2: bool_0}
        bool_2 = {str_1: bool_1}
        bool_3 = {str_0: bool_2}
        headers_formatter_0 = module_0.HeadersFormatter(**bool_3)
        str_3 = headers_formatter_0.format_headers(str_1)

if __name__ == "__main__":
    unittest.main()
