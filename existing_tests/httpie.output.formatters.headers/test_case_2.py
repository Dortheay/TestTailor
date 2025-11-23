import unittest
import timeout_decorator
import httpie.output.formatters.headers as module_0

class Test_Headers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            headers_formatter_0 = module_0.HeadersFormatter()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
