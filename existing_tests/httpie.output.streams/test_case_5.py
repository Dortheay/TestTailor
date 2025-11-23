import unittest
import timeout_decorator
import httpie.output.streams as module_0
import httpie.output.processing as module_1
import httpie.models as module_2

class Test_Streams_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'sDVI\rJF_y \r\x0bJOdso'
            h_t_t_p_message_0 = module_2.HTTPMessage(str_0)
            h_t_t_p_message_1 = module_2.HTTPMessage(h_t_t_p_message_0)
            tuple_0 = (h_t_t_p_message_1,)
            h_t_t_p_message_2 = module_2.HTTPMessage(tuple_0)
            dict_0 = {}
            bool_0 = False
            base_stream_0 = module_0.BaseStream(h_t_t_p_message_2, dict_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
