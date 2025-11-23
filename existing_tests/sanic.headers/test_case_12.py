import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'wv\\uC}nGu`SNK'
        tuple_0 = module_0.parse_host(str_0)

if __name__ == "__main__":
    unittest.main()
