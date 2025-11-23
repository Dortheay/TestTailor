import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            unavailable_source_0 = module_0.UnavailableSource()
            list_0 = None
            list_1 = [list_0]
            tracer_0 = module_0.Tracer(list_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
