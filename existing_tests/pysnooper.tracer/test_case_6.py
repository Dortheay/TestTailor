import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x98'
            list_0 = [bytes_0, bytes_0, bytes_0]
            var_0 = module_0.get_path_and_source_from_frame(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
