import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = False
            str_0 = '{}.x'
            tracer_0 = module_0.Tracer(bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
