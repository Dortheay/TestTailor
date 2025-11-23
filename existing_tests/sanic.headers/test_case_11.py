import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = ''
        str_1 = module_0.fwd_normalize_address(str_0)

if __name__ == "__main__":
    unittest.main()
