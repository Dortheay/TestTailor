import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = None
            list_0 = [bool_0]
            str_0 = '9=1"xcD:YG|A\r+'
            tracer_0 = module_0.Tracer(str_0)
            var_0 = tracer_0.__exit__(bool_0, list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
