import unittest
import timeout_decorator
import httpie.context as module_0
import argparse as module_1
import httpie.output.writer as module_2
import typing as module_3
import httpie.models as module_4
import httpie.output.streams as module_5
import requests.models as module_6

class Test_Writer_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            list_0 = []
            h_t_t_p_message_0 = module_4.HTTPMessage(list_0)
            base_stream_0 = module_5.BaseStream(h_t_t_p_message_0)
            text_i_o_0 = module_3.TextIO()
            bool_0 = False
            var_0 = module_2.write_stream_with_colors_win_py3(base_stream_0, text_i_o_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
