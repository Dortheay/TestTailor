import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        tuple_0 = None
        tracer_0 = module_0.Tracer(tuple_0)

if __name__ == "__main__":
    unittest.main()
