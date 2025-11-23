import unittest
import timeout_decorator
import sanic.helpers as module_0

class Test_Helpers_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 0.001
            var_0 = module_0.is_hop_by_hop_header(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
