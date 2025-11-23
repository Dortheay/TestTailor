import unittest
import timeout_decorator
import py_backwards.utils.helpers as module_0

class Test_Helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = None
        callable_0 = module_0.eager(float_0)

if __name__ == "__main__":
    unittest.main()
