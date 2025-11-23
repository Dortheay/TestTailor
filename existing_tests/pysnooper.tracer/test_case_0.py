import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        unavailable_source_0 = module_0.UnavailableSource()

if __name__ == "__main__":
    unittest.main()
