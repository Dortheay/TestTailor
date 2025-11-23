import unittest
import timeout_decorator
import sanic.utils as module_0

class Test_Utils_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '0'
        bool_0 = module_0.str_to_bool(str_0)

if __name__ == "__main__":
    unittest.main()
