import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = None
            tuple_0 = (float_0,)
            str_0 = 'r?'
            dict_0 = {float_0: float_0, tuple_0: tuple_0, str_0: tuple_0}
            var_0 = module_0.get_shortish_repr(tuple_0, str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
