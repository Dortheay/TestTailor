import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '8#w.\x0cg._n('
            int_0 = -4385
            bool_0 = False
            var_0 = module_0.get_shortish_repr(str_0, int_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
