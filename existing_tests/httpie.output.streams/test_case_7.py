import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.models as module_1

class Test_Streams_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'sDVI\rJF_y \r\x0bJOdso'
        h_t_t_p_message_0 = module_1.HTTPMessage(str_0)
        optional_0 = None
        base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, optional_0)

if __name__ == "__main__":
    unittest.main()
