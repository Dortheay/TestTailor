import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'i2Yd'
        tuple_0 = module_0.parse_host(str_0)

if __name__ == "__main__":
    unittest.main()
