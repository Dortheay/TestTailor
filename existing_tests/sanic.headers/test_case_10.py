import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'IYSiai~{@3/kS'
        tuple_0 = module_0.parse_content_header(str_0)

if __name__ == "__main__":
    unittest.main()
