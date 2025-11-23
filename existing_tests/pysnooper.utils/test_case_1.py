import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        int_0 = -493
        int_1 = 55
        tuple_0 = (bool_0, int_0, int_1)
        var_0 = module_0.ensure_tuple(tuple_0)
        bool_1 = None
        var_1 = module_0.get_shortish_repr(bool_1)

if __name__ == "__main__":
    unittest.main()
