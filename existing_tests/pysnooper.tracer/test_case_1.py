import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\x7f\x9e\xc3\xd2'
        unavailable_source_0 = module_0.UnavailableSource()
        var_0 = unavailable_source_0.__getitem__(bytes_0)

if __name__ == "__main__":
    unittest.main()
