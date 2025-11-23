import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.output.processing as module_1
import httpie.models as module_2

class Test_Streams_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = -1767.311
            h_t_t_p_message_0 = module_2.HTTPMessage(float_0)
            base_stream_0 = module_0.BaseStream(h_t_t_p_message_0)
            bytes_0 = base_stream_0.get_headers()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
