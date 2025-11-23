import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = ()
            var_0 = module_0.normalize_repr(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
