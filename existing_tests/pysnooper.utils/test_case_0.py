import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'Ug4&PJW*2rc\r6)B'
        var_0 = module_0.ensure_tuple(str_0)

if __name__ == "__main__":
    unittest.main()
