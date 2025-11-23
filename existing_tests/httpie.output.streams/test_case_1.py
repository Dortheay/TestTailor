import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.output.processing as module_1
import httpie.models as module_2

class Test_Streams_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            encoded_stream_0 = module_0.EncodedStream(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
