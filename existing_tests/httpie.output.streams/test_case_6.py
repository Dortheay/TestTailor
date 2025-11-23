import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.models as module_1

class Test_Streams_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        h_t_t_p_message_0 = None
        base_stream_0 = module_0.BaseStream(h_t_t_p_message_0)
        iterable_0 = base_stream_0.__iter__()
        binary_suppressed_error_0 = module_0.BinarySuppressedError()

if __name__ == "__main__":
    unittest.main()
