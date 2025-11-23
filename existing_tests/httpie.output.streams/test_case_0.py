import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.output.processing as module_1
import httpie.models as module_2

class Test_Streams_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            raw_stream_0 = module_0.RawStream()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
